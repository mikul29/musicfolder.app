---
{
 "slug": "add-pages-and-timing-to-a-set-list",
 "h1": "Add pages and timing to a set list",
 "seo_title": "Add Breaks, Notes and Timing to a Set List | Music Folder",
 "description": "Add intermission, announcement and note pages between pieces, give pieces a duration, and see a set list's total time and a live countdown on stage.",
 "intent": "existing",
 "intent_note": "Band leaders and music directors who want breaks, spoken cues and a running time in their set list, and who need to know how long a set will run.",
 "searches": [
  "intermission",
  "set break",
  "announcement",
  "stage notes",
  "set length",
  "running time",
  "total time",
  "duration",
  "countdown timer",
  "how long is my set"
 ],
 "availability": [],
 "related": [
  "create-and-edit-a-set-list",
  "play-a-set-list",
  "edit-or-delete-a-piece",
  "add-sections-to-a-book"
 ],
 "feature_link": null,
 "documents": [
  "Services/SetListPlaceholder.swift",
  "Set Lists/Add Set List/SetListPageEditorViewController.swift",
  "Set Lists/Songs View/SetListPageTimerView.swift",
  "Set Lists/Songs View/SetListLibraryPane.swift",
  "Set Lists/Songs View/SetListSummaryPanel.swift",
  "Services/SetTiming.swift",
  "Shared UI/SetListPageRenderer.swift",
  "R38",
  "R42"
 ],
 "verified": "76048e78",
 "differs_from_4_2": null,
 "shots": [
  {
   "id": "setlist-stats-iphone",
   "kind": "crop",
   "device": "iphone",
   "orientation": "portrait",
   "state": "Spring Recital on iPhone: PIECES 7, TOTAL TIME 1 h 38 min, Perform Set, the first rows of the run sheet.",
   "alt": "A set list on iPhone with its piece count and total time under the title, the Perform Set button, and the first pieces with their tempo and duration.",
   "caption": null,
   "reuse": null
  }
 ],
 "open_questions": []
}
---
Set lists can hold more than music. You can add pages for an intermission, an announcement or a note to the band, and give pieces and pages a duration so you know how long the set will run. Pages and timing are free.

## Add a page between pieces

A page is a single screen of large, stage-readable text that plays in the set like any other page. It isn't music, so it never appears in your library, doesn't count toward the free limit and isn't numbered with the pieces.

1. Open the set list and tap {sf:plus}.
2. Switch to **Pages** at the top of the pane or sheet.
3. Tap **Intermission**, **Announcement**, **Note** or **Blank Page**. Each one only fills in a starting title; you can change everything.
4. Type a **Title** and, if you like, some **Text**: talking points, a cue, who's playing next.
5. Under **Details**, choose a **Page Color** (White or Black) and, optionally, a **Duration**.
6. Tap {sf:checkmark} **Add Page**.

The preview in the form shows the page as it will look in the set. A Blank Page prints nothing at all, which is useful for a pause between two pieces that shouldn't run together.

Pages go into the set at the end, or after the piece you chose with **Add Piece After This…** on iPad and Mac. Move and remove them like pieces: drag to reorder, swipe left to remove.

## Edit a page

Touch and hold the page in the set list and choose **Edit Page**. You can also edit the page while you're playing the set: with the page on screen, open the **⋯** menu and choose **Edit Page**. Changes appear in place.

## Give pieces a duration

A piece's duration is part of its details. Open the piece's details with **Edit Details** and set **Duration** in minutes and seconds. A section has its own **Duration** in its section details, separate from the whole book's. See [Edit or delete a piece](/guide/edit-or-delete-a-piece) and [Add sections to a book](/guide/add-sections-to-a-book).

If you attach a recording to a piece that has no duration yet, the recording's length fills it in. A duration you set yourself is never replaced.

## See the set's total time

The set list adds up every piece and page that has a duration, in play order. A piece that appears twice counts twice, and a section counts its own duration rather than the whole book's.

- **On iPhone** (and in a narrow window), the top of the set list shows **PIECES**, **TOTAL TIME** and, while some pieces have no duration, **UNTIMED**.
- **On iPad and Mac**, the summary panel beside the set list shows the number of pieces, the total time with the untimed count next to it, and the total number of pages. A **TIME** column appears next to **KEY** and **BPM** once any entry has a duration.

{shot:setlist-stats-iphone}

Pages never count as untimed: a page without a duration adds nothing to the total. If nothing in the set has a duration, no total is shown.

## Use the countdown on stage

When a page has a duration, the duration is printed on the page in small type (for example, "15 min"), so it shows on printouts and shared PDFs too. While you play the set, the page also shows a live countdown near the bottom of the screen:

- It starts the first time the page appears and keeps running while you move on to other pages.
- Tap it to pause; tap again to resume.
- After zero it counts overtime (for example, "+0:45") in orange. It never makes a sound.

Changing the page's duration starts the countdown again. The countdown also appears in Performance Mode.
