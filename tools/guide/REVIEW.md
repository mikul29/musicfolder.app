# Reviewing User Guide articles

You review guides someone else wrote. Read `tools/guide/WRITING.md` first: its rules are the standard. Do three separate passes on each guide you're given, in this order, and fix what fails directly in `guide-src/<slug>.md`. Don't touch other files, don't commit.

## Pass 1: accuracy (the most important)

Assume nothing in the article is right until the app code at commit `76048e78` shows it. For EVERY step, label, menu path, icon (`{sf:…}` must be the symbol the code uses for that control), limit, Premium gate, device or OS condition, and claim about what happens to data:
- find it in the code (`git -C /Users/matthewmikulich/Documents/Me/Music_Folder/MyBandProject grep -n … 76048e78 -- MyBandProject`, `git … show 76048e78:<path>`), and the product rule in `TEST_PLAN.md` / `CLAUDE.md` where one applies;
- check the path a user actually takes (which screen, which button, what it's called on iPhone vs iPad, what appears next);
- fix wrong text; remove a claim you can't confirm (don't replace one guess with another); add a precise question to `open_questions` for anything only the owner or a device can settle.
Watch especially for: invented button names, steps in the wrong order, "tap" for page turns where the app uses swipes, features attributed to the wrong screen, things that are Premium described as free or the reverse, sharing behaviour from 4.2 described as 4.3, version history implied for all music (Previous Version is shared pieces only), annotations/notes/recordings implied to be shared.

## Pass 2: writing style

Read each guide aloud in your head. Fix, by rewriting the passage:
1. em dashes (none allowed);
2. fragments and short dramatic sentences;
3. one-sentence paragraphs used for effect, or several in a row;
4. an introduction that repeats the formula of other guides ("This guide shows…" in every guide) — vary or cut it; start with the steps when they can start right away;
5. formulaic transitions;
6. adjectives, intensifiers, marketing language, the banned phrases in WRITING.md;
7. awkward keyword repetition;
8. a closing summary or encouragement;
9. too many bullets, bold or headings; bold only for interface labels and real distinctions;
10. anything that sounds unnatural read aloud.
Don't make it artificially casual. Correct grammar, clear instructions and precise terminology still matter.

## Pass 3: SEO and links

- `seo_title` (≤ 60 chars, ends " | Music Folder") and `description` (120–158 chars) are accurate, specific, written in plain English, and use the words a musician would search for this task; unique across all guides (check `guide-src/*.md`).
- The first paragraph says what the guide helps you do in searchable words, without stuffing.
- H2/H3 are descriptive and in order.
- `related` (2–4) are the guides a reader most likely needs next; links in the body point to real slugs.
- The guide explains HOW; it doesn't restate the matching marketing page's pitch (the pages are listed in WRITING.md §4).

## Report

For each guide: what you changed in each pass (one line each, or "no change"), remaining `open_questions`, and any shot whose `state` no longer matches the text.
