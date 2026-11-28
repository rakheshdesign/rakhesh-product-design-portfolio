def ic(name):
    P={'phone':'M6.6 10.8a15 15 0 0 0 6.6 6.6l2.2-2.2a1 1 0 0 1 1-.25 11.4 11.4 0 0 0 3.6.6 1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1c0 1.25.2 2.45.6 3.6a1 1 0 0 1-.25 1z',
       'mail':'M3 5h18a1 1 0 0 1 1 1v12a1 1 0 0 1-1 1H3a1 1 0 0 1-1-1V6a1 1 0 0 1 1-1zm9 7.2L4.2 7v10.5h15.6V7z',
       'globe':'M12 2a10 10 0 1 0 0 20 10 10 0 0 0 0-20zm6.9 9h-3a15.7 15.7 0 0 0-1.3-5.6A8 8 0 0 1 18.9 11zM12 4c.9 1 1.9 3.1 2.2 7H9.8C10.1 7.1 11.1 5 12 4zM4.1 13h3a15.7 15.7 0 0 0 1.3 5.6A8 8 0 0 1 4.1 13zm3-2h-3a8 8 0 0 1 4.3-5.6A15.7 15.7 0 0 0 7.1 11zM12 20c-.9-1-1.9-3.1-2.2-7h4.4c-.3 3.9-1.3 6-2.2 7zm2.6-1.4a15.7 15.7 0 0 0 1.3-5.6h3a8 8 0 0 1-4.3 5.6z',
       'in':'M4.5 9h3.7v11.5H4.5zM6.3 3.5a2.1 2.1 0 1 1 0 4.2 2.1 2.1 0 0 1 0-4.2zM10.5 9h3.5v1.6h.05c.5-.95 1.7-1.95 3.5-1.95 3.75 0 4.45 2.45 4.45 5.65v6.2h-3.7v-5.5c0-1.3 0-3-1.85-3s-2.1 1.4-2.1 2.9v5.6H10.5z'}
    return f'<svg viewBox="0 0 24 24" width="100%" height="100%"><path fill="currentColor" d="{P[name]}"/></svg>'
def circ(name,url,size=26):
    return f'<a class="ci" style="width:{size}px;height:{size}px" href="{url}"><span style="width:{size*0.58}px;height:{size*0.58}px;display:block">{ic(name)}</span></a>'
PORT='https://rakhesh-design.vercel.app'; LI='https://in.linkedin.com/in/rakheshkarnati'
PHONE='+91 7036534813'; EMAIL='rakheshkarnati@gmail.com'
SUMMARY=("Product Designer with 6 years of design experience, 4+ in product design, across fintech and healthcare (B2B and B2C). "
 "Lead Designer on credit-limit, financial-relief and fraud-verification journeys across 10+ US and international markets at American Express.")
SUMMARY2=("Turns research and experiments into measurable results, scales design through Figma Variables and the design system, and builds AI-assisted products end to end. "
 "Strongest as a collaborator: works with Product, Engineering, Risk and Business every day, runs workshops that align teams before design starts, and mentors designers across teams.")
STATS=[('+44%','mobile completion, 2× web'),('+13%','enrollment conversion'),('6','markets launched'),('~20%','revenue growth, Saveo'),('~60%','less designer time per market')]
AMEX_SCOPE="Lead Designer across 5 customer-facing financial modules in the mobile app (credit limit, payment flexibility, financial relief, fraud verification, underwriting), partnering with Product, Engineering, Content and Business in the US and abroad. Also Design System Ambassador."
AMEX=[
"Launched credit-limit management in <b>6 markets</b>, contributing to <b>+44% mobile completion</b> (2× web), by designing one shared journey where only wording and verification depth change by market.",
"Helped lift Financial Relief Program enrollment conversion by <b>13%</b> (core step 13.1% to 14.9%), by cutting the review step, adding side-by-side plan comparison and simplifying the landing page.",
"Avoided a <b>6% drop in completion</b> and a 5% rise in support contacts, as measured by a 35-day 50/50 test, by pushing back on leadership's plan to remove a landing page and proposing the test.",
"Designed a net-new fraud-verification feature that keeps Card Members calm, as measured by user acceptance testing across three finalist versions, by turning a yes-or-no alert into one guided review.",
"Cut the risk of accidental credit-limit decreases in Canada, as measured by testing with no mental math, confusion or dilemma, by showing the change live as people type and confirming both limits. Other markets can adopt the pattern.",
"Cut designer time per market by <b>~60%</b> and enabled a new market in under 4 days on Plan It, by moving market strings into Figma Variables and aligning Product, Tech and Design on one handoff.",
"Pitched market, breakpoint and platform modes in Figma Variables to Design and Research, aiming for ~80% less copy-and-paste (my estimate, not yet measured), by switching wording with Variables modes or the Applanga Global Strings plugin.",
"Equipped <b>about 20 designers across 3 teams</b>, with sessions open to the whole American Express design forum, to build with Auto Layout, Variables and conditionals, by mentoring them, while working with the design-system team on component fixes and the move to the uplifted V7 system.",
]
SAVEO_SCOPE="Designed B2B and B2C products across mobile, web and dashboards (Saveo, SilverCross, Medcross, Clinn, Medbook), working with Product, Engineering, Business and Marketing."
SAVEO=[
"Grew revenue by <b>~20%</b>, as measured by incremental revenue from generic medicine recommendations, by proposing and designing high-margin generic alternatives in search, product pages and the cart.",
"Cut onboarding friction by <b>~30%</b>, as measured by retailer sign-up friction, by breaking registration into one phone number, three short steps and a clear verification state.",
"Cut collection-team effort <b>~5×</b>, as measured by daily work efficiency, by replacing Excel tallying with one Bulk Settlement dashboard that maps every payment to its invoices.",
"Conceptualized Capsi AI, a conversational bot that kept retailers engaged while teaching them medical and pharma topics.",
]
EARLY=[("Bommu Herbals","Motion Graphic Designer","Jun 2021 to Feb 2022","Designed e-commerce experiences, packaging and motion assets for a consumer brand."),
("Strategic Innovative Ads","Graphic-Motion Designer","Jul 2020 to Jun 2021","Designed web, campaign and motion work for clients across industries.")]
AI_ITEMS=[("At American Express","use Figma Make and Replit to generate prototypes, ideas and MVPs across the design process, to ideate, brainstorm and speed up work."),
("ShubhViva (live)","built an India-first wedding platform that starts with the invitation, in 6 languages and 16 designs, with AI as my build partner."),
("Gravity (live)","built a web deck maker where every element is a ball and slides morph instead of cutting."),
("SourcX (2023)","designed both sides of an AI-first outsourcing marketplace, with plain-language search and side-by-side comparison.")]
SKILLS=[("AI","AI-assisted design and building (Claude Design, Claude Code, Replit, Figma Make, Copilot) • Human-AI interaction design"),
("Research &amp; Optimization","Usability and user acceptance testing • Journey mapping • A/B experiments • Hypotheses and synthesis"),
("Design Systems &amp; Scale","Design systems • Figma Variables • Localization (L10n) • Internationalization (i18n) • Component libraries"),
("Product &amp; UX","End-to-end product design • Interaction design • Information architecture • User flows • Prototyping • Accessibility (A11Y) • Product thinking"),
("Collaboration &amp; Leadership","Cross-functional partnership with Product, Engineering, Content, Risk and Business • Workshop facilitation • Stakeholder management • Mentoring • Design critique"),
("Tools","Figma • FigJam • Miro • Whimsical • Adobe Creative Suite • ClickUp")]
EDU="B.Tech, Mechanical Engineering (VBIT)<br>Jawaharlal Nehru Technological University, Hyderabad"
CERTS=["Digital Skills: User Experience","Enterprise Design Thinking Practitioner"]
NOTE="~ means reported by the team or estimated by me, not independently measured."