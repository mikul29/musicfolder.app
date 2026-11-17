---
{
 "slug": "create-a-chord-chart",
 "h1": "Create a chord chart",
 "seo_title": "Write a Chord Chart in ChordPro | Music Folder",
 "description": "Write a chord chart in Music Folder: type chords in brackets or above the lyrics, preview the pages as you go, and import ChordPro and text chart files.",
 "intent": "general",
 "intent_note": "Guitarists, worship and band musicians looking for a way to write chords over lyrics on iPad or iPhone, plus users who want to bring in .cho or .txt chord files.",
 "searches": [
  "chordpro",
  "chords over lyrics",
  "lead sheet",
  "lyrics with chords",
  "new chart",
  "cho file",
  "chordpro file",
  "import chords",
  "song chart",
  "write chords"
 ],
 "availability": [
  {
   "kind": "premium",
   "text": "Each chord chart counts as one piece toward Free's 15-piece limit; Premium has no limit."
  }
 ],
 "related": [
  "transpose-capo-and-numbers",
  "set-the-song-order",
  "format-a-chord-chart",
  "turn-a-pdf-into-a-chord-chart"
 ],
 "feature_link": {
  "href": "/features/chord-charts",
  "text": "chord charts in Music Folder"
 },
 "documents": [
  "Chords/ChartEditorViewController.swift",
  "Chords/ChartImport.swift",
  "Chords/ChordsOverLyricsConverter.swift",
  "Shared UI/SongListViewController.swift (addToLibrarySections, isImportableDropItem)",
  "PDF Reader/PDFReaderToolbar.swift (SongEditActions)",
  "App/SceneDelegate.swift (classifyIncoming)",
  "Info.plist (CFBundleDocumentTypes)",
  "Chords/CHORD_SPEC.md",
  "R24",
  "R26"
 ],
 "verified": "76048e78",
 "differs_from_4_2": null,
 "shots": [
  {
   "id": "chart-editor",
   "kind": "screen",
   "device": "ipad",
   "orientation": "landscape",
   "state": "Amazing Grace (John Newton) open in the chord chart editor (title Edit Chart): the Title, Artist, Original Key: G, 72 and 3/4 fields above the ChordPro text on the left, with chords in orange brackets; the live preview on the right with \"Shown as Key: G\" above it; the [ ], Insert and Symbols buttons along the bottom.",
   "alt": "The chord chart editor on iPad in landscape, with Amazing Grace typed in ChordPro on the left and the finished chart page previewed on the right.",
   "caption": null,
   "reuse": null
  }
 ],
 "open_questions": [
  "Info.plist / SceneDelegate.swift / SongListViewController.swift: SceneDelegate.classifyIncoming routes .cho, .chordpro, .chopro, .pro, .crd and .txt URLs to ChartImport, but Info.plist's CFBundleDocumentTypes declares only the Music Folder types and PDF (no plain text or ChordPro type), the + menu's Files picker (attachFiles) and the document pickers elsewhere accept com.adobe.pdf only, and Import Folder takes PDFs and images only. So the guide describes drag and drop onto a music list (the only verified route) plus pasting into the editor. Please confirm on a device whether the Files app's share sheet, Open In or AirDrop offers Music Folder for a .cho or .txt file; if not, should the document types be added, or the guide stay as is?"
 ]
}
---
A chord chart in Music Folder is a song you type rather than scan: the lyrics with chords above them, laid out as pages you can read on a stand, transpose and print. Charts are stored as ChordPro, a common plain-text format for chord charts, and you can type them in that format or with the chords on their own line above the lyrics.

## Start a new chord chart

1. In Library, open **Music** (or a folder) and tap {sf:plus}.
2. Tap **New Chord Chart**.
3. At the top, fill in the title, the artist, and the key the song is written in (tap **Original Key**), plus the tempo (**BPM**) and time signature if you like.
4. Type the chords and lyrics (see below).
5. Tap {sf:checkmark} **Done**. The new chart opens in the reader.

A chart you start inside a folder is added to that folder. If you tap {sf:xmark} **Cancel** instead of Done, the editor asks before it discards your changes.

{shot:chart-editor}

## Add a chart to a piece you already have

To give an existing piece a chord chart, touch and hold it in your music list (or open it and tap **⋯**) and use the item right after **Edit Details**. For a piece with no PDF, or a PDF the app has found to be sheet music, it reads **Add Chord Chart** and starts a blank chart. For any other PDF it reads **Convert to Chord Chart**, which reads the chords and lyrics from the PDF for you; see [Turn a PDF into a chord chart](/guide/turn-a-pdf-into-a-chord-chart).

Once a piece has a chart, the same item reads **Edit Chord Chart**, and with a keyboard you can press Command-E in the reader. A piece can have both a PDF and a chart; choose which one the reader shows with **⋯ › Show**.

## Type chords and lyrics

Put each chord in square brackets right before the syllable it falls on:

A[G]mazing [G7]grace, how [C]sweet the [G]sound

Type section names on a line of their own, such as Verse 1, Chorus, Bridge or Tag. The chart uses them for its headings and for the song order (see [Set the song order](/guide/set-the-song-order)).

Note: Chord chart sections (verses, choruses and so on) are different from the sections you add to a PDF book of music. For those, see [Add sections to a book](/guide/add-sections-to-a-book).

The bar above the keyboard helps you type:

- **[ ]** inserts a pair of chord brackets (Command-Left Bracket on a keyboard).
- Chord buttons appear once the chart has a key and you start typing. They type the common chords of that key and the chords you've used recently.
- **Insert** adds a page break, a column break, a key change, a comment line, or bold or italic text.
- **Symbols** types ♯, ♭, °, ø or Δ.

For a quick reminder of the format, tap {sf:ellipsis} **More** and choose **ChordPro Basics**.

## Type chords above the lyrics

If you're used to charts with the chords on their own line, you can type or paste them that way. The editor highlights a chord line, and when you tap **Done** it merges each chord into the lyric line below, onto the word underneath it.

When you paste a chart written that way, a **Convert to ChordPro** button appears in the bar above the keyboard. Tap it to convert the pasted text now, preview the result, or keep it as typed.

## Preview the pages

On iPad in landscape and on a Mac, the finished pages appear beside the editor and update as you type. On iPhone and in narrower windows, tap **Preview** to see the pages and **Edit** to go back to the text where you left it. When the toolbar is short of room, **Preview** moves into the {sf:ellipsis} **More** menu.

The **Shown as** button above the preview changes the key, capo and chord display you see without changing the chart; choosing another key or a capo needs Premium (see [Transpose, capo and numbers](/guide/transpose-capo-and-numbers)). To undo everything since you opened the editor, tap {sf:ellipsis} **More** and choose **Revert to Saved**.

## Import chord chart files

You can bring in charts saved as .cho, .chordpro, .chopro, .pro, .crd or .txt files by dragging them onto your music list: on iPad, from the Files app in Split View or Slide Over; on a Mac, from the Finder. Drop them on a folder's list to add them to that folder as well. Each file becomes a chord chart, and when you drop a single file, it opens in the reader.

The title comes from the title written in the file, or from the file name if it has none, and plain text with chords above the lyrics is converted to ChordPro. Each imported chart counts as a piece in your library, like any other.

Note: In the {sf:plus} menu, **Files** (**Import from Files** on a Mac) accepts PDFs only. To bring in a chart that's open in another app, copy its text and paste it into a new chord chart.
