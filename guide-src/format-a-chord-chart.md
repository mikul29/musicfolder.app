---
{
 "slug": "format-a-chord-chart",
 "h1": "Format a chord chart",
 "seo_title": "Change Chord Chart Fonts and Page Size | Music Folder",
 "description": "Change a chord chart's font, text size, chord color, columns, page size, orientation and margins, for one chart or as the default for all your charts.",
 "intent": "existing",
 "intent_note": "Users who want bigger text, one or two columns, A4 or Letter pages, or a different look for their chord charts, for one chart or all of them.",
 "searches": [
  "font",
  "text size",
  "columns",
  "two columns",
  "page size",
  "a4",
  "letter",
  "landscape",
  "margins",
  "chord color",
  "bold chords",
  "chart layout",
  "default formatting"
 ],
 "availability": [],
 "related": [
  "create-a-chord-chart",
  "transpose-capo-and-numbers",
  "set-the-song-order",
  "send-a-copy-or-print"
 ],
 "feature_link": {
  "href": "/features/chord-charts",
  "text": "chord charts in Music Folder"
 },
 "documents": [
  "Chords/ChartFormattingViewController.swift",
  "Chords/ChartViewState.swift (ChartFormatting, ChartPageSize)",
  "Chords/ChartLayout.swift (ChartFontFamily, ChartColorRole, ChartRenderOptions)",
  "Chords/ChartEditorViewController.swift (Formatting)",
  "Chords/CHORD_SPEC.md §7"
 ],
 "verified": "76048e78",
 "differs_from_4_2": null,
 "shots": [
  {
   "id": "formatting-panel",
   "kind": "crop",
   "device": "ipad",
   "orientation": "landscape",
   "state": "Amazing Grace open in the chord chart editor with the Formatting popover open from the Formatting button: This Chart selected at the top, the Text section (Font System, Size 11.6 pt (Default), Chord Color Black, Chord Weight Bold), the Layout section (Columns 1, Show Section Abbreviations off, Keep Sections Together on) and the Page section (Page Size Letter, Orientation Portrait, Margins Normal). Crop to the popover with the preview edge behind it.",
   "alt": "The Formatting panel for a chord chart with This Chart selected, showing the font, size, chord color and chord weight, the number of columns, and the section switches.",
   "caption": null,
   "reuse": null
  }
 ],
 "open_questions": []
}
---
You can change how a chord chart looks on the page: its font and text size, the color and weight of the chords, the number of columns, and the page size. Formatting can apply to one chart or be your default for every chart, and the same pages appear everywhere the chart does, in the reader, in set lists and when you share it as a PDF.

## Change a chart's formatting

1. Open the chart and choose **⋯ › Edit Chord Chart**.
2. Tap {sf:textformat.size} **Formatting**. If it isn't on the editor's toolbar, tap {sf:ellipsis} **More** and choose **Formatting…**.
3. At the top, choose **This Chart** to format only this chart, or **Defaults** to change the formatting of every chart that doesn't have its own.
4. Change the settings you want. The preview updates as you go.
5. Tap {sf:xmark} **Close** to close the panel, then tap {sf:checkmark} **Done** to save.

{shot:formatting-panel}

If you cancel the editor instead of tapping Done, your formatting changes are discarded along with any other edits. On iPhone and in narrow windows, the panel opens as a sheet and the editor switches to its preview, so you can see each change above the panel.

## The settings

**Text**

- **Font**: System, Avenir Next, Helvetica Neue, Rounded, Georgia, New York, Menlo or Chalkboard. Menlo keeps every letter the same width, which helps if you line up chords with spaces.
- **Size**: from 9 to 20 points; 11.6 points is the default.
- **Chord Color**: Black, Orange, Red, Blue, Green or Purple.
- **Chord Weight**: Bold or Regular.

**Layout**

- **Columns**: 1, 2 or 3, or Auto, which picks the number of columns from the page width. Until you change the default, charts use one column.
- **Show Section Abbreviations**: shows a code such as V1 or C1 beside each section heading.
- **Keep Sections Together**: moves a section that doesn't fit at the bottom of a column to the next column. Turn it off to split the section there instead. A section taller than a whole column is split either way, and the continuation is marked "(continued)".

Note: Chord chart sections (verses, choruses and so on) are different from the sections you add to a PDF book of music. For those, see [Add sections to a book](/guide/add-sections-to-a-book).

**Page**

- **Page Size**: Letter, A4, Legal, 11 × 17, Widescreen 16:9 or Fullscreen 4:3. The last two are shaped for projectors and screens rather than paper. Until you choose, the default is Letter in the United States, Canada and other countries that use Letter paper, and A4 elsewhere.
- **Orientation**: Portrait or Landscape.
- **Margins**: Narrow, Normal or Wide.

## This Chart and Defaults

A new chart follows your defaults. As soon as you change something under **This Chart**, the chart gets its own formatting and stops following the defaults. To make it follow them again, choose **This Chart** and tap **Use Defaults for This Chart** at the bottom of the panel.

Changes under **Defaults** apply to every chart that doesn't have its own formatting, including charts you create later.

Tip: To make the text bigger or smaller while you play, you don't need to open the editor. With a keyboard, press Command-Plus or Command-Minus in the reader. See [Transpose, capo and numbers](/guide/transpose-capo-and-numbers).
