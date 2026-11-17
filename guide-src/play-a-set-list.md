---
{
 "slug": "play-a-set-list",
 "h1": "Play a set list",
 "seo_title": "Play Through a Set List on Stage | Music Folder",
 "description": "Play a set list from the first piece or any piece, turn straight from one piece to the next, use Perform Set for the stage, and open a section's whole book.",
 "intent": "existing",
 "intent_note": "Musicians on stage or in rehearsal who want to play through a set list without stopping between pieces, and users looking for Perform Set or Open Whole Document.",
 "searches": [
  "start set",
  "perform set",
  "play through",
  "next song",
  "gig mode",
  "stage mode",
  "open whole document",
  "section tempo",
  "3 of 8"
 ],
 "availability": [],
 "related": [
  "use-performance-mode",
  "turn-pages-hands-free",
  "add-pages-and-timing-to-a-set-list",
  "use-the-metronome"
 ],
 "feature_link": {
  "href": "/features/set-lists",
  "text": "Set Lists"
 },
 "documents": [
  "Set Lists/Songs View/SetListViewSongs.swift",
  "Set Lists/Songs View/PDFViewInSetList.swift",
  "Set Lists/Songs View/SetListSummaryPanel.swift",
  "PDF Reader/PDFReaderToolbar.swift",
  "PDF Reader/PerformanceModeController.swift",
  "Services/SetListPlaceholder.swift",
  "R41",
  "R42",
  "R66",
  "R67"
 ],
 "verified": "76048e78",
 "differs_from_4_2": null,
 "shots": [
  {
   "id": "setlist-ipad-panel",
   "kind": "screen",
   "device": "ipad",
   "orientation": "landscape",
   "state": "Spring Recital set list on iPad landscape: summary panel and run sheet with an Intermission page.",
   "alt": "The Spring Recital set list on iPad: the summary panel with its date, piece count, total time and Perform Set button, beside the run sheet with each piece's key, tempo and time and an Intermission page.",
   "caption": null,
   "reuse": null
  }
 ],
 "open_questions": []
}
---
When you play a set list, the whole set opens as one continuous score. You turn pages the same way you always do, and the last page of one piece leads straight into the first page of the next, with no trip back to the list.

{shot:setlist-ipad-panel}

## Start the set

{sf:play.fill} **Perform Set** plays the set from the first piece in Performance Mode, the stage reader that hides the toolbar and turns taps on the page into page turns. On iPad and Mac it's the orange button in the summary panel beside the set list. On iPhone (and in a narrow window) it's the full-width button under the piece count at the top of the set list.

To start somewhere else, tap a piece in the set list. The set opens at that piece in the regular reader, with the toolbar and all its tools, which is useful in rehearsal when you want to begin partway through. Either way the whole set is open, so you can also turn back to earlier pieces.

## Move through the set

Turn pages by swiping, with the keyboard or with a Bluetooth page turner. A piece that appears twice in the set plays twice, in its place. Pages you added between pieces (an intermission, an announcement) come up in order, and a page with a duration shows its countdown. See [Add pages and timing to a set list](/guide/add-pages-and-timing-to-a-set-list).

On iPad and Mac, the title at the top of the reader names the piece on screen. With iPadOS 26 or macOS 26 or later, its place in the set appears under the title, such as "3 of 8".

Half-Page Turns work inside a piece, but a turn onto or off a set-list page is always a whole-page turn. For more on turning, see [Turn pages](/guide/turn-pages) and [Turn pages hands-free](/guide/turn-pages-hands-free).

## Tempo and the metronome in a set

Each piece plays at its own tempo and time signature, so the metronome is ready for every piece as you reach it. A section in the set uses the section's own tempo and time signature, not the book's. When a whole book is in the set and its sections have tempos, the metronome follows the section on the page.

If you change the tempo by hand during the set, the new tempo holds for that piece until you leave the set, and it isn't saved to the piece. When you've changed the tempo of a whole book whose sections have tempos, **⋯ › Follow Section Tempos** goes back to following them. More in [Use the metronome](/guide/use-the-metronome).

## Open the whole book from a section

A section in a set list plays only its own pages. To see the rest of the book it comes from (to check the next movement or a cue on the page before), open the **⋯** menu while the section is on screen and choose **Open Whole Document** (it isn't offered in Performance Mode). The book opens at the page you were on, and Back returns you to the set at the same place.

## Leave the set

In the regular reader, tap Back to return to the set list. In Performance Mode, first leave the mode: touch and hold **Done** at the top of the screen (a quick tap only shows **Hold to Exit**). Then tap Back. See [Use Performance Mode](/guide/use-performance-mode) for what the mode hides and how to set it up.
