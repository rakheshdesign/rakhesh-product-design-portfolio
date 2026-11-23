# Rakhesh Karnati — Product Design Portfolio

Static site (no build step). Deploy on Vercel with Framework Preset "Other", empty Build Command and Output Directory.

Routes: `/`, `/work`, `/work/<project>`. Case visuals are recreations with illustrative data.

## Like counter

The "Like" button on the home page talks to `api/likes.js`, a Vercel serverless function that stores the count in Redis through its REST API.

To turn it on: in the Vercel dashboard open the project, go to Storage / Marketplace, add Upstash Redis and connect it to the project (this sets `UPSTASH_REDIS_REST_URL` and `UPSTASH_REDIS_REST_TOKEN`, or the `KV_REST_API_*` equivalents), then redeploy.

Until a store is connected the page shows "–" and likes are not saved. The current count can be read at `/api/likes`.
