# Brand System — Star Founder

One mark, three colors, one font pair, one icon set. Anti-corporate on purpose: Kasim is a black-t-shirt founder who says "failure just feels like data." The brand should read like a sharp editorial publication, not a SaaS.

## Logo

**V7 "minimal compass"** — chosen from 7 variants (see `variants.html`, all files in `assets/logo-variants/`): an **8-point compass star** (four-point star + the same star rotated 45° at 45% opacity) in gold beside "STAR FOUNDER" set wide in Space Grotesk 500, single line, no descriptor.
**assets/logo-variants/v7-minimal-compass.svg** — the full lockup (source of truth).
**assets/favicon.svg** — the compass mark alone on an ink rounded chip.
The mark says: the founder as the fixed point the business navigates by. The section-marker bullets inside the page still use the four-point star alone; the compass appears in the header, footer and favicon.

## Palette (three colors, full stop)

| Token | Hex | Use |
|---|---|---|
| Ink | `#101014` | Hero, offer, final CTA backgrounds; all body text on light |
| Bone | `#F7F4ED` | Page background; sections 2–5; text on ink |
| Star Gold | `#E9B44C` | The mark, CTA fills, rules, one highlight per section maximum |

Tints are opacity steps of these three (e.g. bone-on-ink at 70% for secondary text, ink at 6% for card borders). No fourth hue anywhere.

Gold carries exactly one job per section. It never fills a body text run.

## Type — Google Font pair

**Space Grotesk** (500/700) for display and headings. Techy-editorial, slightly contrarian, matches a founder who leads with the uncomfortable claim.
**Inter** (400/600) for body and UI. Invisible at reading size, which is the point.
Both from Google Fonts; the pair is one of Google Fonts' own suggested pairings for Space Grotesk.

Scale: hero 88px clamp, section heads 48px, body 18px/1.65. Headlines set in Space Grotesk 700 with tight tracking (-0.03em); body Inter at normal tracking.

## Icon set — Lucide

One set, one style: Lucide, inline `<symbol>` sprite, 24px grid, stroke 1.75, round caps and joins, currentColor. No one-off icons from anywhere else.

In use: arrow-right (CTAs), check (stack list), clock, calendar-check, users, user-check, compass, layers, refresh-cw, brain, eye, zap, shield-check, quote, book-open, chevron-down (FAQ), arrow-up-right (footer links), sparkles (brand bullets), trending-up.

## Layout rules

- Alternating ink/bone bands; the offer and final CTA are ink so the money sections feel like the same room.
- Section eyebrows: gold star mark + small caps label + section number (01–10).
- One CTA action everywhere: "Ready to Become a Star?" → #apply.
- Numbers always in Space Grotesk, always gold or ink, never bone-on-bone.
- Quotes carry a gold rule and the Lucide quote mark, no speech bubbles, no headshots we don't own.
