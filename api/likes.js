// Like counter for the portfolio. Stores one integer in Redis (Upstash / Vercel KV REST API).
// Needs two env vars on the Vercel project (either naming works):
//   UPSTASH_REDIS_REST_URL + UPSTASH_REDIS_REST_TOKEN   or   KV_REST_API_URL + KV_REST_API_TOKEN
// GET  /api/likes            -> { count, liked }   (count is null until the store is connected)
// POST /api/likes {action}   -> { count, liked }   action: "like" | "unlike"
// One like per visitor (hashed IP + user agent, kept 90 days) so refreshing cannot inflate the count.
const crypto = require('crypto');

const URL_ = process.env.UPSTASH_REDIS_REST_URL || process.env.KV_REST_API_URL;
const TOKEN = process.env.UPSTASH_REDIS_REST_TOKEN || process.env.KV_REST_API_TOKEN;
const KEY = 'portfolio:likes';
const ORIGINS = ['https://rakhesh-design.vercel.app'];

async function redis(cmd) {
  const r = await fetch(URL_, {
    method: 'POST',
    headers: { Authorization: 'Bearer ' + TOKEN, 'Content-Type': 'application/json' },
    body: JSON.stringify(cmd),
  });
  if (!r.ok) throw new Error('redis ' + r.status);
  return (await r.json()).result;
}

module.exports = async (req, res) => {
  const origin = req.headers.origin;
  let host = '';
  try { host = new URL(origin).hostname; } catch (e) {}
  if (host && (ORIGINS.includes(origin) || /^(localhost|127\.0\.0\.1)$/.test(host) || /\.vercel\.app$/.test(host) || /(^|\.)claude\.(ai|com)$/.test(host))) {
    res.setHeader('Access-Control-Allow-Origin', origin);
    res.setHeader('Vary', 'Origin');
  }
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');
  res.setHeader('Cache-Control', 'no-store');
  if (req.method === 'OPTIONS') return res.status(204).end();
  if (!URL_ || !TOKEN) return res.status(200).json({ count: null, liked: false, configured: false });

  try {
    const ip = String(req.headers['x-forwarded-for'] || req.socket.remoteAddress || '').split(',')[0].trim();
    const who = 'portfolio:liker:' + crypto.createHash('sha256').update(ip + '|' + (req.headers['user-agent'] || '')).digest('hex').slice(0, 32);

    if (req.method === 'POST') {
      let body = req.body;
      if (typeof body === 'string') { try { body = JSON.parse(body); } catch (e) { body = {}; } }
      const action = body && body.action;
      if (action === 'like') {
        const fresh = await redis(['SET', who, '1', 'NX', 'EX', 7776000]);
        if (fresh === 'OK') await redis(['INCR', KEY]);
      } else if (action === 'unlike') {
        const removed = await redis(['DEL', who]);
        if (removed === 1) await redis(['DECR', KEY]);
      } else {
        return res.status(400).json({ error: 'action must be like or unlike' });
      }
    } else if (req.method !== 'GET') {
      return res.status(405).json({ error: 'method not allowed' });
    }

    const [count, liked] = await Promise.all([redis(['GET', KEY]), redis(['EXISTS', who])]);
    return res.status(200).json({ count: Math.max(0, parseInt(count || '0', 10)), liked: liked === 1, configured: true });
  } catch (e) {
    return res.status(502).json({ count: null, liked: false, error: 'store unavailable' });
  }
};
