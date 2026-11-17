---
{
 "slug": "work-together-in-a-shared-folder-or-set-list",
 "h1": "Work together in a shared folder or set list",
 "seo_title": "Work Together in a Shared Folder | Music Folder",
 "description": "How edits reach everyone in a Shared Folder or Set List, what happens while you perform or are offline, and how to restore removed music.",
 "intent": "existing",
 "intent_note": "A member or owner of a Shared Folder or Shared Set List who wants to know when changes arrive, whether the music works offline at a gig, and how to undo a removal or a replaced PDF.",
 "searches": [
  "sync shared music",
  "changes not showing",
  "offline gig",
  "ready offline",
  "recently removed",
  "restore deleted piece",
  "previous version",
  "undo replaced pdf",
  "edits couldn't be sent",
  "update available",
  "conflict"
 ],
 "availability": [
  {
   "kind": "premium",
   "text": "Shared folders and set lists need Premium for everyone taking part."
  }
 ],
 "related": [
  "share-a-folder-or-set-list",
  "join-a-shared-folder-or-set-list",
  "use-performance-mode",
  "edit-or-delete-a-piece"
 ],
 "feature_link": {
  "href": "/features/sharing",
  "text": "sharing in Music Folder"
 },
 "documents": [
  "Shared UI/SharedUpdateLineView.swift",
  "Sharing/IncomingChangeGate.swift",
  "Sharing/SharedCollectionStatus.swift",
  "App/SharedCollectionStatusUI.swift",
  "Sharing/SharedRecentlyRemoved.swift",
  "Sharing/RecentlyRemovedOverview.swift",
  "App/RecentlyRemovedViewController.swift",
  "Songs/Song View/PreviousVersionViewController.swift",
  "Sharing/PreviousVersion.swift",
  "Sharing/SharedUnsentEdits.swift",
  "App/UnsentEditsViewController.swift",
  "Shared UI/CrossingSheet.swift",
  "Sharing/PieceLinks.swift",
  "Sharing/SharedMergeNotices.swift",
  "App/AccountView.swift",
  "R73",
  "R74",
  "R79",
  "R82",
  "R83",
  "R90",
  "R102",
  "R103",
  "R106",
  "R107",
  "R110",
  "R111",
  "R112",
  "R114",
  "R145"
 ],
 "verified": "76048e78",
 "differs_from_4_2": "All new in 4.3: changes to a piece you're reading or performing wait for you to tap Show, removed pieces go to Recently Removed instead of disappearing, replaced PDFs and chord charts keep a Previous Version for 30 days, edits the server refuses are kept for you to save, and each shared folder or set list shows its status, including Ready offline.",
 "shots": [],
 "open_questions": [
  "Previous Version for a piece that lives only in a Shared Set List: the menu item exists only in the song reader (SongPDFView.previousVersionMenuElement); set-list playback (PDFViewInSetList) has none. The guide routes through Library › Music with the Source filter set to the Shared Set List (SharedPieces.sourceOptions lists every listed collection, set lists included; SongListScreen opens the song reader). Confirm on a device that a shared set list's piece opens in the song reader from there and shows Previous Version. Songs/Song View/SongPDFView.swift, App/SharedPieceActions.swift."
 ]
}
---
In a Shared Folder or Shared Set List, the owner and members who can make changes edit the same music, and iCloud sends their changes to everyone. Here's how adding and editing works, when changes arrive on your devices, what happens while you read, perform or play offline, and how to get back removed or replaced music.

## Add and edit music for everyone

If you're the owner or can make changes, you work in a shared folder or set list just like in your own:

- In a Shared Folder, tap {sf:plus} to add music from **Files**, **Photos**, **Scan Sheet Music** or **New Chord Chart**, or choose **Add from My Library** to copy pieces you already have.
- In a Shared Set List, tap {sf:plus} (or **⋯ › Add from My Library…**) to copy pieces in from your library. Drag rows to reorder, and add set-list pages as in any set list.
- From your own library, touch and hold a piece (or tap **⋯** in the reader) and choose **Add to Shared Folder** or **Add to Shared Set List**, then pick one.
- Edit details, chord charts, sections and pages as usual.

Adding a piece from your library makes a copy for the group, and your notes, markings and recordings come along privately. If the piece is already there, the menu shows **Already Added** under that folder or set list, and choosing it asks before adding a second, separate copy.

The shared copy and your library piece don't update each other. To bring changes across on purpose, open the piece's details and use **Versions**, which can update either one from the other and copy your annotations or recordings.

## When changes arrive

Changes are sent when you're online and arrive on other devices once they're online too. To check for changes now, pull down on the shared folder or set list. Opening it and returning to the app also check.

If two people change the same thing at about the same time, the most recent change is kept, and the person whose change was replaced sees a short notice saying who changed what. If two people replace the same PDF at about the same time, both are kept: the newer one is shown and the other is under **Previous Version** for 30 days.

## Changes while you're reading or performing

Nothing changes under you while you play. If someone updates a piece you have open in the reader, the page stays as it is and a line at the bottom says "Updated version available". Tap **Show** to load the new version (on the same page, if that page still exists), or keep playing; the update is applied when you close the piece.

In Performance Mode the line is hidden until you leave it. While you play a set list, changes to its pieces and to the set list itself wait until you close it. If a piece is removed while it's open, it stays open until you close it.

## Use shared music offline

Shared music downloads to your device automatically, so it opens without a connection. A status line appears at the top of the shared folder or set list only when something needs attention:

- "Can't reach iCloud" means you're offline. If it adds "Ready offline", every piece is on this device.
- "3 pieces not downloaded yet" means some music hasn't arrived. Tap the line to download it.
- "Sending 2 changes" means your edits are waiting to go out. They're sent when you're back online.
- "Owner's iCloud is full" means your changes wait until the owner has iCloud storage again.

A shared piece that hasn't downloaded yet opens as "Not downloaded yet" with a **Download** button. Before a performance, open the folder or set list while you're online and check that no "not downloaded yet" line is left.

## Remove and restore music

If you can make changes, deleting a piece in a Shared Folder (swipe left on it, or touch and hold it and choose **Delete**) removes it for everyone. The app asks first and reminds you that your personal copies aren't affected. Removed pieces and sections go to **Recently Removed**, where they stay until someone restores them or the owner deletes them permanently. Nothing is deleted automatically.

Removing an entry from a Shared Set List (touch and hold it, then choose **Remove from Set List**) is different: it takes the entry out of the set list for everyone and doesn't go to Recently Removed.

To open Recently Removed:

- In a Shared Folder, tap **⋯**, then **Recently Removed**.
- For all your shared folders and set lists, open Account (tap your picture or initials at the top of Home, or on iPad with the sidebar, your name at the bottom of the sidebar), then tap **Recently Removed** under Library & Sync.

Each row says who removed it and when. Tap a row to preview it. The owner and members who can make changes can restore: swipe left on a row (or touch and hold it) and choose **Restore Piece** or **Restore Section**, or tap **Select** to restore several at once. A restored piece comes back with its sections and any edits made in the meantime. View only members can see the list but not restore.

Only the owner can delete permanently, and only items removed more than 30 days ago: use **Delete Permanently** on an item or **Clear Older Than 30 Days**. Recently Removed also lists a shared folder or set list you deleted for everyone. **Restore Folder** or **Restore Set List** brings it back as your own private copy; members don't get access back, but you can share it again.

## Restore a previous version of a shared piece

When the PDF or chord chart of a shared piece is replaced or changed, the earlier one is kept for 30 days.

1. Open the piece in the reader. For a piece in a Shared Set List, go to **Library › Music**, tap the Filter button in the search field, choose **Source** and the set list, then open the piece from there. (Playing the set list doesn't offer Previous Version.)
2. Tap **⋯**, then **Previous Version**. It only appears while an earlier version is kept.
3. Look through the earlier version. If the piece has both a PDF and a chord chart, switch between them at the top.
4. To bring it back, tap **Restore** and confirm. The current version becomes the previous one, so you can switch back.

The owner and members who can make changes can restore; view only members can look. If the earlier PDF isn't on your device and you're offline, you see "Available when you're online." Pieces in your own library don't keep earlier versions this way. The one exception: when you update a library piece with **Versions**, its earlier version is kept for 30 days and shows under **⋯ › Previous Version** in the reader.

## Edits that couldn't be sent

Sometimes iCloud refuses an edit for good, for example because the owner changed you to view only, the piece was removed, or the shared folder or set list no longer exists. Your edit isn't lost. A line under the header says how many edits couldn't be sent; tap **Review** to see them.

For each one you can choose **Save as My Library Piece** (or **Save as My Set List**) to keep your version as your own, or **Discard** to delete it from this device. The shared version stays as it is either way. If the shared folder or set list is gone, find them in Account under Library & Sync, in **Edits That Couldn't Be Sent**.
