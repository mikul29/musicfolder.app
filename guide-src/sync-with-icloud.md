---
{
 "slug": "sync-with-icloud",
 "h1": "Sync with iCloud",
 "seo_title": "Sync Sheet Music Between iPhone, iPad and Mac | Music Folder",
 "description": "How Music Folder keeps your library the same on iPhone, iPad and Mac with iCloud: turning sync on, the first sync, and what stays on each device.",
 "intent": "existing",
 "intent_note": "Users with more than one device who want the same music everywhere, or who just got a new iPad and want their library on it.",
 "searches": [
  "icloud sync",
  "cloudkit",
  "sync devices",
  "new ipad",
  "second device",
  "transfer library",
  "move music to new device",
  "offline"
 ],
 "availability": [
  {
   "kind": "requires",
   "text": "Requires an iCloud account, signed in with the same Apple Account on each device."
  }
 ],
 "related": [
  "music-isnt-syncing",
  "back-up-and-restore-your-library",
  "library-looks-empty-after-reinstalling",
  "use-music-folder-on-a-mac"
 ],
 "feature_link": null,
 "documents": [
  "App/AppDelegate.swift",
  "App/AccountView.swift",
  "Data/CloudKitImportMonitor.swift",
  "App/EmptyStateView.swift",
  "Data/SongMetadataStore.swift",
  "Data/SongAudioStore.swift",
  "Data/BackupStore.swift",
  "Planning Center/PCOKeychain.swift",
  "Data/SampleLibrary.swift"
 ],
 "verified": "76048e78",
 "differs_from_4_2": null,
 "shots": [],
 "open_questions": [
  "The Important note says that turning iCloud off for Music Folder, or signing out of iCloud, removes the synced library from that device and that changes not yet uploaded can be lost. This comes from the 2026-07 support investigation (NSPersistentCloudKitContainer purges its store when the account goes away), not from app code. Please confirm the wording before publishing. (App/AppDelegate.swift)"
 ]
}
---
Music Folder syncs your library through iCloud, so the same music, folders and set lists appear on your iPhone, iPad and Mac. There's no separate account to create: sync uses the Apple Account each device is signed in to. Signing in inside the app (in Account) only adds your name and photo; it doesn't affect sync.

## What syncs

- Your music: PDFs, chord charts and each piece's details
- Sections, folders, set lists and tags
- Notes and annotations, including annotation layers
- Settings for each piece, such as a chart's transposition and crop margins
- Practice history and the list of recently opened pieces

Changes made on one device usually reach the others shortly afterward, as long as both are online. The app works offline, and changes you make without a connection upload when the device is back online.

## Turn on sync

1. On each device, make sure you're signed in to iCloud with the same Apple Account (in Settings, tap your name at the top).
2. In Settings, tap your name, then **iCloud**. In the list of apps that use iCloud, check that Music Folder is turned on. You may need to tap **Show All** or **See All** to find it.
3. Open Music Folder, then open Account: tap your picture or initials at the top of Home, or, where the app shows a sidebar, your name or **Account** at the bottom of it.
4. Under **Library & Sync**, check that **iCloud Sync** says **On**.

On a Mac, the iCloud settings are in System Settings: click your name, then **iCloud**.

iCloud Drive doesn't have to be on for your library to sync. It is needed for two things: recordings attached to your pieces sync to your other devices only through iCloud Drive, and backups are saved to iCloud Drive when it's on (otherwise they stay on the device and are deleted with the app).

## What the iCloud Sync status means

- **On**: the library is syncing.
- **Paused**: the app is set up to sync, but the iCloud account isn't available right now, for example because you're signed out of iCloud or iCloud is turned off for Music Folder.
- **Off**: this device isn't syncing. If you've just signed in to iCloud, close Music Folder completely and open it again.

Important: If you turn off iCloud for Music Folder or sign out of iCloud, the system removes the synced library from that device. It downloads again when you turn iCloud back on with the same Apple Account, but changes that hadn't finished uploading can be lost. Make a backup first (see [Back up and restore your library](/guide/back-up-and-restore-your-library)).

## The first sync on a new device

1. Sign in to iCloud on the new device with the same Apple Account as your other devices.
2. Install Music Folder and open it.
3. Leave the app open, ideally on Wi-Fi, while your library downloads.

Your music appears as it arrives, and a large library can take a while, especially the PDFs. Avoid adding the same music again on the new device while it downloads, or you'll end up with two copies.

If a device that already had your music downloads the library again (for example after an app update), the Music, Folders and Set Lists screens show **Restoring Library** instead of an empty list. Leave the app open until it finishes, and don't delete or reinstall the app in the meantime. After a reinstall this message doesn't appear, because the app no longer knows it had a library; see [My library looks empty after reinstalling](/guide/library-looks-empty-after-reinstalling).

## What stays on each device

- The two examples in Account › Support › Examples.
- Your Planning Center connection. Connect on each device where you want to see your church's songs and plans.
- Most preferences, such as those under **Preferences** in Account and your chord chart formatting defaults.

Folders and set lists that other people share with you sync through iCloud too, separately from your own library. See [Join a shared folder or set list](/guide/join-a-shared-folder-or-set-list).

## Sync isn't a backup

Sync copies every change to all your devices, deletions included. If you delete a piece by mistake, it's deleted everywhere. Keep backups so you can get it back. Your library also counts toward your iCloud storage; if that storage is full, changes stop uploading until you free up space or add more.
