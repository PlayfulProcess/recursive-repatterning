# Plan: the sleep practice, and the first adaptive test

Oct 8 2026. Draft for her review. Psychoeducation, not therapy or treatment.

Her words: "One thing that I would like your help on is to sleep better ... Maybe a CBT-I module in
recursive repatterning that can also be a grammar that can serve as context for some sort of
practice? journaling etc the whole flow and I will be subject #1?"

What exists now: the grammar `schools/sleep-gently/grammar.json` ("Sleep, gently (CBT-I
informed)"), 15 items in five groups, in the Skills-Based branch beside DBT. Nothing was built on
the platform.

---

## 1. The daily loop

```
  evening                     night                    morning                 once a week
  ------------------------    ---------------------    ---------------------   ------------------------
  worry time (early)          bed when sleepy          same wake time          four numbers
  buffer zone (last hour)     awake? clock away,       light                   one decision at most
  one line:                   get up, dim, calm        diary, 2 minutes,       (only with a clinician's
  "Tonight I accept ___.                               in her private          yes, and only if a
   Tomorrow I keep ___."                               Journal                 sleep window is in use)
```

Grammar items, in order: `evening-practice` → `three-am` → `morning-diary` → `weekly-review`.

## 2. In the daily handoff

The daily handoff (the `recursive-eco/docs/future_plan/HANDOFF-*.md` pattern, and the paste-ready
prompt she asks for at the end of each day) gets two fixed lines. Nothing else in the handoff changes.

**Opening line of each morning's prompt** (before the day's practice):

> Before anything else: open "Sleep, gently", item "Morning: the sleep diary". Copy the blank form
> into your private Journal and fill it in. Two minutes, guesses are fine. On Sundays (or her chosen review day), also open
> "Weekly: sleep efficiency and the window" and work out the four numbers.

**Closing line of each evening's session** (the last thing the session says, after writing the handoff):

> The session is closing, and the buffer zone can start here. Open "Evening: wind down, one line"
> and write: Tonight I accept ___. Tomorrow I keep ___.

Asking for the handoff before the last hour, not inside it, keeps the screen out of the buffer zone.

The new session does not comment on her diary, ask for its numbers, or praise or worry about them.
It only opens the item. She decides what to share.

## 3. Privacy

- The repo holds the method and the blank form only. **Her diary never goes in any repo**: not
  here, not in `recursive-eco/docs/`, not in a HANDOFF file, not in memory files, not in a commit.
- The diary goes in her **private Journal** on recursive.eco as text: Personal notes on the
  "Morning: the sleep diary" item (Private, saved to Journal), or a private Journal entry.
- Text only. No photos of paper diaries and no attachments: the Oct 8 promises audit (C, finding P1)
  found that Journal chat attachments are stored on the public file host today.
- Personal notes hold up to 20,000 characters per item. A filled form is roughly 600 (the blank one is
  521), so one note holds about a month. Start a new Journal entry each week, or each month.

## 4. The measure, and the adaptive test

**Four numbers a week**, from the diary (formulas in the `weekly-review` item):

| Number | What it says | Better is |
|---|---|---|
| Sleep efficiency | share of time in bed spent asleep | higher |
| Sleep onset | average minutes to fall asleep | lower |
| Wake after sleep onset | average minutes awake in the night | lower |
| Weekly 1 to 5 | "how rested did this week feel?" | higher |

**The adaptive test.** A recursive.eco practice is adaptive if people return to it and their own
measure improves. For this one practice, with one person:

- *Return*: days a week with a diary filled in. Five or more counts as returning.
- *Improves*: her weekly numbers against her own first two weeks (the baseline).

She sets the thresholds before she starts, in her Journal, so the result cannot be bent later. A
suggestion she can change: "improved" means sleep efficiency up 5 points or more, or the weekly 1 to 5
up by one, held for two weeks in a row.

**What this cannot show.** One person, no comparison, and people usually start a sleep practice
when sleep is at its worst, so some improvement would come anyway. Seasons, travel, illness and news
move sleep too. A good result says "worth continuing for her", not "CBT-I works" (that is already
known) and not "the platform works". If many people return and improve, that would start to say
something about the practice and its form.

## 5. Weeks, for subject #1

| Weeks | What she does |
|---|---|
| 1-2 | Diary only, plus one fixed wake time. Read the grammar slowly. This is the baseline. |
| 3-4 | Add stimulus control, the buffer zone, worry time, the evening line. |
| 5+ | Only if sleep efficiency is under 85% **and** a clinician has said yes: sleep compression, 15 to 30 minutes a week, never under six hours in bed. |
| 8 | Look back with her own thresholds. Keep, change, or stop. |

The 3am item, the body scan and checking the facts are there from day one, whenever she needs them.

## 6. Safety for subject #1

- The sleep window waits for a clinician's yes. The cautions in the `sleep-window` item apply:
  bipolar disorder, seizures, psychosis, sleep apnoea or another sleep disorder, pregnancy, driving or
  safety-critical work, strong daytime sleepiness, or already sleeping under about five and a half hours.
- 2027 is her survival year. If mood is low, or nights bring thoughts of harm, sleep work waits and
  support comes first: her clinician, a crisis line, emergency services.
- If tracking makes nights more anxious, pause the diary for a week. Rest is the aim, not the score.
- Any sleep medicine stays as prescribed; changes go through the prescriber.

## 7. Findings, not a build queue

- The grammar is in this repo only. Putting it on recursive.eco as **Private** needs her word.
  Not checked: whether the channel import skips grammars with `metadata.status: "draft"`.
- No new platform feature is needed for the loop: items, Personal notes, the Journal and the
  handoff already do it. A computed weekly summary would be a platform feature; it is not proposed.
- If she wants a second evening practice later, DBT items already linked from the grammar
  (check the facts, opposite action, radical acceptance, PLEASE) are the first place to look.

## Sources

Every citation is in the grammar's Research note sections, each checked on Oct 8 2026 against
Crossref or the source page. The main ones: AASM 2021 guideline (https://doi.org/10.5664/jcsm.8986),
ACP 2016 guideline (https://doi.org/10.7326/M15-2175), the Consensus Sleep Diary
(https://doi.org/10.5665/sleep.1642), the Australian joint position statement on insomnia, 2026
(https://doi.org/10.1093/sleepadvances/zpag086), Kaplan & Harvey 2013 on bipolar disorder
(https://doi.org/10.1176/appi.ajp.2013.12050708), Kyle et al. 2014 on daytime sleepiness during sleep
restriction (https://doi.org/10.5665/sleep.3386), and the VA CBT-i Coach
(https://mobile.va.gov/app/cbt-i-coach).
