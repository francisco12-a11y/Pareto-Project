# Star Founder — landing page for Kasim Aslam

**Preview URL (local):** [http://127.0.0.1:8901](http://127.0.0.1:8901) — served from this folder (`python3 -m http.server 8901`).

Sample founder: **Kasim Aslam**. Everything on the page is built from his Second-Brain vault (`../Second-Brain/`). Process order followed exactly: brief → offer → inverse interview → copy → brand → page.

## The submission map

| Deliverable | File |
|---|---|
| Brief (one offer, one audience, one action) | [brief.md](brief.md) |
| Grand Slam Offer (Hormozi method, vault's own Day-5 math) | [offer.md](offer.md) |
| Inverse interview (20 questions, answered from the vault) | [interview.md](interview.md) |
| Copy for every section, final wording | [copy.md](copy.md) |
| Brand system | [brand.md](brand.md) |
| The page (10 sections) | [index.html](index.html) |
| Logo | [assets/logo.svg](assets/logo.svg) |
| Favicon | [assets/favicon.svg](assets/favicon.svg) |
| Image prompts (3 on-page slots + 2 spares) | [assets/prompts.md](assets/prompts.md) |

## Assignment checklist

- **Brief** — one offer (Star Founder, the vault's own "10-week Kasim cohort" from BC7 Day 5), one audience (founders with traction who are still the operator), one action (apply; every button goes to `#apply`).
- **Grand Slam Offer** — value equation, 10X stack, conditional guarantee, real scarcity; built with the exact anatomy taught in the vault's `hormozi-method.md`.
- **Inverse interview** — 20 strategist questions answered only from vault notes, each with source.
- **Copy first** — `copy.md` was finished before `index.html` was written; the page transcribes it.
- **Brand system** — one logo + favicon (four-point north-star mark), three colors (ink `#101014`, bone `#F7F4ED`, gold `#E9B44C`), one Google Font pair (Space Grotesk + Inter), one icon set (Lucide, inline sprite, 19 icons, single style).
- **Images** — 3 on-page slots, all filled with photos of Kasim's world (see [assets/prompts.md](assets/prompts.md)): hero = real photo of Kasim at the podium (provided by Fran), problem = live-workshop room shot (provided by Fran), about = his 2024 award photo. An AI composite hero (OpenRouter `google/gemini-3.1-flash-image`, Fran's key) was built first and is kept as a spare.
- **8+ sections** — hero, social proof, problem, how it works, benefits, the solution (the offer), guarantee, about, FAQ, final CTA = 10. (The application form is deliberately absent for now: the final CTA holds a placeholder button; the GoHighLevel form embeds there later.)

## What's real vs. written (per the vault's "never invent facts" rule)

**Real, from the vault:** all credentials and numbers (6 businesses / 3 exits, #1-ranked Google Ads agency, $100M+ ad spend, 40% vs 20% margins, $2,000/hr, $1.5M contracts, $490k storage deal, $1M-in-year-one Pareto Talent), the frameworks (Miracle Brief, 2-6-2, Core + Edge, Evolution Engine, Second Brain), the offer structure and price ($3,000; the vault's own Day-5 math: "≈ $30k stack, sell at $3k"), the story beats (welfare childhood, candy, the cemetery of failed businesses, the Ukrainian EA → 50/50 partner). The Feldberg/Nelson press quotes were cut from the page per Fran's decision (kept in copy.md for reference); the social-proof quote cards are the sample testimonials below.

**Marketing layer, flagged:** the name "Star Founder" (Fran's concept, vault grounds the substance); cohort start date "January 11, 2027" and "25 seats" (placeholders; vault pattern is small rooms, first Pareto cohort was 11); the two $500 bonus prices (stack pricing; the $40,000 / $3,000 / $2,400 components trace to vault numbers); the Bottleneck Guarantee wording (new, built on Hormozi type 3 per the vault's method note; Pareto's real guarantee is lifetime EA replacement); **the three founder testimonials (Marcus T., Priya S., Daniel R.) are fictional samples** Fran requested for the demo — framed as coaching clients rather than cohort grads so they don't contradict the January 2027 start date; swap with real participant quotes before any real deployment (HTML comment marks the spot).

## Wire it up when real

- Form: the final CTA section holds a placeholder button with an HTML comment marking the spot — drop the GoHighLevel form embed there (the vault confirms Pareto runs on GHL).
- Images: live. If the desk shot needs a clean license, regenerate from `assets/prompts.md` and swap `assets/desk-hoodie.jpg`.
- og:image: set to the hero portrait; swap in a designed card later if wanted.
