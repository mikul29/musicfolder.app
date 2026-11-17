---
{
 "slug": "add-text-symbols-and-shapes",
 "h1": "Add text, symbols and shapes",
 "seo_title": "Add Text, Music Symbols and Shapes | Music Folder",
 "description": "Add typed text, music symbols like dynamics and fermatas, and shapes like hairpins, slurs and staves to your sheet music, then move, resize or delete them.",
 "intent": "existing",
 "intent_note": "Musicians who want neat dynamics, articulations, rehearsal marks or typed notes on a PDF instead of handwriting, and users looking for the + in the tool palette.",
 "searches": [
  "stamps",
  "dynamics",
  "hairpin",
  "crescendo",
  "slur",
  "fermata",
  "rehearsal mark",
  "bar number",
  "type text on pdf",
  "cover up",
  "white out",
  "staff lines"
 ],
 "availability": [
  {
   "kind": "requires",
   "text": "Add Text, Add Symbol and Add Shape need iOS 18 or iPadOS 18 or later."
  }
 ],
 "related": [
  "mark-up-music-with-apple-pencil",
  "use-annotation-layers",
  "jump-to-repeats-with-page-links"
 ],
 "feature_link": {
  "href": "/features/annotation",
  "text": "annotation in Music Folder"
 },
 "documents": [
  "PDF Reader/PDFReaderInk.swift (installAccessoryMenu)",
  "PDF Reader/AnnotationTextEditor.swift",
  "PDF Reader/AnnotationTextOverlay.swift",
  "PDF Reader/AnnotationTextPopovers.swift",
  "PDF Reader/MusicSymbolOverlay.swift",
  "PDF Reader/MusicSymbolPaletteViewController.swift",
  "PDF Reader/MusicSymbolCatalog.swift",
  "PDF Reader/MusicShape.swift",
  "R46",
  "R47"
 ],
 "verified": "76048e78",
 "differs_from_4_2": null,
 "shots": [
  {
   "id": "symbol-palette",
   "kind": "crop",
   "device": "ipad",
   "orientation": "landscape",
   "state": "Wiegenlied in annotation mode with the Symbols card open: Recently Used and the Dynamics tab.",
   "alt": "The Symbols card above the annotation tools, with recently used symbols and the Dynamics tab showing dynamics from pppp to sub.",
   "caption": null,
   "reuse": null
  }
 ],
 "open_questions": []
}
---
Besides drawing by hand, you can type text onto a page and place clean music symbols and shapes: dynamics, accents, fermatas, rehearsal marks, hairpins, slurs, brackets and extra staves. They go on the layer you're drawing on, so you can hide them with that layer.

All three start from the **+** button in the tool palette, which appears while you annotate. On iPad, tapping **+** shows a menu; on iPhone, the menu opens just above the palette.

## Add text

1. Open a piece and tap {sf:pencil.tip.crop.circle} **Annotate**.
2. Tap **+** in the tool palette, then tap **Add Text**.
3. A text box appears in the middle of the page (or in the middle of what's on screen, if you've zoomed in). Tap it to bring up the keyboard, then type.
4. Tap outside the box when you're done.

Tap a text box once to select it. While it's selected you can drag it to move it, pinch it to make the text bigger or smaller, or drag the dots on its sides to set how wide it is before the text wraps. Tap it again to edit the words.

A selected text box has a small toolbar: the color circle changes the text color, {sf:textformat} sets the font, size, bold, italic, underline, strikethrough and alignment, {sf:plus.square.on.square} duplicates the box, and {sf:trash} deletes it.

## Add a symbol

1. While annotating, tap **+** in the tool palette, then tap **Add Symbol**.
2. Find the symbol. The symbols you used most recently are at the top; below them, tabs sort the rest into **Dynamics**, **Articulation**, **Notes**, **Technique**, **Navigation**, **Words** and **Cues**. You can also swipe the grid to move between tabs, and the palette opens on the tab you used last time.
3. Tap the symbol you want. The palette closes and a bar at the top of the page tells you what to do next.
4. Tap the page where the symbol goes. To place it precisely, touch and hold: a magnifier appears, and you can slide to aim and lift your finger to place it.
5. The symbol you placed stays selected, so you can move or resize it right away. Tap elsewhere to put it down, then tap again to add another of the same symbol. When you've finished, tap **Done** in the bar at the top, or tap {sf:square.grid.2x2} **Choose Another Symbol** to pick a different one.

{shot:symbol-palette}

Rehearsal marks, bar numbers and string numbers ask for their text when you place them. To change it later, double-tap the symbol, or select it and tap {sf:character.cursor.ibeam} **Edit Text**.

## Add a shape

Shapes are marks you draw to size, such as a long crescendo or a slur over several notes.

1. While annotating, tap **+** in the tool palette, then tap **Add Shape**.
2. Choose a shape from the **Hairpins & Slurs**, **Lines**, **Shapes** or **Staff** tab.
3. Drag across the page to draw it, or tap to place it at a standard size. It stays selected so you can adjust it; tap elsewhere to put it down, then draw another.
4. Tap **Done** in the bar at the top when you've finished.

The **Shapes** tab includes circles for highlighting a passage and cover-ups, which hide part of the printed page in the color of the paper. You can write on top of a cover-up, so it's useful for replacing a printed fingering or a wrong note. The **Staff** tab adds blank staff lines, for example to write out an ossia or a changed passage; select a staff and tap {sf:music.note.list} **Staff** to change its lines or the number of bars.

## Move, resize or delete a symbol or shape

- **Select:** tap a symbol or shape. Handles appear around it.
- **Move:** drag a selected symbol or shape. To move one that isn't selected, touch and hold it until it lifts, then drag.
- **Resize:** pinch a selected symbol, or drag a corner handle. Symbols keep their proportions. A shape's handles change its ends and curve (for a hairpin or slur), its corners (for a box), or its edges (for a staff).
- **Change the color:** tap the color circle in the symbol's toolbar. Cover-ups always match the paper.
- **Copy or delete:** tap {sf:plus.square.on.square} **Duplicate** or {sf:trash} **Delete**.

Tap anywhere else on the page to put a selected symbol down.

Tip: Navigation signs such as D.S. al Coda, D.C. and To Coda show a {sf:link} **Link** button when selected. Use it to make the sign a jump in your music; see [Jump to repeats with Page Links](/guide/jump-to-repeats-with-page-links).

Text, symbols and shapes work on chord charts too. Like drawn marks, they're personal: they're included when you use **Share as PDF** (if their layer is visible) and never shared with the people in a shared folder or set list.
