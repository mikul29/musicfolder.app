---
{
 "slug": "mark-up-music-with-apple-pencil",
 "h1": "Mark up music with Apple Pencil",
 "seo_title": "Annotate Sheet Music with Apple Pencil | Music Folder",
 "description": "How to write on sheet music and chord charts in Music Folder with Apple Pencil or your finger: pens, highlighter, eraser, and finishing your markings.",
 "intent": "existing",
 "intent_note": "Musicians who want to write fingerings, dynamics and reminders on a PDF score, and existing users looking for how to start and stop annotating.",
 "searches": [
  "annotate",
  "draw on pdf",
  "write on sheet music",
  "markup",
  "pencil",
  "highlighter",
  "eraser",
  "finger drawing",
  "markings"
 ],
 "availability": [],
 "related": [
  "use-annotation-layers",
  "add-text-symbols-and-shapes",
  "send-a-copy-or-print",
  "the-reader-at-a-glance"
 ],
 "feature_link": {
  "href": "/features/annotation",
  "text": "annotation in Music Folder"
 },
 "documents": [
  "PDF Reader/PDFAnnotationSession.swift",
  "PDF Reader/PDFReaderToolbar.swift (ReaderAnnotationChrome, PDFReaderOrientation)",
  "PDF Reader/PageTurnerKeys.swift (acceptsTurn)",
  "PDF Reader/ReaderToolbarCustomization.swift",
  "Chords/ChartAnchor.swift",
  "Sharing/AnnotationLayerTransport.swift",
  "R30",
  "R31",
  "R32"
 ],
 "verified": "76048e78",
 "differs_from_4_2": null,
 "shots": [
  {
   "id": "annotate-session",
   "kind": "screen",
   "device": "ipad",
   "orientation": "landscape",
   "state": "Wiegenlied (Lullaby) in annotation mode on iPad landscape, tool palette docked at the bottom.",
   "alt": "Wiegenlied in annotation mode on iPad: the highlighted pencil and the Layers button in the toolbar, handwritten markings on the page, and the tool palette at the bottom.",
   "caption": null,
   "reuse": null
  }
 ],
 "open_questions": [
  "PDFAnnotationSession.swift: the code relies on Apple's tool palette for finger drawing (drawingPolicy .default; the comment names the palette's \"Draw with Finger\" switch). Confirm that switch's current wording in the iPadOS 18 / 26 tool palette and whether to also mention Settings › Apple Pencil › Only Draw with Apple Pencil.",
  "PDFAnnotationSession.swift: drawing with a mouse or trackpad on a Mac is not covered here; confirm how annotation behaves on Mac before adding it."
 ]
}
---
You can write fingerings, breath marks, dynamics and reminders straight onto your sheet music with Apple Pencil, or with your finger. Your markings are saved with the piece and show wherever you open it, including in set lists.

{shot:annotate-session}

## Start annotating

1. Open a piece.
2. Tap {sf:pencil.tip.crop.circle} **Annotate** in the toolbar. If you moved it off the toolbar, you'll find **Annotate** in the **⋯** menu.
3. Draw on the page.

While you annotate, the pencil button stays highlighted in orange and Apple's tool palette appears. On iPad the palette floats over the page, and you can drag it out of the way; on iPhone it sits along the bottom of the screen. The {sf:square.3.layers.3d} **Layers** button appears beside the pencil, so you can choose which layer you're drawing on (see [Use annotation layers](/guide/use-annotation-layers)).

## Choose a pen, highlighter or eraser

The tool palette is the same one you use in Notes and Markup. Tap a tool to pick it: pens and a pencil for writing, the highlighter for marking a passage, the eraser, the lasso for selecting and moving marks, and the ruler for straight lines. Tap a color to change it, and use the palette's undo and redo buttons to step back.

The eraser and the lasso only reach the marks on the layer you're drawing on. Marks on other layers stay as they are.

To work on a small detail, pinch with two fingers to zoom in, and drag with two fingers to move around the page.

## Draw with your finger

If you use an Apple Pencil, the Pencil draws and one finger scrolls the page, as in Notes. To draw with your finger as well, turn on **Draw with Finger** in the tool palette's options. Without an Apple Pencil, for example on iPhone, your finger draws. Two fingers always zoom and scroll.

## Finish annotating

When you're done, tap the highlighted pencil again; there's no separate Done button. Your markings are saved as you finish.

You annotate the page that's on screen (both pages, if you use Two-Page View). Pages don't turn while you're annotating, so to mark another page, finish, turn the page, and tap {sf:pencil.tip.crop.circle} **Annotate** again.

Note: The screen keeps its current orientation while you annotate and rotates again when you finish. If the window changes size anyway, for example in Stage Manager, your markings stay in place on the page.

## Mark up a chord chart

You can annotate chord charts the same way. Each mark you draw is attached to the line of the chart it's next to, so it moves with that line when you transpose, change the text size or formatting, or turn on Follow Sequence. If you later edit a line so much that it can't be found, the mark stays where you drew it on the page.

## Who sees your markings

Your markings are personal. If your library syncs with iCloud, they sync to your other devices too, but they're never shared with the people in a shared folder or set list, who keep markings of their own.

When you send a copy, **Share as PDF** includes the markings on your visible layers, and a Music Folder file includes your layers so the person who opens it gets them too. See [Send a copy or print](/guide/send-a-copy-or-print).
