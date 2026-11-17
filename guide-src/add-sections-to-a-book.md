---
{
 "slug": "add-sections-to-a-book",
 "h1": "Add sections to a book",
 "seo_title": "Organize Multiple Songs in One PDF | Music Folder",
 "description": "Mark where each hymn, tune or movement starts in a PDF songbook, give each section its own key and tempo, and find your old bookmarks.",
 "intent": "existing",
 "intent_note": "Musicians with hymnals, fake books, method books or multi-movement scores in one PDF, including 4.2 upgraders looking for bookmarks.",
 "searches": [
  "bookmarks",
  "bookmark",
  "bookmarks menu",
  "where are my bookmarks",
  "hymnal",
  "fake book",
  "real book",
  "songbook",
  "split pdf",
  "split pdf into songs",
  "movements",
  "table of contents",
  "outline",
  "book",
  "collection",
  "find pieces"
 ],
 "availability": [
  {
   "kind": "premium",
   "text": "Without Music Folder Premium, your library can hold up to 5 sections."
  },
  {
   "kind": "requires",
   "text": "Find Pieces Automatically requires Apple Intelligence and iOS 26 or iPadOS 26 or later."
  }
 ],
 "related": [
  "import-music",
  "create-and-edit-a-set-list",
  "set-the-song-order",
  "use-the-metronome"
 ],
 "feature_link": {
  "href": "/features/sheet-music-organizer",
  "text": "the Sheet Music Organizer"
 },
 "documents": [
  "Shared UI/AddBookmarksViewController.swift",
  "Shared UI/ReviewBookmarksViewController.swift",
  "Shared UI/EditBookmarkViewController.swift",
  "Shared UI/SectionDetailsView.swift",
  "Services/BookmarkSuggestions.swift",
  "Services/AddMusicFormLayout.swift",
  "Services/FindPiecesCard.swift",
  "Services/PieceFinder.swift",
  "Sharing/BookDivisionAnalyzer.swift",
  "Services/BookmarkRemovalConfirmation.swift",
  "Services/SectionRules.swift",
  "Songs/Song View/SongPDFView.swift (BookmarkDrawerController)",
  "PDF Reader/SectionTempoFollower.swift",
  "Premium/PremiumGate.swift (FreeTier.sectionAllowance)",
  "R61",
  "R62",
  "R63",
  "R64",
  "R65",
  "R66",
  "R67",
  "R68"
 ],
 "verified": "76048e78",
 "differs_from_4_2": null,
 "shots": [
  {
   "id": "add-sections-grid",
   "kind": "screen",
   "device": "ipad",
   "orientation": "portrait",
   "state": "Add Sections for Mozart's Quartet in D, K. 155 (8 pages), pages 1, 4 and 7 marked.",
   "alt": "The Add Sections grid for an eight-page Mozart quartet, with pages 1, 4 and 7 marked as the starts of three movements, Find Pieces Automatically above the pages, and Review 3 Sections at the top.",
   "caption": "Tap the page where each piece starts.",
   "reuse": null
  }
 ],
 "open_questions": []
}
---
Sections mark where each piece or movement starts and ends inside a larger PDF, such as a hymn in a hymnal, a tune in a fake book or a movement of a sonata. Each section can have its own key, tempo, time signature, duration and composer, and you can put a section in a set list on its own.

## Bookmarks are now sections

Sections were called bookmarks before Music Folder 4.2. They were renamed because they now stand for the individual pieces or movements inside a PDF, not just saved page positions. Bookmarks you made in an earlier version are your sections now. There's no separate Bookmarks menu: in the reader, tap {sf:list.bullet} **Sections** next to the back button to see them and jump to one.

Sections aren't the verses, choruses and bridges of a chord chart (V1, C1, B) or a chart's song order, which belong to the chart itself. See [Set the song order](/guide/set-the-song-order).

## When the app suggests sections

Many publishers' PDFs carry their own table of contents, the outline a PDF viewer shows in its sidebar. When you import such a PDF, or open **Edit Details** for one without sections, the app reads that outline. If it lists at least two pieces on different pages, the **Sections** part of the form shows a card such as "12 sections found." Nothing has been created yet:

1. Tap **Review**. **Review Sections** lists each entry with its pages. Contents pages, indexes and part headings start unchecked.
2. Keep checked only the entries that are pieces. Tap a row to change its title or pages.
3. Tap **Use 12 Sections**, then tap the checkmark on the form to save.

Music you scan with the document scanner can show "4 possible pieces found" instead, read from the titles at the top of the scanned pages.

Until a piece has sections, the reader's {sf:list.bullet} **Sections** list also shows the PDF's own outline under **Table of Contents**. Those entries only take you to a page: they have no details and can't go into a set list. To turn one into a section, swipe left on it, tap **Edit** and save it. Once the piece has sections, the list shows only them.

## Mark sections by hand

{shot:add-sections-grid}

1. Touch and hold the piece in your library and choose **Edit Details**, or start from the Add Music form while importing.
2. Under **Sections**, tap **Add Sections**. The row appears for music with two or more pages.
3. Tap the page where each piece starts. Marks are numbered in page order; tap a marked page again to remove its mark.
4. Tap **Review Sections** (for example, **Review 12 Sections**).
5. Tap each section to name it in **Edit Section**, then tap the checkmark. Until you rename them, sections are called Untitled 1, Untitled 2 and so on.
6. Tap **Use 12 Sections**, then the checkmark on the form.

Each section ends one page before the next one starts, so you only need to mark the starts.

On iPad: in a wide window, the list of sections and the section you're editing sit side by side, and your edits apply as you make them.

## Find pieces automatically

With Apple Intelligence turned on, the Add Sections screen has a **Find Pieces Automatically** card above the pages. Tap it and the app looks for the pieces using the PDF's outline, its contents page and the titles on its pages. When it finishes, **Review Sections** opens with what it found, plus any pages you'd already marked. You can tap **Cancel** while it works and **Resume** to start again; if it finds nothing, mark the pages by hand.

Check the titles and start pages before you tap **Use**, especially in books whose printed page numbers don't match the PDF's pages.

## Set a section's details

**Edit Section** has the section's title, a strip of the PDF's pages (tap one to move the start) and these settings:

- **Starts on page**.
- **Follow Next Section**: on by default, so the section ends just before the next one starts. Turn it off to set **Ends on page** yourself, for example when blank pages separate the pieces.
- **Details**: **Composer**, **Tempo**, **Time Signature**, **Key** and **Duration**. The composer is the book's ("From document") until you type another. Key, tempo, time signature and duration are never taken from the book, so leave them empty if they don't apply.

A section played from a set list uses its own tempo and time signature. In the reader, the metronome changes to a section's tempo when you reach its pages; after you change the tempo yourself, choose **⋯ › Follow Section Tempos** to follow them again. See [Use the metronome](/guide/use-the-metronome).

## Use sections in the reader

Tap {sf:list.bullet} **Sections** and tap a section to jump to its first page. The section you jumped to has a checkmark while you're on its pages. Nothing stops you at the end of a section.

To add a section while you read, go to its first page, open **Sections** and tap **Add Section Here** (or {sf:plus}). To rename a section or change its pages, swipe left on it and tap **Edit**. Tap **Delete** to remove it.

## Change or remove sections later

1. Touch and hold the piece and choose **Edit Details**.
2. Under **Sections**, tap a section, **Edit Sections**, or **All 12 Sections** in a long list.
3. Tap a section to edit it, swipe left and tap **Remove** to remove it, or tap **Add Section**.
4. Tap **Done**, then the checkmark on the form.

If a section you remove is in a set list, the app names the set list first and removes only that entry; everything else in the set list stays in order. **Remove All Sections** turns the book back into one regular piece. Adding or removing sections never changes the PDF; to reorder or remove pages, use [Organize Pages](/guide/organize-rotate-and-crop-pages).

## Put a section in a set list

When you add music to a set list, a piece with sections shows how many it has. Open its sections and choose the ones you want instead of the whole document; each one plays only its own pages. See [Create and edit a set list](/guide/create-and-edit-a-set-list).

## Display as Book

**Display as Book**, in the form's **Details**, shows a piece as a book in your library lists and in the **Books** filter. It changes only how the piece looks; sections work the same either way. **Review Sections** offers the same choice, **Show as Book**, when you review six or more titled sections.

## The free allowance

The free version includes 5 sections across your library. If tapping **Use** or **Add Section Here** would take you past 5, the Premium offer appears and your unsaved work stays open behind it. Editing, renaming and removing sections is always allowed, **Display as Book** is free, and sections in shared folders and set lists don't count. See [Free and Premium](/guide/free-and-premium).
