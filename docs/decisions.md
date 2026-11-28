# Decisions log

Newest first. Add an entry whenever a decision changes how the site or résumé should be built.

## Résumé (Nov 2026)
- Two PDFs: one-page and two-page. The live site's "View résumé" link serves the two-page file (`RK-Product_Designer.pdf`, same filename so old links work).
- Built in the portfolio design system: dark theme (page 1 of the two-pager, hero of the one-pager), light theme (page 2 and the one-pager body). Space Grotesk headings, Inter body, Instrument Serif italic for one accent word.
- Profile photo: the Collaboration photo, edited so the sign board sits behind the head. Shape: 50% radius on three corners, square bottom-right. Behind it, a sharp quarter circle in the top-right page corner.
- Experience on page 1 is a vertical tracker (timeline). Page 2 experience has no card containers. The one-pager has no containers and a thin vertical divider between columns.
- All contact items are clickable links (phone, email, portfolio, LinkedIn), on icons and on text.
- Page boxes are cropped to 595.5 x 842.25 pt so no white edge shows (Chromium otherwise adds ~0.6 pt of white).
- Rebuild: see `resume/README.md`.

## Navigation (Nov 2026)
- Same header on every page: Impact, Work, Proposals, AI builds, About. No per-case section links in the header.
- Work is active on Work and every case page. Proposals is active on Design System Usage and Localization Automation. None active on Mechanical Design. Work always goes to the Work page.
- A thin 3 px accent reading-progress line at the top of every page.
- Scroll-spy supports several ids per link (`data-sec="work global"`). The older spy ignores links that have `data-sec`; that fixed "Impact stays active after its section".

## Case-study research rows
- Pattern: crisp rows of what I did / why / what it gave. Done for Digital Charge Verification. Pending for Canada Experience Gap, Manage Credit Limit, ShubhViva (they have the material).

## Open items
- Financial Verification: web screens.
- AI-behaviour case: facts needed from Rakhesh.
- Bulk Payment: check the Figma embed.
- Manage Credit Limit: the three-option tree has no connectors on mobile.
- Live About/hero still use the older portrait; the new Collaboration portrait is only in the résumé so far.
- Word version of the résumé still has the old tagline and design.

## Canvas facts that bite
- The canvas editor's autosave can reset a board height to 8000. `tools/lint.py` flags it. Known heights: BulkPayment 9610, CanadaExperienceGap 11360, DesignSystemUsage 6610, DigitalChargeVerification 19600, FinancialReliefProgram 13900, FinancialVerification 10470, GenericMedicine 9140, GravityDeck 8650, LocalizationAutomation 9720, Main 16330, ManageCreditLimit 13540, MechanicalDesign 10930, Onboarding 7650, PaymentsMexico 10100, PlanItPromoPricing 11120, ShubhViva 14200, SourcX 8750, Work 8570.
- A canvas publish over a hand edit is refused and names the file to re-read; always read the latest first.
