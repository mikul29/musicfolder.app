---
{
 "slug": "create-and-edit-a-set-list",
 "h1": "Create and edit a set list",
 "seo_title": "Make a Set List for a Gig or Service | Music Folder",
 "description": "Create a set list in Music Folder, add whole pieces or single sections, drag them into order, and add music to a set list from anywhere in the app.",
 "intent": "existing",
 "intent_note": "Musicians putting together the running order for a concert, gig, rehearsal or worship service, and existing users looking for how to add, reorder or remove pieces.",
 "searches": [
  "setlist",
  "running order",
  "program",
  "order of service",
  "gig list",
  "reorder songs",
  "add song to set list",
  "repeat a song",
  "playlist"
 ],
 "availability": [],
 "related": [
  "add-pages-and-timing-to-a-set-list",
  "play-a-set-list",
  "add-sections-to-a-book",
  "share-a-folder-or-set-list"
 ],
 "feature_link": {
  "href": "/features/set-lists",
  "text": "Set Lists"
 },
 "documents": [
  "Set Lists/Add Set List/SetListDetailsViewController.swift",
  "Set Lists/Set List View/SetListView.swift",
  "Set Lists/Songs View/SetListViewSongs.swift",
  "Set Lists/Songs View/SetListLibraryPane.swift",
  "Set Lists/Songs View/SetListAddSheetViewController.swift",
  "Shared UI/AddToSetListMenu.swift",
  "Services/SetListTargets.swift",
  "Services/SetListSections.swift",
  "R2",
  "R4",
  "R7",
  "R12",
  "R55",
  "R60"
 ],
 "verified": "76048e78",
 "differs_from_4_2": "On iPhone, + in a set list now opens the Add to Set List sheet (the iPad pane at full width, with Undo after each add and a ✓ that adds another copy) instead of the old picker. New Set List has a Shared Set List switch.",
 "shots": [
  {
   "id": "setlist-drag-reorder",
   "kind": "clip",
   "device": "ipad",
   "orientation": "landscape",
   "state": "Spring Recital: the third piece dragged to first place.",
   "alt": "A piece being dragged from third to first place in a set list's run sheet on iPad, after which the numbers update.",
   "caption": null,
   "reuse": null
  }
 ],
 "open_questions": []
}
---
A set list puts pieces in the order you'll play them for a concert, gig, rehearsal or service. It only points to music in your library, so removing a piece from a set list, or deleting the whole set list, never deletes the music itself.

## Create a set list

1. In the Library, open **Set Lists**.
2. Tap {sf:plus} **New Set List**.
3. Type a name. To give the set list a date, turn on **Date** and pick the day.
4. Tap {sf:checkmark} **Create**.

The new set list opens with adding already started, so you can pick the first pieces right away. Names don't have to be unique; the date tells two lists called "Sunday Service" apart.

Note: The **Shared Set List** switch in the same form creates a set list other people can edit with you. Sharing needs Premium for everyone taking part and has its own guide: [Share a folder or set list](/guide/share-a-folder-or-set-list).

To rename a set list or change its date later, open it and tap **Edit**, or touch and hold it on the Set Lists screen and choose **Edit**.

## Add pieces

Tap {sf:plus} in the set list. What opens depends on how much room there is.

**On iPad and Mac** (a full-size window), the **Add to Set List** pane opens beside the set list:

1. Search by title, section or composer, or narrow the list with the Filter button in the search field.
2. Tap {sf:plus} next to a piece to add it to the end of the set list. A piece that's already in the set shows {sf:checkmark} instead, and "In set ×2" when it's there more than once.
3. To add a single section instead of the whole piece, tap the piece (or the section count next to it) to list its sections, then tap {sf:plus} next to the section.
4. When you're done, tap {sf:checkmark} at the top of the screen, where {sf:plus} was.

You can also drag a piece from the pane into the set list to drop it at an exact spot. To fill in after a particular piece, touch and hold that piece in the set list and choose **Add Piece After This…**. The pane then reads "Adding after" with the piece's name; tap the {sf:xmark} in that banner to go back to adding at the end.

**On iPhone** (and in a narrow iPad window), the **Add to Set List** sheet opens:

1. Tap a piece, or its {sf:plus}, to add it to the end of the set list. A confirmation appears with **Undo**.
2. Tapping a piece that has sections lists its sections instead, so you can add one on its own; the piece's {sf:plus} still adds the whole piece.
3. Tap {sf:checkmark} **Done**, or swipe the sheet down, to keep what you added. {sf:xmark} **Cancel** asks whether to discard the pieces you added in this sheet and removes them if you choose **Discard**.

The **Pages** segment, next to **Music** at the top of the pane or sheet, adds intermissions, announcements and notes between pieces. See [Add pages and timing to a set list](/guide/add-pages-and-timing-to-a-set-list).

## Play the same piece more than once

A piece can appear in a set list as many times as you need, for a reprise or a song that opens and closes the night. On iPhone, tap the {sf:checkmark} next to a piece that's already in the set to add another copy. On iPad and Mac, the {sf:checkmark} in the pane takes the last copy back out, so drag the piece into the set list instead. Removing one copy later removes only that one.

## Reorder pieces

Touch and hold a piece, then drag it to its new place. You can also touch and hold a piece and choose **Move Up** or **Move Down** from its menu.

{shot:setlist-drag-reorder}

## Remove a piece

Swipe left on the piece and tap {sf:trash}, or touch and hold it and choose **Remove from Set List**. Only that entry goes; the music stays in your library and in any other set lists.

## Add to a set list from anywhere

You don't have to open a set list to add to it. In your music list or a folder, touch and hold a piece and choose **Add to Set List**. In the reader, it's in the **⋯** menu. In Select mode, **Add to Set List** in the toolbar adds every selected piece at once.

The menu starts with **New Set List…**, then lists up to five set lists: dated ones from today on (soonest first), then the rest. **All Set Lists…** appears when you have more. A checkmark marks set lists that already hold the piece; choosing one of them still adds it again. The piece goes to the end of the set list, you stay where you are, and a short confirmation offers **Open**.

In the reader, when the page on screen belongs to a section, the menu asks first whether to add **Current Section** or **Entire Music**.

## Sort and delete set lists

On the Set Lists screen, tap **⋯** and choose **Sort By**. **Date** groups set lists into Upcoming, Past and No Date; **Title** sorts by name; **Manual** lets you drag them into your own order. **Hide Past Set Lists** in the same menu keeps old gigs out of the way.

To delete a set list, swipe left on it, or touch and hold it and choose **Delete**. The music in it isn't deleted.
