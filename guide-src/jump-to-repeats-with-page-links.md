---
{
 "slug": "jump-to-repeats-with-page-links",
 "h1": "Jump to repeats with Page Links",
 "seo_title": "Page Links: Jump to Repeats, D.S. and Coda | Music Folder",
 "description": "Create Page Links in Music Folder to jump from a D.S., D.C. or repeat sign straight to the segno, coda or earlier page, then tap Back to return.",
 "intent": "general",
 "intent_note": "Musicians frustrated by flipping back for repeats, D.S. al Coda or D.C. in a PDF, and users looking for how to set up or remove a link.",
 "searches": [
  "repeat",
  "d.s.",
  "dal segno",
  "d.c.",
  "da capo",
  "coda",
  "segno",
  "go back to page",
  "jump",
  "link pages",
  "hyperlink",
  "navigation"
 ],
 "availability": [],
 "related": [
  "turn-pages",
  "add-text-symbols-and-shapes",
  "use-performance-mode",
  "turn-pages-hands-free"
 ],
 "feature_link": {
  "href": "/features/sheet-music-reader",
  "text": "the Sheet Music Reader"
 },
 "documents": [
  "PDF Reader/ScoreLink.swift",
  "PDF Reader/ScoreLinkNavigator.swift",
  "PDF Reader/ScoreLinkMarkerLayer.swift",
  "PDF Reader/PageLinkSetupController.swift",
  "PDF Reader/PageLinksListViewController.swift",
  "Services/PageLinkService.swift",
  "R49"
 ],
 "verified": "76048e78",
 "differs_from_4_2": null,
 "shots": [
  {
   "id": "page-links-review",
   "kind": "screen",
   "device": "ipad",
   "orientation": "portrait",
   "state": "Sicilienne after following a page link from the To Coda sign: the Coda, with the Back to p. 1 button at the bottom.",
   "alt": "Sicilienne after following a page link to the Coda, with a Back to p. 1 button at the bottom of the page.",
   "caption": null,
   "reuse": "reader-page-links-ipad.jpg"
  }
 ],
 "open_questions": []
}
---
A Page Link takes you from one place in a piece to another with one tap, so a D.S., a D.C. or a repeat back to an earlier page no longer means paging back by hand. You set the link up once. After that, a small marker sits next to the jump, you tap it when you get there, and the reader shows the place you're going to. A Back button then takes you back to where you jumped from.

## Create a link

1. Open the piece and choose **⋯ › Page Links**.
2. Tap **Add Link**.
   The first time, a short introduction appears; tap **Start**.
3. Go to the page where the jump starts and tap the exact spot, such as the printed D.S. or To Coda.
   The bar at the top reads "Tap where to jump from", and a **JUMP FROM** tag marks your spot.
4. Swipe to the page you want to land on and tap the spot, such as the segno or the coda.
   A **JUMP TO** tag marks it. If you tapped the wrong spot on the first page, tap {sf:chevron.backward} to go back a step.
5. Check the review. It shows the pages the link connects; tap **Change From** or **Change To** to choose a different spot.
6. Tap **Create Link**.
7. Tap **Test Link** to try it, **Add Another** to make another link, or **Done**.

While you set up a link, the reader's own toolbar is replaced by the Page Links bar, which shows the step you're on and the page. To stop without saving, tap {sf:xmark} or press Escape. Nothing is saved until you tap **Create Link**.

If you've already placed a symbol on the page with Add Symbol, such as a D.S. sign, you can tap the symbol itself in step 3 or 4, and the link uses it.

## Jump with a link

When you reach the start of the jump, tap the orange {sf:arrow.up.right.square} marker beside it. The reader jumps to the destination page, and a ring briefly highlights where to start playing. Markers are placed in empty space near the spot, away from the notes where possible.

After a jump, a **Back to p.** button (for example, "Back to p. 4") appears at the bottom of the page for a few seconds. Tap it to return to exactly where you jumped from. It disappears when you turn the page. With a keyboard, press Command-[ while it's showing.

{shot:page-links-review}

Links work in Performance Mode, in set lists and in Planning Center plans. In a set list, a link only jumps within the pages of that piece (or that section) in the set.

## Let the pedal follow a link

If you turn pages with a pedal, you can have the next forward turn on the link's page make the jump for you, so you don't have to reach for the screen. Turn on **Pedal follows this link** in the review step, or touch and hold the link in the Page Links list and choose **Pedal Follows Link**.

The pedal follows each link once per pass through the piece, so a repeat can't send you round in a loop. Turning back never follows a link.

## Edit or remove links

Choose **⋯ › Page Links** (Shift-Command-L with a keyboard) to see every link in the piece, listed by the pages they connect.

- Tap a link to edit it.
- Swipe left on a link and tap **Remove Link**.
- Touch and hold a link for **Test Link**, **Edit Link**, **Pedal Follows Link** and **Remove Link**.

If a link's destination has been removed, the list says so; edit the link to choose a new place.

Page Links are saved with your annotations, so they're yours: they sync to your other devices with iCloud and are included in your backups, but they aren't shared with collaborators in a shared folder or set list.

Note: Page Links work on PDF pages. They aren't available on chord charts or set-list pages such as an intermission; in those places the menu item says "Not available on this page".
