# Writing a Music Folder User Guide article

This is the brief every guide writer and reviewer works from. Read all of it before writing.

The User Guide lives at `https://musicfolder.app/guide` (hub) and `https://musicfolder.app/guide/<slug>` (one page per guide). Source files are `guide-src/<slug>.md` in this repo; `tools/guide/build.py` turns them into static HTML. The inventory of all 48 guides (slugs, chapters, titles, what each covers) is `tools/guide/inventory.json`. Slugs and titles there are fixed: don't rename, merge or drop guides.

## 1. Accuracy comes first

Every step, label, menu path, limit and requirement must match the shipped app. **Write against Music Folder 4.3**, the commit `76048e78` on branch `release/4.3` of the iOS repo at `/Users/matthewmikulich/Documents/Me/Music_Folder/MyBandProject`.

- Read that repo's `CLAUDE.md` first: it maps every feature to its files and records the owner's product rules. `TEST_PLAN.md` holds the numbered rules (R1–R145).
- Verify UI text against the code, never from memory. Search the commit, not the working tree (other sessions may switch branches):
  `git -C /Users/matthewmikulich/Documents/Me/Music_Folder/MyBandProject grep -n '"Add Sections"' 76048e78 -- MyBandProject`
  `git -C … show 76048e78:"MyBandProject/Shared UI/AddSongFormViewController.swift"`
- Check: exact control names (titles and accessibility labels), menu paths, which device shows what (iPhone vs iPad vs Mac; layout is decided by space, see CLAUDE.md "Landscape everywhere"), Premium gates (`PremiumGate`, `FreeTier`, `CollaborationAccess`, the paywall's `compareRow` list in `Premium/PremiumPaywallView.swift`), iOS version gates (`#available`), Apple Intelligence requirements, what happens to data.
- 4.3's minimum system is iOS 17 / iPadOS 17 (macOS on Apple silicon runs the iPad app). Don't put version numbers in articles unless a feature needs a newer OS (say "iOS 18 or later" only where the code gates on it).
- If something differs from 4.2 (sharing especially), set `"differs_from_4_2"` in the front matter and say what.
- **Never invent.** If you can't confirm a label or a step from the code, don't write a guess: leave the step out or describe it generically, and add the question to `"open_questions"`. A short accurate guide beats a complete-looking wrong one.
- Read-only: don't edit the app repo, switch its branch, build, run tests or touch simulators.

## 2. Terminology (owner rules)

- The library and sheet music in general: **music** ("Add Music", "All Music"). Counting works: **pieces** ("15 pieces"). **Song** only for real songs (chord charts, lyrics, Planning Center songs).
- **Folders** (the code says Group; the UI says Folder). **Set lists** (two words in text; "Set List" in UI labels).
- **Sections**, not bookmarks. Bookmarks were renamed Sections in 4.2. A section is a page range inside a PDF for one piece or movement (a hymn in a hymnal, a tune in a fake book, a movement of a sonata); it can have its own key, tempo, time signature, duration and composer, and can go into a set list on its own. Chord-chart sections (verse, chorus, bridge; V1, C1) and the chart's song order are a different thing. Where it helps returning users, say "sections (called bookmarks before Music Folder 4.2)" once.
- American English. Plain words. Apple's names for Apple things (Apple Pencil, iCloud, AirDrop, Files app, Settings).
- Page turns are swipe, scroll, keyboard and Bluetooth pedal. Tapping turns pages only where the code says so (Performance Mode tap zones, Half-Page Turns' edge zones). Check before writing "tap".
- Markings, notes and recordings are personal: never shared with collaborators. Sharing (collaboration) is Premium for everyone taking part. A one-time copy is free.

## 3. Writing style (mandatory)

Write like an experienced technical writer who uses the app and is explaining it to another musician. Apple's user guides are the model.

- **No em dashes (—)** anywhere. Use commas, periods, parentheses or two sentences. En dashes only in ranges (3–7).
- Natural paragraph lengths with connected sentences. No strings of one-sentence paragraphs, no short dramatic sentences for emphasis, no rhetorical questions.
- Contractions where natural. No superlatives, intensifiers or promotional claims. Don't repeat "Music Folder" in every sentence; "the app" or nothing is usually better.
- Don't open every article the same way, and don't end with a summary or encouragement. Stop when the task is done.
- Banned (and anything like them): "Whether you're a beginner or…", "take … to the next level", "unlock", "seamless(ly)", "effortless(ly)", "designed with musicians in mind", "more than just", "it's not just X, it's Y", "from rehearsals to performances", "everything you need", "all in one place", "say goodbye to", "with just a few taps", "the result?", "here's where X comes in", "X, reimagined", "X, made simple", "powerful yet intuitive", "game-changing", "streamline", "dive in", "let's", "simply".
- Numbered steps for procedures, one action per step. Paragraphs for explanation. Bullets only when they make a list easier to scan.
- Bold only for interface labels (**Add Sections**), important distinctions and rare warnings. Don't bold ordinary phrases.
- Headings describe the task ("Add a section by hand"), never slogans.
- If the steps can start right away, start them. No filler to reach a length. Most guides land at 250–800 words; a simple task may be 150, a complex one longer.

Good: "You can organize your music into folders for different ensembles, performances, or collections. A piece can appear in more than one folder without creating another copy."
Bad: "Take control of your music library with powerful organizational tools."

## 4. SEO (natural, never stuffed)

For every guide decide who searches for it: an existing user looking for a feature, a musician with a general problem who doesn't know the app, or someone troubleshooting. Use the words musicians use ("page turner pedal", "hymnal PDF", "transpose chords", "set list") in the SEO title, description and first paragraph where they fit naturally. Don't add "iPad" or "sheet music" to every title; don't repeat keywords; no invented long-tail variants.

- `seo_title`: unique, ≤ 60 characters, ends with ` | Music Folder`. Example: H1 "Turn pages hands-free" → "Turn Sheet Music Pages Hands-Free on iPad | Music Folder".
- `description`: unique, 120–158 characters, plain English, says what the page explains. Example: "Learn how to import sheet music PDFs into Music Folder from Files, Photos, AirDrop, or a document scanner."
- `h1`: the inventory title, unchanged.
- First paragraph: one or two sentences saying what the guide helps you do, in searchable words.
- The marketing pages explain WHY; guides explain HOW. Don't restate a feature page's pitch. Link to it once where it genuinely helps (`feature_link`).

Marketing pages you may link: `/features/sheet-music-organizer`, `/features/sheet-music-reader`, `/features/set-lists`, `/features/page-turner`, `/features/annotation`, `/features/chord-charts`, `/features/sharing`, `/features/toolkit`, `/features/free-sheet-music`, `/planning-center`, `/for/bands`, `/for/worship-teams`, `/for/orchestras-choirs`, `/for/students`, `/pricing`, `/support`, `/contact`, `/privacy`.

## 5. File format

`guide-src/<slug>.md`: a JSON front matter block between two `---` lines, then the body.

```
---
{
 "slug": "add-sections-to-a-book",
 "h1": "Add sections to a book",
 "seo_title": "Split a PDF Songbook Into Sections | Music Folder",
 "description": "…",
 "intent": "existing | general | troubleshooting",
 "intent_note": "One line: who searches for this and what they want.",
 "searches": ["bookmarks", "hymnal", "fake book", "split pdf into songs"],
 "availability": [{"kind": "premium", "text": "Free includes 5 sections; Premium has no limit."}],
 "related": ["import-music", "create-and-edit-a-set-list", "set-the-song-order"],
 "feature_link": {"href": "/features/sheet-music-organizer", "text": "the Sheet Music Organizer"},
 "documents": ["Shared UI/AddBookmarksViewController.swift", "Services/SectionRules.swift", "R61", "R63"],
 "verified": "76048e78",
 "differs_from_4_2": null,
 "shots": [ … see §7 … ],
 "open_questions": []
}
---
Body…
```

- `searches`: words people might type into the guide's own search box that aren't already in the title (synonyms, old names, everyday terms). Never shown on the page.
- `availability`: zero or more notices shown under the H1. `kind` is one of `premium`, `device` (iPad and Mac only, needs a camera…), `requires` (Apple Intelligence, iOS 18, an iCloud account, Planning Center Services…), `version` (needs Music Folder 4.3 for everyone…). One short sentence each, no notice when nothing applies.
- `related`: 2–4 slugs from the inventory that a reader of this guide is likely to need next. Genuinely related only.
- `documents`: app files / screens / rule numbers the guide describes, so a future release can find affected guides.

## 6. Body syntax (a small Markdown subset; nothing else renders)

- `## Heading` and `### Heading` (the H1 comes from the front matter; never write `#`).
- Paragraphs separated by a blank line.
- `1.` numbered steps, `-` bullets. One level only, no nesting. A step may continue on the next line indented by three spaces.
- `**Label**` for bold. `[text](/guide/slug)` or `[text](/features/…)` for links (site-relative only; every guide link must be a real slug).
- Inline interface icon: `{sf:<SF Symbol name>}` with the exact symbol the code uses for that control (e.g. `{sf:list.bullet}` for the reader's Sections button), followed by its bold name: `tap {sf:list.bullet} **Sections**`. Find the symbol in the code (`UIImage(systemName:`, `Image(systemName:`). Use icons only for buttons that show an icon; menu items get bold text only.
- Menu paths: `**⋯ › Page Display & Layout › Dark Background**`, with `›` between levels.
- Callouts: a paragraph that starts with `Note:`, `Tip:`, `Important:`, `On iPhone:`, `On iPad:` or `On Mac:` becomes a styled note. Use them only when they change what the reader does.
- Image or clip: `{shot:<id>}` on its own line, where `<id>` is defined in `shots`.

## 7. Screenshots and clips

Default to none: an inline icon plus a bold label is usually enough. Use the kinds the inventory plan assigns (see `marketing/help-guides-plan.md` in the iOS repo):
- `crop`: just the control (a menu, popover, sheet or settings screen) with a little context, when it's hard to find or describe.
- `screen`: the whole iPad screen, only for orientation pages and the plan's Screen entries.
- `clip`: a silent, looping clip under 6 seconds, only where the plan assigns one.

Each entry in `shots`:
```
{"id": "add-sections-grid", "kind": "screen|crop|clip", "device": "ipad|iphone",
 "orientation": "portrait|landscape", "state": "Exactly what must be on screen: which piece (from the demo library: hymnal, Bach, etc.), which menu open, which item selected.",
 "alt": "Descriptive alt text that would make sense read aloud.", "caption": "Optional short caption, or null",
 "reuse": "an existing assets/ filename that shows EXACTLY this state, or null"}
```
Existing real captures in `assets/` (4.2 builds, same UI unless the feature changed) you may propose to reuse; open them to check they match the step: reader-layout-menu-ipad, reader-crop-ipad, reader-half-page-ipad, reader-half-split-ipad, reader-page-links-ipad, reader-perform-ipad, reader-sections-ipad, reader-sections-hymn-ipad, reader-two-page-ipad, reader-toolbar-edit, annotate-ipad, annotate-layers-ipad, annotate-shapes-ipad, chart-editor-ipad, chart-convert-ipad, chart-key-ipad, chart-sequence, organizer-book-ipad, organizer-import-ipad, organizer-pages-ipad, folders-band-ipad, setlist-*-ipad, practice-ipad, tempo-key-iphone, recording-iphone, tool-metronome, tool-tuner-reader, tool-tone, tool-piano, tool-tools-tab, planning-center-iphone, pco-connect-iphone, share-sheet-iphone, home-ipad.webp (all `.jpg` unless noted). Shots are captured from the app after the text is final, so describe the state precisely.

## 8. When you finish

Re-read each guide aloud in your head against §3, check every label against the code once more, and confirm each `related` slug exists in the inventory. Your final report: one line per guide (slug, word count, shots, anything that differs from 4.2), then every open question with the file it concerns.
