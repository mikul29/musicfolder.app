---
{
 "slug": "organize-music-in-folders",
 "h1": "Organize music in folders",
 "seo_title": "Organize Sheet Music Into Folders | Music Folder",
 "description": "Create folders for ensembles, concerts or students, choose a cover color, add and remove pieces, and delete a folder with or without its pieces.",
 "intent": "existing",
 "intent_note": "Musicians sorting a growing library by ensemble, concert, season or student.",
 "searches": ["groups", "group", "folder", "categories", "playlist", "organize library", "collection", "folder colour", "folder color", "delete folder"],
 "availability": [{"kind": "premium", "text": "Free includes 1 folder; Premium has no limit."}],
 "related": ["import-music", "find-music-with-search-and-filters", "share-a-folder-or-set-list", "create-and-edit-a-set-list"],
 "feature_link": {"href": "/features/sheet-music-organizer", "text": "the Sheet Music Organizer"},
 "documents": ["Groups/FolderEditorSheet.swift", "Services/FolderCoverColor.swift", "Groups/Groups View/GroupsView.swift (context menu, confirmDeleteGroup, addGroupTapped, groupsEmptyState)", "Groups/Songs View/GroupsViewSongs.swift (Add Existing Pieces, Remove from Folder, Delete Piece)", "Shared UI/MusicPickerViewController.swift", "Shared UI/SongListViewController.swift (makeAddToGroupMenu)", "Services/GroupLibraryService.swift (deleteGroupKeepingSongs, deleteGroupAndSongs)", "Discover/StarterGroup.swift", "Sharing/NewSharedCreation.swift", "R6", "R126"],
 "verified": "76048e78",
 "differs_from_4_2": "New Folder has a Shared Folder switch in 4.3 (4.2 had a Collaborate row in the folder sheet). Sharing an existing folder is now in its Share Folder menu.",
 "shots": [],
 "open_questions": []
}
---
Folders group your music by ensemble, concert, season, student or anything else that helps you find it. A piece can be in several folders at once without making another copy, and editing it in one place changes it everywhere.

## Create a folder

1. Open **Library**, then **Folders**. On iPad, choose **Folders** in the sidebar.
2. Tap {sf:plus}.
3. Type a name, and tap a cover color: **Black**, **Midnight**, **Forest**, **Burgundy**, **Plum**, **Slate**, **Cognac** or **Linen**.
4. To fill the folder now, tap **Add Music** and choose pieces from your library. You can also add them later.
5. Tap the checkmark (**Create Folder**).

**New Folder** also has a **Shared Folder** switch. Leave it off for a folder only you use. Turning it on creates the folder as a shared folder that you and the people you invite work on together, which needs Premium; see [Share a folder or set list](/guide/share-a-folder-or-set-list).

The free version includes 1 folder. Creating a second one shows the Premium offer.

## Add pieces to a folder

You can add pieces from either side:

- **From inside the folder**: tap {sf:plus} and choose **Add Existing Pieces**. Search or scroll, tap the pieces you want, and tap the checkmark.
- **From anywhere in your library**: touch and hold a piece and choose **Add to Folder**, then the folder.
- **From the piece's details**: in **Edit Music**, tap **Folder** and choose one or more folders.
- **While importing**: music you import with the folder's {sf:plus} menu goes straight into the folder, and so does a new chord chart you start there. See [Import music](/guide/import-music).

## Remove a piece from a folder

Open the folder, touch and hold the piece, and choose **Remove from Folder**. The piece stays in your library and in any other folders.

**Delete Piece** in the same menu is different: it deletes the piece from your library and every folder. See [Edit or delete a piece](/guide/edit-or-delete-a-piece).

## Rename a folder or change its color

1. In **Folders**, touch and hold the folder (or right-click it on a Mac) and choose **Edit**.
2. Change the name or the cover color. Tap **Music** to change which pieces it holds.
3. Tap the checkmark (**Save Changes**).

## Delete a folder

1. In **Folders**, touch and hold the folder and choose **Delete**. In list view you can also swipe left on it and tap {sf:trash}.
2. Choose **Delete Folder Only** or **Delete Folder & Pieces**.

**Delete Folder Only** removes the folder and keeps every piece in your library. **Delete Folder & Pieces** removes the folder and deletes every piece in it from your library.

Important: **Delete Folder & Pieces** deletes the pieces even if they're also in other folders or in set lists, and it removes them from those set lists without naming them first. Choose **Delete Folder Only** if you're not sure.

An empty folder offers a single **Delete Folder** button. To delete several folders, choose **⋯ › Select**, tap the folders, and tap {sf:trash}.

## Add the starter folder

When you don't have any folders yet, the Folders screen offers **Add a Starter Folder**. It creates "Classical Starters" with five public-domain pieces, downloaded from the free catalog. They count toward the 15 pieces in the free version. See [Get free sheet music](/guide/get-free-sheet-music).
