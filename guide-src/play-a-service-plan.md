---
{
 "slug": "play-a-service-plan",
 "h1": "Play a service plan",
 "seo_title": "Play a Planning Center Service Plan | Music Folder",
 "description": "Open a Planning Center service in Music Folder, play through its songs in order, pick the right chart or PDF, and transpose chord charts from the plan key.",
 "intent": "existing",
 "intent_note": "A worship musician who connected Planning Center and wants to lead or play Sunday's service from an iPad, with the right charts in the right keys.",
 "searches": [
  "planning center plan",
  "service order",
  "worship set",
  "sunday service",
  "run of service",
  "chord chart key",
  "transpose planning center",
  "attachments",
  "lead sheet",
  "pco"
 ],
 "availability": [
  {
   "kind": "requires",
   "text": "Needs Planning Center connected (Premium and a Planning Center Services account)."
  }
 ],
 "related": [
  "connect-planning-center",
  "transpose-capo-and-numbers",
  "play-a-set-list",
  "use-performance-mode"
 ],
 "feature_link": {
  "href": "/planning-center",
  "text": "Music Folder for Planning Center"
 },
 "documents": [
  "Planning Center/PCOPlanViewController.swift",
  "Planning Center/PCOPDFViewController.swift",
  "Planning Center/PCOLibraryStore.swift",
  "Chords/PCOChartSupport.swift",
  "Services/SetListSections.swift",
  "Set Lists/Set List View/SetListGridCell.swift"
 ],
 "verified": "76048e78",
 "differs_from_4_2": null,
 "shots": [
  {
   "id": "pco-plan",
   "kind": "screen",
   "device": "iphone",
   "orientation": "portrait",
   "state": "A Planning Center service plan open on iPhone: date, plan sections as headings, numbered songs with page thumbnails and their keys.",
   "alt": "A Sunday Service plan from Planning Center on iPhone: the date, the plan's sections such as Communion and Offering as headings, and numbered songs with page thumbnails and their keys.",
   "caption": null,
   "reuse": "planning-center-iphone.jpg"
  }
 ],
 "open_questions": []
}
---
Each Planning Center service appears in Music Folder as a set list, with its songs in service order. Open one to see the run of service, then play through every song with the sheet music or chord chart your team uses, in the keys set in the plan.

## Open a service

1. In **Library**, open **Set Lists**.
2. Tap a service marked "Planning Center".

The service shows its date and total time at the top, then its songs, numbered in order with the key set for each one. Other items from the plan, such as a welcome or the sermon, appear between the songs as plain rows so you can follow the whole service.

{shot:pco-plan}

Services are read-only here. To reorder songs, change a key or add an item, edit the plan in Planning Center, then pull down on the service in Music Folder to refresh it. Pulling down also downloads charts again if they were changed in Planning Center.

## Play through the service

1. Tap the first song (or any song) to open it.
2. Turn pages as usual. When you turn past the last page of a song, the next song follows in the same reader.

On the last page of each song, a label names the song that's up next; on the last page of the service it says "End of service". When you open a service, Music Folder downloads its songs in the background, so the whole service works offline once it has loaded.

The reader has the same tools as the rest of the app: metronome (set to the arrangement's tempo when Planning Center has one), tuner, piano, notes, annotation and Performance Mode. If a song has an audio file in Planning Center, tap {sf:play.fill} **Play Recording** to hear it.

## Choose the sheet music for a song

A song in Planning Center can have several attachments, such as a lead sheet, a chord chart and parts in different keys. Music Folder opens the one you last chose for that song. Until you choose, it opens the attachment picked in the plan, or the first one.

1. Tap {sf:doc.on.doc} **Sheet Music** on the toolbar. If it isn't there, tap **⋯**, then **Sheet Music**.
2. Choose an attachment. **Chord Chart** at the top is the song's chord chart written in Planning Center; PDFs follow, grouped by arrangement and key.

## Use Planning Center chord charts

A chord chart written in Planning Center opens in the key set for that song in this service. If the arrangement has a song order, you can turn on **Follow Sequence** in the **⋯** menu to lay the chart out in that order.

To play in another key, use the **Key** control on the toolbar. It's there whenever a chord chart is on screen. Transposing changes only your own view; nothing changes in Planning Center or for anyone else. See [Transpose, capo and numbers](/guide/transpose-capo-and-numbers).

## Save a chord chart to your library

To keep your own editable copy of a Planning Center chord chart:

1. Open the song with its chord chart.
2. Tap **⋯**, then **Save to My Library**. You can also find **Save to My Library** in the **Key** control.

The chart becomes one of your own songs, written in the key set in the service (your own transposition isn't applied), with the arrangement's tempo and time signature. It doesn't stay linked to Planning Center, so later changes there don't reach it. Saved songs count toward the free limit of 15 pieces.

## Notes and markings

To add a note to a song, touch and hold it in the service and choose **Notes**, or tap Notes in the reader. Notes and markings on Planning Center songs are yours and stay in Music Folder; the first time you annotate, the app reminds you that they aren't sent back to Planning Center, so your team won't see them.
