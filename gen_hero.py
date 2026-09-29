#!/usr/bin/env python3
"""Generate the Kasim-on-stage hero via OpenRouter (gemini flash image).

Sends Kasim's portrait (identity) + the stage photo (scene) and asks the model
to put the man on the stage. Saves the returned image to assets/ai-hero-<tag>.png.
Usage: python3 gen_hero.py <tag> [prompt-extra]
"""
import base64, io, json, os, sys, urllib.request
from PIL import Image

TAG = sys.argv[1] if len(sys.argv) > 1 else "v1"
EXTRA = sys.argv[2] if len(sys.argv) > 2 else ""

KEY = None
for line in open(os.path.expanduser("~/.zcode/.env")):
    if line.startswith("OPENROUTER_API_KEY="):
        KEY = line.strip().split("=", 1)[1]
if not KEY:
    sys.exit("no OPENROUTER_API_KEY in ~/.zcode/.env")

def b64_image(path, max_w=800):
    im = Image.open(path).convert("RGB")
    if im.width > max_w:
        im = im.resize((max_w, int(im.height * max_w / im.width)), Image.LANCZOS)
    buf = io.BytesIO()
    im.save(buf, "JPEG", quality=88)
    return "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()

kasim = b64_image("assets/kasim-conference.jpg", 768)
stage = b64_image("assets/base-mic.jpg", 800)

PROMPT = (
    "Image 1 is a portrait of a man: long dark hair, black t-shirt, warm smile. "
    "Image 2 shows a different man on a dark stage holding a microphone, facing the camera, "
    "wearing a black t-shirt. Edit image 2: replace the speaker's head, face and hair with the "
    "man from image 1 — identical face, identical long dark hair, same warm smile. "
    "Keep everything else in image 2 exactly as it is: the black t-shirt, the microphone held to his mouth, "
    "his pose, the dark stage background, the cool blue-teal stage lighting. "
    "Light his face to match the stage: cool ambient with a soft warm key from the front. "
    "Photorealistic, seamless, no borders or watermarks. " + EXTRA
)

body = json.dumps({
    "model": "google/gemini-3.1-flash-image",
    "modalities": ["image", "text"],
    "messages": [{
        "role": "user",
        "content": [
            {"type": "text", "text": PROMPT},
            {"type": "image_url", "image_url": {"url": kasim}},
            {"type": "image_url", "image_url": {"url": stage}},
        ],
    }],
})

req = urllib.request.Request(
    "https://openrouter.ai/api/v1/chat/completions",
    data=body.encode(),
    headers={
        "Authorization": f"Bearer {KEY}",
        "Content-Type": "application/json",
    },
)
with urllib.request.urlopen(req, timeout=180) as r:
    resp = json.load(r)

msg = resp["choices"][0]["message"]
note = (msg.get("content") or "")[:200]
images = msg.get("images") or []
if not images:
    print("NO IMAGE IN RESPONSE. text:", note)
    sys.exit(1)

for i, img in enumerate(images):
    url = img.get("image_url", {}).get("url", "")
    if "," in url:
        payload = base64.b64decode(url.split(",", 1)[1])
        out = f"assets/ai-hero-{TAG}.png"
        open(out, "wb").write(payload)
        print(f"saved {out} ({len(payload)//1024} KB). model note: {note}")
