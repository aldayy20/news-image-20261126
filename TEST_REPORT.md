# TEST_REPORT — news-image-20261126

Entry: a program that writes one image summing up the world news of
Thursday 26 November 2026. Bounty: https://make.fun/bounty/news-image-20261126
($100 USDC on Solana; 50 places; entries close 2026-11-28 07:00 WIB,
i.e. 2026-11-28 00:00 UTC).

## Repo files (this directory is the repo root — push exactly these 6 files)

| File | Bytes | Role |
| --- | --- | --- |
| `main.ts` | 2,306 | Entrypoint (Node 22, stdlib only). Copies `entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png` after validating PNG magic + IHDR, ≤1 MiB, ≤1024×1024. |
| `entry.png` | 153,935 | The image, 1024×1024 PNG, rendered by `render.py`. |
| `render.py` | 7,639 | Generator (Pillow + DejaVu fonts, local use only; the grader never runs it). |
| `README.md` | 2,915 | make.fun badges, bounty link, run instructions, referral `?ref=axs8j3b9`. |
| `LICENSE` | 1,061 | MIT, Copyright (c) 2026 Aldi. |
| `TEST_REPORT.md` | — | This file. |

Total repo snapshot: ~167 KB (6 files). No size cap on the whole tree is stated
for this bounty in its requirements; the only file cap that matters is the
image's own: ≤1 MiB, ≤1024×1024. The downloaded kit lives OUTSIDE this repo, in
`~/workspace/news-image-20261126-kit/` (kit.tar.gz + extracted kit) — do not
push it. `.makefun/owner.json` is NOT included: the repo owner will be
`aldayy20`, the account's GitHub login, so the claim file is unnecessary.

## Kit

Downloaded from https://make.fun/c/news-image-20261126/kit
(8,569,797 bytes, gzip) and extracted to
`~/workspace/news-image-20261126-kit/news-image-20261126-kit/`.
RULES.txt confirms the entry rules: one PNG/JPEG named `entry.png`,
≤1 MiB, ≤1024×1024, no network at run time; the image must name the day
it sums up (Thursday 26 November 2026). The kit offers no local grader
for this bounty; the server grades every entry.

## Tests run (26 Nov 2026, ~01:30 UTC / 08:30 WIB)

1. `python3 render.py` → `entry.png`, 1024×1024 RGB PNG, 153,935 bytes.
   Re-ran it: identical sha256 (`a4624988dd7f7f9d5ad69fb71c20875cdd84c1da13aeb3ca9067ff34bcbaa081`) — deterministic.
2. `MAKEFUN_OUTPUT_DIR=out1 node main.ts` and `...=out2 node main.ts`
   (node v24.22.1 locally; grader uses Node 22) → both exit 0, both write
   `entry.png` byte-identical to the repo image (sha256 matches in all
   three places) — deterministic across runs, as the bounty requires.
3. Gate check: PNG magic bytes OK (`89 50 4e 47`, IHDR present);
   153,935 ≤ 1,048,576 bytes; 1024×1024 ≤ 1024×1024. PASS.
4. Visual check: rendered image read back and inspected. All seven
   panels fit inside their boxes with no clipped or overlapping text
   (three layout iterations fixed: the Thanksgiving body wrapping to 4
   lines, the Flipkart body wrapping to 4 lines, the chess body wrapping
   to 4 lines, and the sport-strip headline overflowing the panel width
   — every block also verified programmatically against its panel bounds
   with a wrap-measurement script, all ending inside their bounds).
   At 300 px across, the date, "15% / TAIWAN KEEPS IT", "TAIPEI HOLDS
   THE LINE", "PARADE PUSHED TO SATURDAY" and the panel headlines stay
   legible.
5. Docker grader simulation: NOT run — Docker is not installed on this
   machine. Mitigation: `main.ts` uses only Node stdlib (`node:fs`,
   `node:path`, `node:url`), makes no network call, reads only
   `entry.png` beside itself, and was verified by two plain `node`
   runs as the grader would invoke it.

## News covered (all first reported on 26 Nov 2026)

1. **Taipei holds the line** — Taiwan says it is confident of keeping
   its agreed 15% US tariff rate, a day after Trump fired a new salvo
   at 14 trading partners; China faces 20%, the EU, Japan and South
   Korea are capped at 15%. Reuters reports the Taiwanese government
   made the statement "on Thursday". Sources: Reuters, Fox Business.
2. **Parade pushed to Saturday** — Macy's Thanksgiving Day Parade,
   scheduled for Thanksgiving Day (Thursday 26 Nov), moves to Saturday
   as powerful winds bear down on New York; storms threaten holiday
   travel for 250m Americans. Sources: AP.
3. **F-15EX fighters at Kadena** — the US Air Force unveils its newest
   F-15EX fighters at Kadena Air Base in Okinawa. Source: SimpleLife
   daily news digest, 26 Nov 2026.
4. **Flipkart chief to step down** — Flipkart CEO Kalyan Krishnamurthy
   will step down in December. Source: selfstudys school-assembly
   headlines, 26 Nov 2026.
5. **293,600 jobs in Saudi** — Kenya secures 293,600 job
   opportunities in Saudi Arabia for its workers. Source: C54 News
   global live feed, Thu 26 Nov 2026.
6. **Game 3 in Geneva** — Gukesh and Sindarov, both 20, play Game 3
   of the World Chess Championship on Thursday 26 Nov (FIDE schedule:
   Round 3, 3:00 pm CET), the youngest world title match in 140 years,
   $2.5m prize fund. Sources: FIDE regulations, ChessBase India.
7. **Sport** — Champions League Wednesday-night results, reported on
   Thursday morning in Asia (matches ended ~04:45 WIB on 26 Nov):
   Liverpool 3-0 Club Brugge (Isak brace), PSG 2-2 Roma (holders'
   perfect record ends), Lille 2-1 Bayern, Barcelona 4-1 Sabah,
   Manchester United 2-2 Sporting, Inter 2-0 Stuttgart,
   Atlético 2-0 Viking. Source: UEFA.
8. Footer ticker: India marks Constitution Day (26 Nov); Ghana unveils
   Heritage Series banknotes; São Tomé and Príncipe reappoints
   Américo Ramos as prime minister; ECOWAS approves a roadmap for its
   regional security force by end-2027. Sources: C54 News, 26 Nov.

Accuracy notes: this was a thin news day — the week's biggest stories
(Trump's tariff salvo, the Rosstat leak of ~490,000 Russian war dead,
ESA Hera's Dimorphos images, the Cairo tanker fire, Andy Taylor's
death) were all first reported on 24–25 Nov and were deliberately NOT
reused as 26 Nov news. Every item above is tied to 26 Nov by its
reporting date or by the event falling on 26 Nov (Thanksgiving Day,
Game 3, the Thursday Taiwan statement, the Wednesday-night results
landing in Asia on Thursday morning). The Champions League results are
the one item whose matches were played late on 25 Nov CET; they are
included as the sport strip because they were first reported in Asia
on the morning of 26 Nov and were not used in the 25 Nov entry.

## Still needed (parent / user)

- Create public GitHub repo `aldayy20/news-image-20261126` (after the
  2026-11-26 00:00 UTC opening), push exactly the 6 files above, set
  About: website https://make.fun/bounty/news-image-20261126, topics
  `makefun, ai-agents, bounties, growth`, description naming make.fun.
- Add `.makefun/owner.json` naming the agent wallet
  `EuY16n7eBkcKQ6Q8n9QY7Rbi4xyeTfQ1ThaYdcm9KoND` if the first check
  refuses on `repo_owner` (same fix as the 22 Nov entry), and make
  thinking_revised edits directly in the git clone, not a staging dir.
- Bundle the transcripts of the sessions that built this entry
  (kit CLI `bundle`, from inside the downloaded kit) and submit via
  the kit CLI before 2026-11-28 07:00 WIB, signing with the agent
  keypair as approved for the 22/23/24/25 Nov entries. Do NOT resubmit
  any accepted entry.
- Note: no result date is published for this bounty yet; the 25 Nov
  entry's result is due 11 Dec 2026, so a similar lag is likely.
