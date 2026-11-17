---
{
 "slug": "turn-a-pdf-into-a-chord-chart",
 "h1": "Turn a PDF into a chord chart",
 "seo_title": "Convert a PDF into an Editable Chord Chart | Music Folder",
 "description": "Convert a PDF or scanned chord chart into an editable chart you can transpose: check the flagged lines, confirm the key, and switch back to the PDF.",
 "intent": "general",
 "intent_note": "Musicians with chord charts as PDFs or scans (downloaded charts, church song sheets) who want to transpose them, and users wondering why sheet music can't be transposed.",
 "searches": [
  "convert pdf",
  "transpose pdf",
  "transpose a pdf chord chart",
  "pdf to chordpro",
  "ocr chords",
  "scanned chord chart",
  "change key of pdf",
  "transpose sheet music",
  "edit pdf chords"
 ],
 "availability": [],
 "related": [
  "create-a-chord-chart",
  "transpose-capo-and-numbers",
  "import-music",
  "the-reader-at-a-glance"
 ],
 "feature_link": {
  "href": "/features/chord-charts",
  "text": "chord charts in Music Folder"
 },
 "documents": [
  "Chords/PDFChartConversionFlow.swift",
  "Chords/ChartEditorViewController.swift (review mode)",
  "Chords/PDFChartConverter.swift (decideKey)",
  "Chords/PDFDocumentClassifier.swift",
  "Chords/PDFChordDetector.swift",
  "PDF Reader/PDFReaderToolbar.swift (SongEditActions, showVersionMenu)",
  "Songs/Song View/SongPDFView.swift (chartMenuElements)",
  "R27"
 ],
 "verified": "76048e78",
 "differs_from_4_2": null,
 "shots": [
  {
   "id": "conversion-review",
   "kind": "screen",
   "device": "ipad",
   "orientation": "landscape",
   "state": "Holy, Holy, Holy (PDF chord sheet) converted and open in Review Chart on iPad landscape; no lines flagged.",
   "alt": "Holy, Holy, Holy converted from a PDF and open in Review Chart: the ChordPro text on the left and the chart preview on the right, with the Chart and Original switch above it.",
   "caption": null,
   "reuse": null
  }
 ],
 "open_questions": []
}
---
If you have a chord chart as a PDF, such as a chart you downloaded or a scanned song sheet with chords over the lyrics, Music Folder can read it and turn it into an editable chord chart that you can transpose, play with a capo or read as numbers. The PDF stays with the piece, and you can switch between the two whenever you like.

## Convert a PDF

1. Touch and hold the piece in your music list, or open it and tap **⋯**.
2. Tap **Convert to Chord Chart**. It's right after **Edit Details**.
3. Wait while the app reads the PDF. Scanned pages take a little longer, because the app reads them with text recognition on your device. Tap **Cancel** to stop.
4. Check the chart in the **Review Chart** screen (see below), and fix anything that came across wrong.
5. Tap {sf:checkmark} **Done** to save the chart.

You can also convert from a piece's menu in a set list. If you convert often, you can add {sf:wand.and.rays} **Convert to Chord Chart** to the reader's toolbar with **⋯ › Customize Toolbar**.

## Check the chart before you save it

{shot:conversion-review}

The Review Chart screen is the chord chart editor with the converted text. The lines the app wasn't sure about, where a chord may be in the wrong place or a word misread, have a dotted underline. The toolbar shows how many are left, for example **2 to Check**. Tap it and choose **Show Next Line to Check** to go to the next one, or **Mark All as Checked** once you've looked them over. The same menu also lists notes about the conversion, such as text it left out.

To compare with the original, switch between **Chart** and **Original** above the preview. Edit the text as you would any chart; see [Create a chord chart](/guide/create-a-chord-chart).

If you tap **Done** while lines are still unchecked, the app tells you how many are left; tap **Review** to keep checking or **Save Anyway**. If you cancel instead, nothing is saved and the PDF stays as it was.

Website addresses, page numbers, publisher and license lines, and chord diagrams aren't copied into the chart. Musical directions, such as a repeat or a return to the chorus, are kept as comment lines. From a lead sheet, the chords and lyrics come across, but the melody doesn't.

## Check the key

The key field at the top of the editor shows **Original Key: D** when the key is known, from the PDF itself, from a key you've chosen before, or from the piece's details (unless the chords clearly say otherwise). When the app worked the key out from the chords, the field says **Detected Key: D** instead, and when it can't tell, **Key Unknown**. Tap the field to keep the key shown, use the detected one, or pick another key. The key matters, because transposing and numbers start from it.

## Switch between the chart and the PDF

After you save, the piece opens on the chord chart, and the menu item after **Edit Details** reads **Edit Chord Chart** from then on. To see the PDF again, choose **⋯ › Show › Original PDF**; choose **⋯ › Show › Chord Chart** to go back. The reader remembers your choice for that piece. Both versions are kept, along with any markings you've made on each.

## When a PDF can't be converted

- **Sheet music:** Music written on staves can't be converted or transposed, and the app tells you so. Conversion works with chord charts, where the chords are written over the lyrics. Once the app knows a PDF is sheet music, its menu shows **Add Chord Chart** instead, which starts a blank chart you can type yourself.
- **Lyrics without chords:** The app offers to start a chart from the lyrics so you can add the chords. The menu item may read **Start Chart from Lyrics**.
- **Nothing readable:** If the app finds no chords or lyrics, it offers to start a blank chart for the piece instead.
