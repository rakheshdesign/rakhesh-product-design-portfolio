---
name: "rakhesh-portfolio-design-system"
description: "Design system, taste, approach and content voice for Rakhesh Karnati's product design portfolio; use for any page, section, component, illustration or copy for that portfolio or its case studies."
---

# Rakhesh Karnati portfolio: design system, taste and content

Use for any new or changed screen, section, component, illustration, chart or copy in the portfolio (canvas artifact, rakhesh-design.vercel.app). Read CONTINUE_HERE.md and the content briefs too when available.

## 1. Positioning (what every decision serves)
- Product Designer at American Express (Bangalore), owns the Core Portfolio, leads US and international design. Target: Senior Product Designer with an AI Product Designer angle.
- The portfolio must read as senior, calm, evidence-led and human. Outcomes and judgement first, decoration second.
- Title is always "Product Designer". About speaks only about product design (Product design, AI, Experience). Engineering, CAD and 3D printing sit behind one secondary button ("See the engineering side") and the Mechanical Design page.

## 2. Tokens
Light (.th): bg #F7F9FC, bg2 #EEF2F7, card #FFFFFF, card2 #F1F4F8, ink #101318, ink2 #44505F, ink3 #5B6879, line #D9E0E8, line2 #E4E9F0, accent #0F7A4D, fill #0B8450 (fillink #FFFFFF), accent2 #4B54D6, warn #8A5F00, bad #C22F2F, button #101318 on #F7F9FC.
Dark (data-theme="dark"): bg #07090D, bg2 #0B0F16, card #0F131B, card2 #151A22, elev #141A2E, ink #F5F7FA, ink2 #A9B4C3, ink3 #8491A3, line #1F2733, accent #66F5B2, accent2 #9E9EFF, warn #F5C451, bad #FF7B7B, button #F5F7FA on #07090D.
Always use the CSS variables, never hard-coded hex in components. Both themes must pass contrast.
Elevation: e1 subtle, e2 cards (0 2px 4px / 0 12px 26px -10px), e3 hover and overlays (0 4px 8px / 0 30px 64px -22px). Soft shadows only.
Radius: cards 22px, tiles 12-16px, panels 28px, buttons and tags fully round (999px).
Layout: max width 1360px, 40px side padding (16px on phones), generous vertical rhythm, 1px hairline borders.

## 3. Typography
- Display and UI: Space Grotesk 500-700, tight tracking (-0.02 to -0.025em), headings clamp(30px, 4.4vw, 64px) / 1.08, text-wrap balance.
- Body: Inter 400-600, lead 19px / 1.6 in ink2.
- Accent: Instrument Serif italic in the accent colour for ONE phrase inside a heading (e.g. "A little about how I think and work." with the last phrase in italic serif).
- Kicker: Space Grotesk 13px, 600, uppercase, +0.08em, ink3. Tags: 12px, 700, uppercase, +0.06em, pill with 1px border; .tag.ok uses accent.
- Rule: no more than two text styles in a single line of copy (regular plus one accent).

## 4. Components
- Buttons: pill, min-height 48px (44px touch minimum everywhere), Space Grotesk 16/600. Primary = ink fill, turns green fill with soft glow on hover and lifts 2px. Secondary = transparent with hairline, border turns accent on hover. Icon button 44px round.
- Cards: card colour, 1px line, 22px radius, e2; .lift hover moves up 4px, e3, accent border.
- Header: floating rounded bar with blur. At <=1100px nav collapses to a drawer; below 640px the Say hello button becomes an icon.
- Mobile menu: glass panel (blurred, semi-transparent elevated colour) over a blurred, dimmed page; tapping the blur closes it. Items in order: Home, Impact, Projects (to Work page, not a project list), AI builds (not a list of AI products), Leadership, About, Beyond product design (quiet), then a full-width "Say hello" mail-icon button. Numbered rows (01-06), 24px Space Grotesk, staggered entrance. On other pages, links point to Main.dc.html#anchor.
- Charts: solid fills only, never gradients; label results vs targets vs concepts honestly.
- Principle cards (About): icon tile 44px + bold title + one short line; one column on phones, two on desktop. Keep copy tiny.

## 5. Illustrations
- Small, crisp, geometric, 48x48 viewBox, 2px strokes (ink3), accent for the one thing that matters, card and line tints for the rest. Never large hero illustrations in cards.
- Classes: .il .ln outline, .fa accent fill, .fb soft accent, .fc card fill. One idea per icon (magnifier = real problem, toggle = consequence, node tree = system, bars = measure).

## 6. Motion
- Scroll-driven reveals (view timeline, entry 0-55%), subtle only; hover lifts 2-4px; flow diagrams loop gently (Observe, Reflect, Make, back to Observe); the orbit and portrait stage are the only showpieces.
- Always honour prefers-reduced-motion. Never block content behind animation.

## 7. Content voice
- First person, warm, plain and senior. Short sentences, concrete nouns, no buzzwords or hype. Say what changed and why it mattered.
- Structure for cases: context, the real problem, what I did, decision and trade-off, outcome with honest labelling, what I would do next.
- Never invent metrics. Check 08_IMPACT_AND_METRICS.md and 10_FACTS_AND_GAPS.md. Mark targets and concepts as such.
- Sample voice: "I care about curiosity, careful problem-solving, and the belief that good design makes complex things easier."
- Headline pattern: plain words plus one italic serif accent phrase. Kickers are one or two words.

## 8. Page structure (Home)
Hero (portrait stage) > Moments > Outcomes (before projects) > Selected work (stacked cards) > Working Method flow > Proposal > AI builds > Leadership > Range > About (cards left, photo right, CTA after cards) > Like > Footer.

## 9. Do not
- No gradients on chart bars. No more than two text styles per line. No dense lists in the mobile menu. No CAD or mechanical chips in About.
- Do not bring back: the "How I design AI behaviour" block, the Financial Verification outcome card, the hero cursor hint, the hero "More about me" button.
- No large illustrations in small cards, no decorative stock imagery, no unverifiable claims.

## 10. Quality bar (check before shipping)
1280px and 390px, light and dark; menu open at 390px; 44px touch targets; contrast; links (Projects to Work, AI builds to #ai); no console errors; Like count loads. Never push live unless asked.