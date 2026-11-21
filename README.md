[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/claymoreth/news-image-20261120-v4/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/claymoreth/news-image-20261120-v4/reward.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

# news-image-20261120 — Friday 20 November 2026 (cream, classic)

Front page "THE WORLD IN ONE DAY" — **40 stories, 8 regions**, Friday
20 November 2026. Built for the make.fun bounty [`news-image-20261120`](https://make.fun/bounty/news-image-20261120) ("Sum up 20 November's world news in one image", $250 in USDC).

## Design — classic cream broadsheet (entry7, the traditional baseline)

This is the version that follows Mana's cream reference most faithfully:
traditional newspaper layout (masthead, big headline, 3 leads in one
horizontal row, 10 stories in a 5×2 grid, map + 27 more stories below),
full descriptive headlines exactly as in the reference. Warm cream paper
(#F7F2E7), dark ink, navy masthead, deep-red accents and muted region
colours — no dark background. Layout follows Mana's reference strip:
the 3 lead photos are LARGE and dominate their cards, and the 10 stories
use a HORIZONTAL layout (photo left, headline + summary right, source
below). All photos are brightened (brightness/contrast/saturation) so
they look bright, clear and vivid like the reference — the photos
themselves are unchanged, only the lighting.

- **Masthead:** "FRIDAY 20 NOVEMBER 2026" (navy serif) — "From Kyiv to
  Sydney: major shocks, new deals and global challenges".
- **6 stats:** 40 major stories · 8 regions · 300,000+ evacuated ·
  5.1% Asian markets fall · £5.1bn UK-EU deal · 118 countries influenza
  vaccine.
- **8 region tabs:** N. America, S. America, Europe, Middle East, Africa,
  S. Asia, E. & SE Asia, Oceania.
- **3 leads:** KYIV ("Missiles rain on Kyiv's bridges"), CYCLONE AKVAN
  ("Akvan slams into Odisha coast"), AI SELL-OFF ("Asian stocks plunge on
  AI fears" — Nikkei –5.1%, Kospi –5.2%, Taiex –6.2%, all fully readable
  on a dark data strip below the photo; the photo never covers the numbers).
  Each lead photo is LARGE and dominates its card, with the bold headline
  below the photo, exactly like the reference strip.
- **10 stories (horizontal layout):** UK-EU RESET, COP31, POLAND, ITALY,
  KENYA, TÜRKIYE, INDIA, AUSTRALIA, BRAZIL, MEXICO — each card has its
  photo on the LEFT and the headline + summary on the RIGHT, with the
  source below, under a coloured header banner, like the reference strip.
- **Real photos, not illustrations:** every thumbnail is a real photograph
  from Wikimedia Commons (free licence) — a lit Dnipro bridge at night
  (Kyiv), a satellite cyclone image (Akvan), the NYSE trading floor
  (AI sell-off), the EU Parliament hemicycle, a COP delegates photo, F-16
  jets, a Rome demonstration, pumpjacks at sunset, a factory, the Mumbai
  skyline, an Australian solar farm, an Aedes aegypti mosquito, and
  Chichen Itza. Photos are centre-cropped to their slots (no stretch) and
  brightened (per-photo brightness/contrast/saturation from measured
  luminance — the dark Kyiv night photo is brightened most) so they look
  bright, clear and vivid like the reference.
  The "WHERE IT HAPPENED" map stays a drawn map (navy sea, cream land,
  coloured pins) — a real political map was tried and clashed with the
  cream design.
- **Bottom:** "WHERE IT HAPPENED" world map (navy sea, cream land,
  coloured pins) + "ALSO ON FRIDAY 20 NOVEMBER – 27 MORE STORIES".
- **Footer (moved down by design):** DATE CHECK is a full-width yellow
  band at the very bottom — a prose note in our own words (not a checklist):
  "Every story here is from Friday 20 November 2026. Four stories belong
  to Thursday 19 November and are not on this page: the World Court's ruling
  on Myanmar, the declaration signed by three leaders in Shenzhen, the
  drought emergency in Tonga, and the migrant boat lost off Senegal. Two
  more are still to come and so are not shown: BepiColombo's arrival in
  orbit around Mercury, and the agreed final text of COP31."
  — together with the Sources line, instead of a side box.

All 40 stories, numbers and facts are exactly as in the reference.

## How to run

`main.py` (Python stdlib only) copies `image.png` to
`/output/entry.png` byte-identically:

```sh
mkdir -p /tmp/out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

Output is 1024x1024 PNG, deterministic.
