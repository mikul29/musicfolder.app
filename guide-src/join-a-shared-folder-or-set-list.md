---
{
 "slug": "join-a-shared-folder-or-set-list",
 "h1": "Join a shared folder or set list",
 "seo_title": "Join a Shared Folder or Set List | Music Folder",
 "description": "Accept an invitation to a Shared Folder or Shared Set List, see what you can do in it, keep your markings private, save pieces to your library, or leave.",
 "intent": "existing",
 "intent_note": "A band member, choir singer or student who received a Music Folder invitation link and wants to open the shared music and know what others can see.",
 "searches": [
  "invitation",
  "invite link",
  "accept invitation",
  "join band folder",
  "shared with me",
  "leave shared folder",
  "save to my library",
  "private annotations",
  "couldn't join"
 ],
 "availability": [
  {
   "kind": "premium",
   "text": "Joining and opening shared folders and set lists requires Music Folder Premium. You can leave one without it."
  },
  {
   "kind": "version",
   "text": "Requires Music Folder 4.3 or later and an iCloud account."
  }
 ],
 "related": [
  "work-together-in-a-shared-folder-or-set-list",
  "share-a-folder-or-set-list",
  "mark-up-music-with-apple-pencil",
  "keep-notes-on-a-piece"
 ],
 "feature_link": {
  "href": "/features/sharing",
  "text": "sharing in Music Folder"
 },
 "documents": [
  "App/SharedFolderActions.swift",
  "App/SharedSetListActions.swift",
  "Sharing/SharedShareManager.swift",
  "Shared UI/CrossingSheet.swift",
  "Sharing/SharedFolderRows.swift",
  "Sharing/SharedSetListRows.swift",
  "Sharing/SharedScreenRouting.swift",
  "Sharing/RecentlyRemovedOverview.swift",
  "App/LegacyMoveActions.swift",
  "Premium/CollaborationAccess.swift",
  "R69",
  "R73",
  "R74",
  "R85",
  "R96",
  "R112",
  "R116",
  "R134"
 ],
 "verified": "76048e78",
 "differs_from_4_2": "In 4.3, invitations come from the new Shared Folders and Shared Set Lists, and joining needs Music Folder 4.3. Save to My Library is new: you can keep your own copy of any shared piece. Leaving keeps a copy on your device in Recently Removed. If you were in a folder or set list shared with 4.2, the owner has to move it to the new sharing and invite you again; your notes, markings and recordings come along.",
 "shots": [],
 "open_questions": [
  "What a person on Music Folder 4.2 (or without the app) sees when they tap a 4.3 invitation link isn't confirmed (06-edge-cases says the 4.2 behavior is untested). The guide only says 4.3 or later is needed. App/SceneDelegate.swift, App/SharedFolderActions.swift handleInvitation.",
  "Leave: the app's confirmation does say \"Your notes and markings on N pieces will be kept for 30 days in case you rejoin.\" (SharedFolderActions.confirmLeave, line 277). leaveCollection only enqueues the zone leave; no code found that deletes the member's notes / layers after 30 days (and R110: nothing is purged automatically). The guide says they're kept in case you rejoin, without a number. Owner: should the alert drop \"for 30 days\", or is a cleanup planned?"
 ]
}
---
When your band leader, director or teacher shares a folder or set list with you, you get an invitation link by Messages, Mail or another app. Accepting it adds the Shared Folder or Shared Set List to your lists, where you can read, play and perform its music, and edit it too if the owner allows.

## Accept an invitation

1. Tap the invitation link on the iPhone, iPad or Mac where you use Music Folder.
2. Music Folder opens. If you don't have Premium, the Premium screen appears; you join once you subscribe.
3. The app says "Joined" with the folder's or set list's name and opens it.

The music downloads in the background. Until the first download finishes, the folder or set list reads "Joining…" in your list. After that it appears in **Folders** or **Set Lists** marked "Shared by" and the owner's name.

If you close the Premium screen, nothing is joined. The invitation still works: tap the link again later. If the app says "Couldn't Join", check that you're signed in to iCloud in Settings, then tap the invitation again.

You only need to accept once. Your other devices signed in to the same Apple Account get the shared folder or set list on their own.

## What you can do

The owner chooses, in Apple's sharing options, whether members **can make changes** or are **view only**.

- **Can make changes**: add, edit and remove pieces, sections and chord charts, change a set list's order, pages and date, and restore removed music.
- **View only**: open, read, play and perform everything, and add your own markings and notes. Editing options like **Edit Details** don't appear.

Everyone, whatever their permission, can send a copy of the whole folder or set list and save pieces to their own library. Only the owner can rename it, invite or remove members, or stop sharing it.

## Your markings, notes and recordings stay private

Shared pieces open in the same reader as your own music, with the same tools. Anything personal you add is yours alone: markings and annotation layers, text and symbols, notes, recordings, Page Links, cropped margins, transposition, and tempo and key settings for recordings. Other members never see them, and you never see theirs. They sync between your own devices like the rest of your library.

## Save a shared piece to your library

Saving makes your own copy of a shared piece, so you can keep it even if you leave or the owner stops sharing.

1. In the shared folder or set list, touch and hold the piece. In the reader, tap **⋯** instead.
2. Choose **Save to My Library**.
3. Choose a folder for it, or leave **Folder** set to **None**.
4. Tap {sf:checkmark}.

Your copy includes your notes, markings and recordings. The shared piece stays as it is, and the two don't update each other. Saved pieces count toward the free limits. If you've saved the same piece before, the sheet tells you when, and saving again makes a second copy.

## If you were in a folder or set list shared with Music Folder 4.2

When the owner moves an older shared folder or set list to the new sharing, they invite you again. After you join the new one, the app says it replaces the old one. Your notes, markings and recordings on the old pieces come along to the new pieces. Tap **Save to My Library** if you also want your own copy of the old one; it stays until its owner stops sharing it.

## Leave a shared folder or set list

1. Touch and hold the shared folder or set list in your list, or open it and tap **⋯**.
2. Choose **Leave**.
3. Tap **Leave** to confirm.

You can leave without Premium. Your notes and markings on its pieces are kept in case you rejoin. A copy of the music stays on this device in **Recently Removed**. To keep its pieces as your own, swipe left on it there (or touch and hold it) and choose **Save to My Library**.

If the owner stops sharing, removes you or deletes the folder or set list, the app tells you once, for example "You no longer have access to" followed by its name. The same copy is kept in Recently Removed. To find it, open Account (tap your picture or initials at the top of Home, or on iPad with the sidebar, your name at the bottom of the sidebar), then tap **Recently Removed** under Library & Sync.
