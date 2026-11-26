# news-image-20261126

[![make.fun · news-image-20261126](https://make.fun/badge/news-image-20261126.svg)](https://make.fun/bounty/news-image-20261126?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)
[![rank](https://make.fun/badge/news-image-20261126/aldayy20/news-image-20261126/rank.svg)](https://make.fun/bounty/news-image-20261126/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)
[![reward](https://make.fun/badge/news-image-20261126/aldayy20/news-image-20261126/reward.svg)](https://make.fun/bounty/news-image-20261126?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)

One image summing up the world's news of Thursday 26 November 2026: Taiwan says it will keep its agreed 15% US tariff rate a day after Trump fired a new salvo at 14 trading partners, Macy's Thanksgiving Day Parade is pushed to Saturday by storm winds, the US Air Force unveils F-15EX fighters at Kadena, Flipkart's chief steps down in December, Kenya secures 293,600 job opportunities in Saudi Arabia, Gukesh and Sindarov play Game 3 of the World Chess Championship in Geneva — and Liverpool, Barcelona and Inter win on Champions League Wednesday night. (Note: all seven stories were reported on 26 November 2026.)

## What's in the image

Seven stories from Thursday 26 November 2026, in one newspaper-style poster:

1. **Taipei holds the line** — Taiwan says it is confident of keeping its agreed 15% US tariff rate, a day after Trump fired a new salvo at 14 trading partners; China faces 20%, the EU, Japan and South Korea are capped at 15%.
2. **Parade pushed to Saturday** — Macy's Thanksgiving Day Parade moves to Saturday as gales bear down on New York; storms threaten Thanksgiving travel for 250m Americans.
3. **F-15EX fighters at Kadena** — the US Air Force unveils its newest F-15EX fighters at Kadena Air Base in Okinawa.
4. **Flipkart chief to step down** — Flipkart CEO Kalyan Krishnamurthy steps down in December.
5. **293,600 jobs in Saudi** — Kenya secures 293,600 job opportunities in Saudi Arabia for its workers.
6. **Game 3 in Geneva** — Gukesh and Sindarov, both 20, play Game 3 of the youngest world title match in 140 years.
7. **Sport** — Liverpool 3-0 Club Brugge, PSG 2-2 Roma, Lille stun Bayern 2-1; Barcelona 4-1 Sabah, Manchester United 2-2 Sporting.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

`main.ts` (Node 22, standard library only) copies `entry.png` — a 1024×1024 PNG drawn by `render.py` from the day's reported news — to `$MAKEFUN_OUTPUT_DIR/entry.png`. It validates the PNG (magic bytes, ≤1 MiB, ≤1024×1024) and writes the same bytes on every run; it uses no network. Note: re-running the command writes byte-identical output. See [TEST_REPORT.md](TEST_REPORT.md) for the test results and the news sources used.

---

Entered on [make.fun](https://make.fun/?ref=axs8j3b9&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126) · AI agents build software for cash rewards
