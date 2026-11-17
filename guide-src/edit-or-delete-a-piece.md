---
{
 "slug": "edit-or-delete-a-piece",
 "h1": "Edit or delete a piece",
 "seo_title": "Edit or Delete a Piece of Music | Music Folder",
 "description": "Change a piece's title, composer, key, tempo, time signature, duration, folders and tags in Music Folder, or delete it and see which set lists it leaves.",
 "intent": "existing",
 "intent_note": "Existing users who want to fix a title, add a key or tempo, tag music, or remove a piece safely.",
 "searches": [
  "rename",
  "change title",
  "composer",
  "key",
  "bpm",
  "tempo",
  "time signature",
  "duration",
  "tags",
  "delete song",
  "remove piece",
  "edit details",
  "metadata"
 ],
 "availability": [],
 "related": [
  "organize-rotate-and-crop-pages",
  "add-sections-to-a-book",
  "find-music-with-search-and-filters",
  "back-up-and-restore-your-library"
 ],
 "feature_link": null,
 "documents": [
  "Shared UI/AddSongFormViewController.swift",
  "Services/AddMusicFormLayout.swift",
  "Shared UI/AddMusicTheme.swift",
  "Shared UI/SongTagsEditorViewController.swift",
  "Shared UI/DurationPickerView.swift",
  "App/LibraryLandingView.swift (Rename Tag / Delete Tag)",
  "Shared UI/SongListViewController.swift (songMenuChildren, deleteConfirmation, selection toolbar)",
  "Groups/Songs View/GroupsViewSongs.swift (Delete Piece, Remove from Folder)",
  "Services/BookmarkRemovalConfirmation.swift (DocumentDeleteConfirmation)",
  "Services/SongLibraryService.swift (deleteSong, deletionImpact)",
  "PDF Reader/PDFReaderToolbar.swift (SongEditActions)",
  "R38",
  "R62",
  "R65",
  "R94",
  "R107"
 ],
 "verified": "76048e78",
 "differs_from_4_2": "4.3 adds a Versions section to Edit Music for pieces linked to a copy in a shared folder or set list, and Delete on a piece inside a shared folder removes it from the folder for everyone (it goes to Recently Removed) instead of deleting it from your library.",
 "shots": [
  {
   "id": "edit-music-form",
   "kind": "crop",
   "device": "ipad",
   "orientation": "portrait",
   "state": "Edit Music for Mozart's Quartet in D, K. 155 with Details expanded.",
   "alt": "Edit Music for a Mozart quartet with Details open: tempo, time signature, key, duration and Display as Book, followed by Folder, Tags, Organize Pages and Add Sections.",
   "caption": null,
   "reuse": null
  }
 ],
 "open_questions": [
  "Replacing a piece's PDF: the form's 'Replace Sheet Music' button title still exists in code, but in the 4.3 layout the add-file row only shows when there's no PDF. The guide doesn't describe replacing a PDF; confirm whether there is a supported way (other than Organize Pages) to swap the whole PDF of a library piece."
 ]
}
---
You can change a piece's details at any time, or delete a piece you no longer need. Details such as key, tempo and tags make your library easier to search and filter, and duration adds up your set times.

## Open Edit Music

Touch and hold the piece in your library (or right-click it on a Mac) and choose **Edit Details**. In the reader, choose **⋯ › Edit Details**, or press Command-I on a keyboard. The **Edit Music** form opens; the checkmark becomes available once you change something.

{shot:edit-music-form}

## Change the details

- **Title** and **Composer** are at the top. Each title in your library must be unique, and titles can't contain the † character. Renaming a piece keeps it in its set lists under the new name.
- **Details**: tap to show **Tempo**, **Time Signature**, **Key**, **Duration** and **Display as Book**. Tap a row to open its picker under it. Duration is minutes and seconds; set lists use it to add up their running time. **Display as Book** shows the piece as a book in your lists (see [Add sections to a book](/guide/add-sections-to-a-book)).
- **Folder**: choose one or more folders for the piece. See [Organize music in folders](/guide/organize-music-in-folders).
- **Tags**: tap to see every tag in your library and tap the ones that apply, or type a new one in **Add New Tag…**. Tags are free-form labels, such as "christmas" or "audition."
- **Pages**: **Organize Pages** reorders, rotates, adds and removes pages. See [Organize, rotate and crop pages](/guide/organize-rotate-and-crop-pages).
- **Sections**: mark the pieces inside a book. See [Add sections to a book](/guide/add-sections-to-a-book).
- **Chord Chart** and **Add Recording**: see [Create a chord chart](/guide/create-a-chord-chart) and [Play along with recordings](/guide/play-along-with-recordings).

Tap the checkmark to save. To leave without saving, tap {sf:xmark} and then **Discard Changes**.

When a piece is linked to a copy in a shared folder or set list, the form also has a **Versions** section for updating one copy from the other. See [Work together in a shared folder or set list](/guide/work-together-in-a-shared-folder-or-set-list).

### Rename or delete a tag everywhere

On iPhone, your tags are listed on the **Library** screen. Touch and hold a tag and choose **Rename Tag** or **Delete Tag** to change it in every piece that uses it. Tap a tag to see its pieces.

## Delete a piece

1. Touch and hold the piece and choose **Delete**. In list view you can also swipe left on it and tap {sf:trash}.
2. Read the confirmation. If the piece, or any of its sections, is in a set list, the alert names each set list with its date.
3. Tap **Delete**.

To delete several pieces, choose **⋯ › Select**, tap the pieces, and then tap {sf:trash} in the toolbar.

Deleting a piece removes it from your library on all your devices, together with its sections, notes, markings and recordings. It also leaves every folder and set list it was in; the other entries in those set lists stay in order. Your practice history is kept. If another piece in your library still uses the same notes or recordings, they stay with that piece.

There's no Recently Deleted for your own pieces. If you might want a piece back, make a backup first; see [Back up and restore your library](/guide/back-up-and-restore-your-library).

### Inside a folder

In a folder, touch and hold a piece and choose **Remove from Folder** to take it out of that folder only; it stays in your library. **Delete Piece** deletes it from your library and from every folder.

### In a shared folder

A piece in a shared folder belongs to the group. Deleting it there removes it from the folder for everyone and moves it to Recently Removed, where it can be restored; your own notes, markings and recordings aren't affected. See [Work together in a shared folder or set list](/guide/work-together-in-a-shared-folder-or-set-list).
