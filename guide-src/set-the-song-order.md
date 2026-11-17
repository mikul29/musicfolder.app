---
{
 "slug": "set-the-song-order",
 "h1": "Set the song order",
 "seo_title": "Set a Song's Section Order and Sequence | Music Folder",
 "description": "Name a chord chart's verses and choruses, build the song's sequence (V1, C1, V2, Bridge), and use Follow Sequence to read the chart in the order you play it.",
 "intent": "existing",
 "intent_note": "Band and worship musicians who want a chart's arrangement (verse, chorus, bridge, repeats) written once and read in play order, as in Planning Center.",
 "searches": ["sequence", "arrangement", "song structure", "song map", "verse chorus order", "repeat chorus", "roadmap", "follow sequence", "section labels", "v1 c1"],
 "availability": [],
 "related": ["create-a-chord-chart", "format-a-chord-chart", "play-a-service-plan", "add-sections-to-a-book"],
 "feature_link": {"href": "/features/chord-charts", "text": "chord charts in Music Folder"},
 "documents": ["Chords/ChartSequenceEditorViewController.swift", "Chords/ChartSequence.swift", "Chords/ChartEditorViewController.swift (Edit Sequence)", "Songs/Song View/SongPDFView.swift (chartMenuElements)", "Chords/CHORD_SPEC.md §6, §8", "R24"],
 "verified": "76048e78",
 "differs_from_4_2": null,
 "shots": [
  {"id": "sequence-editor", "kind": "crop", "device": "ipad", "orientation": "landscape",
   "state": "The Edit Sequence sheet for a chart with one Verse 1 and one Chorus: the sequence list on the left holding 1 Verse 1 and 2 Chorus, and the labels on the right: Verse with a filled 1 and an outlined 2, Chorus the same, Bridge with an outlined 1, then Intro, Outro, Ending, Instrumental, Interlude and Tag with outlined 1s.",
   "alt": "The Edit Sequence screen, with the song's sequence listed on the left and buttons for verses, choruses, bridge and other section labels on the right.",
   "caption": null, "reuse": "chart-sequence.jpg"}
 ],
 "open_questions": []
}
---
Most songs repeat sections: a chorus after every verse, a bridge, a tag at the end. In a chord chart you can write each section once and then set the song's sequence, the order you actually play it. The chart shows the sequence at the top, and the reader can lay the whole chart out in that order.

Note: Chord chart sections (verses, choruses and so on) are different from the sections you add to a PDF book of music. For those, see [Add sections to a book](/guide/add-sections-to-a-book).

## Name the sections

In the chord chart editor, type each section's name on a line of its own, for example:

- Verse 1, Verse 2, Chorus, Pre-Chorus, Bridge
- Intro, Outro, Ending, Instrumental, Interlude, Tag

Short codes such as V1, C2 and PC work too, as do names in brackets or capitals with a colon, like [Chorus] or CHORUS:. For a section of your own, write a name of up to four words in title case or capitals, ending in a colon, such as Last Chorus:.

The chart's headings show your names exactly as you typed them. When a section name appears more than once without a number, such as two sections both called Chorus, the app numbers them in order behind the scenes (C1, C2) so the sequence can tell them apart.

## Build the sequence

1. Open the chart and choose **⋯ › Edit Chord Chart**.
2. Tap {sf:list.number} **Edit Sequence**. If it isn't on the editor's toolbar, tap {sf:ellipsis} **More** and choose **Edit Sequence…**.
3. In the labels, tap a section's number to add it to the end of the sequence (for example, 2 beside Verse adds Verse 2), or drag the number to the place you want. The buttons stay after you use them, so you can tap Chorus 1 again for every time it comes back.
4. To change the order, drag a row by its handle. To remove a row, swipe left and tap **Remove**, or touch and hold it for **Move Up**, **Move Down**, **Duplicate** and **Remove**.
5. Tap {sf:checkmark} **Save** to keep the sequence, then tap {sf:checkmark} **Done** in the editor to save the chart.

{shot:sequence-editor}

The labels list the chart's own sections first, each section type with a numbered button for every verse or chorus the chart has, followed by the common section names. A number with an outline instead of a fill is one the chart doesn't have yet. To add a label of your own, such as Guitar Solo, type it in **Add a new label** and tap {sf:plus.circle} **Add label**. To delete a label you created, tap {sf:xmark.circle.fill} beside it, or touch and hold its name and choose **Delete Label**. Its heading comes out of the chart when you save, but the lyrics and chords under it stay.

When there's room, the labels sit beside the sequence; on a narrow screen they're below it. Once you save, the sequence appears in the **ORDER** strip at the top of the chart.

## Read the chart in play order

By default, a chart shows each section once, in the order you wrote it. Where the next section in the sequence isn't the next one on the page, a cue at the right of the section's heading tells you where to go, such as C1 → V3, or End. The page footer says **Compact**.

To read the chart in the order you play it, open it in the reader and choose **⋯ › Follow Sequence**. The chart is then laid out section by section in sequence order. A section that comes back is printed again, a section repeated straight away is printed once with ×2, and sections that aren't in the sequence are left out. The footer says **Full order** while this is on; choose **Follow Sequence** again to go back to the compact layout.

**Follow Sequence** appears in the **⋯** menu only when the chart has a sequence. It works in set lists and in Planning Center plans too, where a song's Planning Center sequence is used.
