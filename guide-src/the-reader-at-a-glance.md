---
{
 "slug": "the-reader-at-a-glance",
 "h1": "The reader at a glance",
 "seo_title": "The Sheet Music Reader at a Glance | Music Folder",
 "description": "A tour of the Music Folder reader: the toolbar, the ⋯ menu, the Sections list, the title menu, the iPhone bottom bar and how to customize the toolbar.",
 "intent": "existing",
 "intent_note": "A user who has opened a piece and wants to know what the buttons do, where a command went, or how to rearrange the toolbar.",
 "searches": [
  "toolbar",
  "more menu",
  "ellipsis",
  "rearrange tools",
  "move tools",
  "missing button",
  "page thumbnails",
  "bottom toolbar",
  "reader buttons",
  "pdf viewer"
 ],
 "availability": [],
 "related": [
  "turn-pages",
  "change-the-page-view",
  "keep-notes-on-a-piece",
  "add-sections-to-a-book"
 ],
 "feature_link": {
  "href": "/features/sheet-music-reader",
  "text": "the Sheet Music Reader"
 },
 "documents": [
  "Songs/Song View/SongPDFView.swift",
  "Set Lists/Songs View/PDFViewInSetList.swift",
  "Planning Center/PCOPDFViewController.swift",
  "PDF Reader/PDFReaderToolbar.swift",
  "PDF Reader/ReaderToolbarCustomization.swift",
  "PDF Reader/ReaderBottomBar.swift",
  "PDF Reader/SectionReading.swift",
  "R23",
  "R28",
  "R52"
 ],
 "verified": "76048e78",
 "differs_from_4_2": null,
 "shots": [
  {
   "id": "reader-ipad",
   "kind": "screen",
   "device": "ipad",
   "orientation": "portrait",
   "state": "Ave Maria (Schubert) open in the single-piece reader on page 1, light mode, the default toolbar: Back and Sections on the left, the title with its menu chevron, then Notes, Tuner, Metronome with its tempo, Play, Annotate and ⋯ on the right. No menu or panel open.",
   "alt": "An iPad showing a page of Schubert's Ave Maria in the reader, with Back and Sections buttons at the top left, the piece's title, and the Notes, Tuner, Metronome, Play, Annotate and More buttons at the top right.",
   "caption": null,
   "reuse": "reader-ave-maria-ipad.jpg"
  },
  {
   "id": "reader-iphone",
   "kind": "screen",
   "device": "iphone",
   "orientation": "portrait",
   "state": "The same piece (Ave Maria) open on iPhone in portrait with the default layout: Back and Sections at the top left; Annotate, Play and ⋯ at the top right; the bottom bar showing Tuner, Metronome, Piano and Notes below the page. No menu open.",
   "alt": "Ave Maria open in the reader on iPhone, with Back and Sections at the top left, Annotate, Play and More at the top right, and the Tuner, Metronome, Piano and Notes buttons in the bottom bar.",
   "caption": null,
   "reuse": null
  }
 ],
 "open_questions": []
}
---
When you open a piece, it opens in the reader: the page fills the screen and the tools you use while playing sit in the toolbar above it. Music you play from a set list or a Planning Center plan opens in the same kind of reader, so the toolbar, the ⋯ menu and the settings described here work the same way there.

{shot:reader-ipad}

## The toolbar

At the top left, {sf:chevron.left} **Back** returns you to the list you came from. When you open a single piece, {sf:list.bullet} **Sections** sits next to it and opens the piece's sections. Tap a section to jump to its first page, or add one from there (see [Add sections to a book](/guide/add-sections-to-a-book)). The button is there for every PDF, even one that has no sections yet.

The tools are on the right. In an iPad-sized window the toolbar starts with:

- {sf:text.document} **Notes**: your notes on this piece. The icon is filled in when the piece has a note.
- {sf:music.note.list} **Key**: transposition and capo for a chord chart. It appears only while a chord chart is on screen.
- {sf:tuningfork} **Tuner**.
- {sf:metronome} **Metronome**, with the piece's tempo beside it.
- {sf:play.fill} **Play**: plays the piece's recording, or lets you add one if it has none.
- {sf:pencil.tip.crop.circle} **Annotate**: mark up the page with Apple Pencil or your finger.
- **⋯**: everything else (see below).

The toolbar shows only as many tools as fit. In a narrow window, the tools that don't fit move into the ⋯ menu.

## The title menu

In an iPad-sized window the piece's title appears at the top of the screen. For a piece in your library that you can edit, tap the title to open a short menu with **Edit Details**, the chord chart command and **Share**. The chord chart command is **Edit Chord Chart** for a piece with a chart; for a PDF without one it's **Convert to Chord Chart** (or **Start Chart from Lyrics** for a lyrics sheet), and otherwise **Add Chord Chart**. The same commands are always in the ⋯ menu too, and on iPhone, which has no room for a title, that's where you'll find them.

## The ⋯ menu

The ⋯ menu holds the commands that aren't on the toolbar, in the same order in every reader. Rows that don't apply to what's on screen are left out or dimmed.

- **Performance Mode**, **Face Gestures** (on devices that support them) and **Page Links**.
- Tools that don't fit on the toolbar, such as **Piano**.
- Commands for the piece: **Share**, **Edit Details**, the chord chart command, and **Add to Set List**.
- For a chord chart: **Follow Sequence**, and **Show** to switch between the chord chart and the original PDF when a piece has both.
- **Page Display & Layout**: reading options such as Vertical Scrolling, Two-Page View, Half-Page Turns, Dark Background and Crop Margins. See [Change the page view](/guide/change-the-page-view).
- **Customize Toolbar**.

## Page thumbnails

When you're reading a single piece, tap the page to show or hide a strip of page thumbnails at the bottom of the screen. (With Half-Page Turns on, tap the middle of the page, because the edges turn it.) Tap a thumbnail to go to that page. A piece with sections opens with the strip showing.

## The reader on iPhone

On iPhone the title isn't shown, and the tools are split between two bars. The top bar holds **Annotate**, **Key** (for a chord chart) and **Play** next to the ⋯ menu, and a bar at the bottom holds **Tuner**, **Metronome**, **Piano** and **Notes**, within reach of your thumb.

{shot:reader-iphone}

The bottom bar appears only when it fits in the empty space below the page without making the page smaller, which usually means holding the phone upright. In landscape, with Vertical Scrolling on and in Performance Mode, its tools join the top bar, and any that don't fit go into the ⋯ menu.

## Customize the toolbar

You can choose which tools stay on the toolbar, put them in a different order, and move the ones you rarely use into the ⋯ menu. Your arrangement applies to every piece you open.

1. Touch and hold the toolbar, or choose **⋯ › Customize Toolbar**.
   The tools start to jiggle, and an orange {sf:checkmark} takes the place of Back.
2. Drag a tool to a new position. On iPhone you can drag a tool between the top and bottom bars.
3. To move a tool into the ⋯ menu, tap {sf:minus.circle.fill} on it.
4. To add a tool, tap {sf:plus.circle.fill} at the end of the toolbar, then tap a tool in the list.
5. Tap {sf:checkmark} when you're done.

Some tools are never on the toolbar until you add them: **Performance Mode**, **Dark Background**, **Face Gestures** and **Share**, for example. Adding one puts it a tap away instead of inside the ⋯ menu. When the toolbar is full, remove a tool before you add another.

Note: In an iPad-sized window, customizing the toolbar needs iPadOS 26 or later (macOS 26 or later on a Mac). On iPhone it's always available.
