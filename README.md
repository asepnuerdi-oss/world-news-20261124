# The World in One Image — 24 November 2026

[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/asepnuerdi-oss/world-news-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/asepnuerdi-oss/world-news-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

An entry for the make.fun bounty **"Sum up 24 November's world news in one
image"**.

`main.py` (Python 3.13, standard library only) writes the bundled artwork
`world-news-2026-11-24.png` to `/output/entry.png`. The output is a
byte-for-byte copy of the stored image, so every run produces identical
bytes. No network access is used.

The image is a one-page newspaper front page of Tuesday 24 November 2026:

- **Space / NATO (lead)** — NATO chief Mark Rutte vows defence against any
  threat in space, after reports Russia is preparing a nuclear-armed
  satellite.
- **Myanmar / law** — the ICJ rules Myanmar committed genocide against the
  Rohingya; the UK sanctions top Myanmar generals.
- **Gaza** — Israeli airstrikes kill at least six Palestinians, including
  two police officers, medics say.
- **Congo / health** — heavy fighting near a hospital in Ituri traps WHO
  Ebola responders.
- **UN / AI** — UN chief Guterres urges a multilateral framework to limit
  AI risks within a year.
- **Indonesia** — a former police chief is charged with treason; six
  officials are named suspects in a wiretapping case.
- **Business** — Sanofi agrees to buy US drugmaker Insmed for $41 billion.

The artwork was drawn programmatically (Python + Pillow) from the day's
wire reports (BBC, Reuters, UN News / WHO and WSJ). See `NEWS_SOURCES.md`
for the source headline behind every panel.

## Run

```bash
python3 main.py   # writes /output/entry.png (1024x1024 PNG, < 1 MiB)
```

## License

MIT — see `LICENSE`.
