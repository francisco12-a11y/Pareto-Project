# Images — status & prompts

**Status (2026-09-29, final): all three page slots are filled, two with photos Fran supplied directly.**

| Slot | File | What it is | Source |
|---|---|---|---|
| H1 hero | `kasim-podium.jpg` | **Real photo of Kasim giving a talk**: at a podium with mic and MacBook, brick-wall venue, black long-sleeve, smiling (1014×1551) | **Provided by Fran** |
| P1 problem | `room-audience.jpg` | Founders working in the room at a live workshop — full-resolution original (2400×1600) | **Pexels #18999470** ("business-training-course", licensed) — Fran's photo, found and swapped for the low-res copy |
| A1 about | `kasim-headshot.jpg` | Kasim's professional headshot, portrait crop (600×900) | **Provided by Fran** (same photo as `kasim-portrait-1.jpg`, cropped to his framing from the 1000×900 Front Row Dads original) |

The AI-generated composite (`ai-hero-v2.png` → superseded) remains as a spare, generated with `google/gemini-3.1-flash-image` via OpenRouter (Fran's key, script `../gen_hero.py`) from `kasim-conference.jpg` + Pexels #29708270. Spares: `ai-hero-v1.png`, `hero-stage.jpg`, `kasim-portrait-1.jpg`, `kasim-award.jpg` (2024 SaaSPRENEUR Gold photo, replaced by Fran's headshot choice), `kasim-podcast-cover.jpg`, `desk-tired.jpg`.

The AI-generation prompts below are kept as the fallback if any image needs regenerating with a clean license. All images will be AI-generated (or licensed stock as fallback). Never sourced from Google Search. Brand constants for every prompt: palette ink `#101014`, bone `#F7F4ED`, gold `#E9B44C`; editorial, high-contrast, warm; no text baked into images; photoreal grade.

---

## H1 — Hero founder portrait (4:5, right column of hero)

> Editorial studio portrait of a very tall confident male founder in his early 40s wearing a plain black t-shirt, arms crossed, slight knowing half-smile, short dark hair, light stubble. Deep matte charcoal background (#101014), dramatic warm golden rim light from behind left (#E9B44C), soft key light on the face. Photorealistic, shallow depth of field, 85mm lens look, fine grain, magazine-cover grade. Vertical 4:5. No text, no logos, no hands on hips, no laptop.

## P1 — The overloaded operator (21:9, under the problem section)

> Cinematic wide shot of a founder alone at a kitchen table late at night, lit only by two laptop screens and a phone face-up, dozens of open tabs glowing, coffee gone cold, papers with sticky notes pushed aside. His face half in shadow, shoulders rounded, one hand on his forehead. Warm amber screen glow against a dark room (#101014 tones), one thin gold light streak (#E9B44C) from a doorway in the background. Photorealistic, 21:9, moody editorial documentary grade, fine film grain. No text visible on screens, no brand logos.

## A1 — Kasim on stage (4:5, about section)

> Editorial photograph of a very tall speaker in a plain black t-shirt on a small event stage, mid-gesture, talking to a seated audience of founders seen from behind in soft focus. Stage lit warm gold (#E9B44C) against a dark room (#101014), strong silhouette, black t-shirt, relaxed posture, holding no clicker. Photorealistic, 4:5 vertical, 50mm lens look, documentary event photography grade. No readable text on screens behind him, no logos.

## OG — Social share card (1200:630, optional, for og:image)

> Minimal social card on near-black (#101014): a single large four-point north star in warm gold (#E9B44C) centered high, generous negative space below for a headline to be overlaid in type. Subtle film grain, no other elements, no text.

## S1 — Star texture (16:9, optional spare)

> Abstract macro of a dark charcoal surface (#101014) with a single gold four-point star embossed and catching warm light, extreme minimalism, soft vignette, fine grain. No text.
