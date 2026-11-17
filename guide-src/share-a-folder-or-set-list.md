---
{
 "slug": "share-a-folder-or-set-list",
 "h1": "Share a folder or set list",
 "seo_title": "Share Sheet Music and Set Lists | Music Folder",
 "description": "Turn a folder or set list into a Shared Folder or Shared Set List, invite members, choose who can edit, and stop sharing when you're done.",
 "intent": "existing",
 "intent_note": "A band leader, music director or teacher who wants everyone working from the same music and set order, and wants to know what sharing does to their own library.",
 "searches": [
  "collaborate",
  "collaboration",
  "share with band",
  "invite members",
  "shared folder",
  "shared set list",
  "permissions",
  "view only",
  "stop sharing",
  "move to new sharing",
  "manage sharing",
  "share link"
 ],
 "availability": [
  {
   "kind": "premium",
   "text": "Sharing needs Premium, for you and for everyone you invite."
  },
  {
   "kind": "version",
   "text": "Everyone you invite needs Music Folder 4.3 or later."
  },
  {
   "kind": "requires",
   "text": "Needs an iCloud account and an internet connection to start sharing."
  }
 ],
 "related": [
  "join-a-shared-folder-or-set-list",
  "work-together-in-a-shared-folder-or-set-list",
  "send-a-copy-or-print",
  "free-and-premium"
 ],
 "feature_link": {
  "href": "/features/sharing",
  "text": "sharing in Music Folder"
 },
 "documents": [
  "App/CollectionShareMenu.swift",
  "App/SharedFolderActions.swift",
  "App/SharedSetListActions.swift",
  "Sharing/SharedShareManager.swift",
  "Sharing/NewSharedCreation.swift",
  "Sharing/SharedConversion.swift",
  "Sharing/SharedCollectionStatus.swift",
  "Sharing/SharedCollectionPlan.swift",
  "App/LegacyMoveActions.swift",
  "Sharing/LegacyMove.swift",
  "Premium/CollaborationAccess.swift",
  "App/WhatsNewViewController.swift",
  "R69",
  "R73",
  "R74",
  "R86",
  "R96",
  "R97",
  "R99",
  "R100",
  "R126",
  "R129",
  "R136",
  "R137"
 ],
 "verified": "76048e78",
 "differs_from_4_2": "Sharing was rebuilt in 4.3. The separate Collaborate button and Manage Collaboration are replaced by one Share Folder / Share Set List menu with Collaborate and Send Copy. A shared folder or set list now holds its own copies of the pieces, so your library pieces never change when members edit. New Folder and New Set List have a Shared switch. Folders and set lists shared with 4.2 keep working for 4.2 members but have to be moved with Move to New Sharing, and members invited again. Everyone needs 4.3 or later.",
 "shots": [
  {
   "id": "share-folder-menu",
   "kind": "crop",
   "device": "ipad",
   "orientation": "landscape",
   "state": "Library › Folders with the demo library. A folder that isn't shared yet (the band folder) is touched and held, and its Share Folder submenu is open, showing Collaborate (subtitle “Work together with live updates”) and Send Copy (subtitle “Send files without live updates”). Crop to the menu and the folder cover.",
   "alt": "A folder's menu with Share Folder open, offering Collaborate (Work together with live updates) and Send Copy (Send files without live updates).",
   "caption": null,
   "reuse": null
  }
 ],
 "open_questions": [
  "Permission names: the app never names the roles itself; they appear only in Apple's sheets (UIActivityViewController with CKAllowedSharingOptions [.readOnly, .readWrite] × [.specifiedRecipientsOnly, .anyoneWithLink], and UICloudSharingController). The guide uses Apple's labels \"Can make changes\" / \"View only\" and \"Anyone with the link\". Confirm the exact wording on an iOS 17 and an iOS 26 device. Sharing/SharedShareManager.swift, App/SharedFolderActions.swift.",
  "Move to New Sharing: verified in code that once a move reaches converted, LegacyMoves.hideMovedOriginals hides the original on every device, and the ONLY routes to the move screen (and its Stop Old Sharing…) are the original's own context menu (\"Moving to New Sharing\") and Collaborate on the original (routeToMove). Nothing else opens LegacyMoveViewController and nothing un-hides the original (Account ▸ Moved Shares was removed 2026-11-16). So after a completed move the owner has no way to stop the old 4.2 sharing. The guide gives no steps for stopping it. Owner: is this intended, or does a route need restoring? App/LegacyMoveActions.swift, App/LegacyMoveViewController.swift.",
  "Owner's other devices still on 4.2: Collaborate removes the original library folder / set list (GroupLibraryService.deleteGroupKeepingSongs via LibraryConversionAdapter.hideOriginal) once the server verifies the copy; that delete syncs, so a 4.2 device should see the folder disappear while its pieces stay in All Music. The guide only says to update other devices. Confirm on a 4.2 device before saying more."
 ]
}
---
You can share a folder or set list with your band, choir or students so that everyone works from the same music in the same order. A Shared Folder or Shared Set List lives in iCloud: each member opens it on their own iPhone, iPad or Mac, and members you allow can add and change music for everyone.

## Collaborate or Send Copy

Every folder and set list has one share menu, **Share Folder** or **Share Set List**, with two choices:

- **Collaborate** makes it shared, with live updates. Members join with an invitation and everyone works on the same folder or set list.
- **Send Copy** sends files without live updates, as a Music Folder file or a PDF. See [Send a copy or print](/guide/send-a-copy-or-print).

## Share a folder you already have

1. In **Library**, open **Folders**.
2. Touch and hold the folder, then choose **Share Folder › Collaborate**. You can also open the folder, tap **⋯**, then choose **Share Folder › Collaborate**.
3. If you don't have Premium yet, the Premium screen appears first. Sharing starts after you subscribe.
4. When the share sheet appears, choose how to send the invitation, for example Messages, Mail or Copy Link. See "Invite members and choose permissions" below.

{shot:share-folder-menu}

The folder stays where it was in your list. While the app copies and uploads its music, the folder shows its progress (for example "Sharing…") and can't be edited, but you can keep using the rest of the app. Once everything is in iCloud, the folder is marked as shared. If something goes wrong, the app says it couldn't share the folder and that nothing was changed, and you can tap **Try Again**.

## Share a set list

1. In **Library**, open **Set Lists**.
2. Touch and hold the set list, then choose **Share Set List › Collaborate**. You can also open the set list, tap {sf:square.and.arrow.up} **Share**, then tap **Collaborate**.
3. Send the invitation from the share sheet.

A Shared Set List keeps your order, sections, set-list pages and timing. Planning Center items can't be included; if the set list has any, the app says how many won't be included and asks you to continue before it starts.

## Create a new shared folder or set list

1. Start a new folder or set list as usual (**New Folder** or **New Set List**).
2. Turn on **Shared Folder** or **Shared Set List**. If you don't have Premium, the Premium screen appears first; closing it turns the switch off again.
3. Tap {sf:checkmark} to create it. The share sheet opens as soon as the shared copy exists, so you can invite members.

If you're offline or not signed in to iCloud, the folder or set list is created as a private one and the app tells you that you can share it when you're online.

## What happens to your music

Sharing makes copies. The shared folder or set list holds its own copy of each piece, and your original pieces stay in your library, under **All Music**, exactly as they were. When a member changes a shared piece, your library piece doesn't change, and changes you make to your library piece don't reach the group. To bring changes across on purpose, open the piece's details and use **Versions**.

Your notes, markings, recordings and other personal settings on those pieces are copied to the shared copies, but only for you. Members never see them, and you never see theirs.

A shared folder or set list uses the owner's iCloud storage, including pieces that members add.

## Invite members and choose permissions

Invitations are sent with Apple's sharing sheet, which also holds the access options. By default, only the people you invite can join; you can choose **Anyone with the link** instead. In the same options you choose what members can do (the wording is Apple's):

- **Can make changes**: add, edit and remove pieces, sections and chord charts, change a set list's order, pages and date, and restore removed music.
- **View only**: open, read, play and perform the music, add their own private markings and notes, send a copy and save pieces to their own library.

You're the owner. Only the owner can rename the folder or set list (and change a folder's color), manage members, stop sharing, delete it for everyone, and permanently delete removed music.

To invite more people, change permissions or remove someone later, touch and hold the shared folder or set list (or open it and tap **⋯**), then choose **Share Folder** or **Share Set List** › **Manage Sharing**. Inside one, you can also tap the people button in the bar at the top.

## Premium and app version

Each person you invite needs Premium too, and sees the Premium screen when they accept. If someone's Premium ends, the shared folder or set list stays in their lists and nothing is deleted; it opens again when Premium is active, and they can always leave.

Members need Music Folder 4.3 or later, and so do your own devices. Update your other iPhone, iPad or Mac to see your shared folders and set lists there.

## Folders and set lists shared with Music Folder 4.2

Sharing works differently in 4.3. A folder or set list you shared with an earlier version keeps working for members who are still on it, but it has to be moved to the new sharing, and your members need to be invited again.

1. Touch and hold the folder or set list, then choose **Move to New Sharing…**.
2. Read the message and tap **Update Sharing**.
3. When the share sheet opens, invite your members again.

Your music, sections and order are copied into a new Shared Folder or Shared Set List; nothing in the original is changed. Once the move is complete, the original no longer appears in your lists, but it stays shared with members who haven't moved yet. Members who join the new one get their own notes, markings and recordings carried over to it. Only the person who shared the original can move it.

## Stop sharing

1. Touch and hold the shared folder or set list in your list, or open it and tap **⋯**.
2. Choose **Stop Sharing**.
3. Tap **Stop Sharing** to confirm.

Members lose access, and the folder or set list stays in your list as your own, with its latest changes. Where a shared piece is still the same as your original, the folder or set list uses your original piece again; pieces the group changed or added come back as new pieces in your library. Stopping sharing in Apple's sheet, which opens from **Manage Sharing**, does the same.

**Delete for Everyone** is different: members lose access and the folder or set list moves to Recently Removed on your devices. See [Work together in a shared folder or set list](/guide/work-together-in-a-shared-folder-or-set-list).
