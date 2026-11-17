---
{
 "slug": "music-isnt-syncing",
 "h1": "My music isn't syncing",
 "seo_title": "Fix Music Not Syncing Between Devices | Music Folder",
 "description": "Music Folder not syncing between your iPad, iPhone or Mac? Work through these iCloud checks in order, from the sync status to storage and Apple Accounts.",
 "intent": "troubleshooting",
 "intent_note": "Existing users whose music, folders or set lists added on one device don't appear on another.",
 "searches": [
  "icloud sync",
  "not syncing",
  "sync not working",
  "missing on ipad",
  "missing on iphone",
  "sync paused",
  "icloud storage full",
  "devices not matching"
 ],
 "availability": [
  {
   "kind": "requires",
   "text": "Sync requires an iCloud account on every device."
  }
 ],
 "related": [
  "sync-with-icloud",
  "library-looks-empty-after-reinstalling",
  "back-up-and-restore-your-library",
  "work-together-in-a-shared-folder-or-set-list"
 ],
 "feature_link": null,
 "documents": [
  "App/AppDelegate.swift (CloudKit attachment gate)",
  "Data/CoreDataStack.swift (isCloudKitSyncAttached)",
  "App/AccountView.swift (AccountSyncStatus, iCloud Sync row)",
  "Data/CloudKitImportMonitor.swift",
  "App/EmptyStateView.swift",
  "Data/SongAudioStore.swift",
  "Data/BackupStore.swift",
  "Sharing/SharedCollectionStatus.swift",
  "memory: offline-icloud-support-ticket"
 ],
 "verified": "76048e78",
 "differs_from_4_2": null,
 "shots": [],
 "open_questions": [
  "AppDelegate.swift attachment gate: a store that was created without iCloud is CloudKit-attached on the NEXT launch (storeExists is true), so the guide tells people who signed in later to close and reopen the app. Owner: confirm that a library created before signing in uploads its existing pieces once the account appears (I could not verify NSPersistentCloudKitContainer's behaviour for a none-to-account change from the code).",
  "The warning that turning off iCloud for the app (or signing out) removes the synced library from the device comes from the 2026-07-08 support ticket memo (NSPersistentCloudKitContainer purge on account loss). Owner: confirm this wording is still right for 4.3."
 ]
}
---
Music Folder keeps your library in sync through your iCloud account, so the same music, folders, set lists, sections, notes and annotations appear on every iPad, iPhone and Mac signed in to that account. When something you added on one device doesn't appear on another, the cause is usually the iCloud setup on one of the devices or a first sync that hasn't finished yet. The checks below start with the most likely cause.

## Check the sync status in Account

1. Open **Account**: tap your picture or initials at the top of Home, or, where the app shows a sidebar, your name or **Account** at the bottom of it.
2. Under **Library & Sync**, look at **iCloud Sync**.

**On** means the library on this device is connected to iCloud. Continue with the checks below on the device that's missing changes, and on the device where you made them.

**Paused** means the app is set up to sync but can't use an iCloud account right now. Check that you're signed in to iCloud and that iCloud is turned on for Music Folder (see the next section).

**Off** means the library on this device isn't connected to iCloud. This happens when Music Folder was first opened before the device was signed in to iCloud. Sign in to iCloud, close Music Folder from the App Switcher, then open it again and check that **iCloud Sync** says **On**.

Note: **Sign in to Music Folder** at the top of Account only adds your name and photo. It has nothing to do with sync, which always uses the iCloud account the device is signed in to.

## Check iCloud on each device

1. Open Settings and tap your name at the top. Make sure every device shows the same Apple Account. Devices signed in to different accounts keep separate libraries.
2. Tap **iCloud** and find Music Folder in the list of apps that use iCloud (you may need to tap **Show All** or **See All**). Make sure it's turned on.
3. Make sure iCloud Drive is on. Recordings attached to your music and your backups are kept in iCloud Drive, so they won't reach your other devices without it. Your library itself syncs either way.

On Mac: open System Settings, click your name, then click **iCloud**.

Important: Don't turn off iCloud for Music Folder, or sign out of iCloud, to try to restart syncing. When the app loses access to iCloud, the synced copy of your library is removed from that device. It downloads again when you turn iCloud back on with the same Apple Account, but any changes on that device that hadn't finished uploading are lost. If you're unsure, [back up your library](/guide/back-up-and-restore-your-library) first.

## Give the first sync time

When you set up a new device or connect a library to iCloud for the first time, every piece has to upload from the device where you added it and then download on the others, PDFs included. A large library can take a while.

- Open Music Folder on the device where you added the music, so it can finish uploading.
- Keep Music Folder open on the device that's missing music, on Wi-Fi, ideally plugged in. Lists update by themselves as new music arrives.
- If a device that already had your library is downloading it again, the Music, Folders and Set Lists screens show **Restoring Library** instead of an empty list. Leave the app open until it finishes, and don't delete the app. After a reinstall this message doesn't appear; see [My library looks empty after reinstalling](/guide/library-looks-empty-after-reinstalling).

## Check your iCloud storage

Your library is stored in your iCloud account and uses your iCloud storage. When the storage is full, new changes stop uploading, and Music Folder doesn't show a separate warning for your own library. Check how much space is left in Settings › your name › **iCloud**. Free up space or choose a larger iCloud plan, then open Music Folder on the device with the new changes so they can upload.

## Update Music Folder everywhere

Install the latest version of Music Folder on every device. An older version may not show what a newer one saves, such as sections or features added in a later release.

## Shared folders and set lists

Folders and set lists you share with other musicians sync separately from your own library. Open one to see its status at the top of the screen, for example **Can’t reach iCloud**, **iCloud storage is full** or **Owner’s iCloud is full**. Pull down on the list to check for changes right away. For more, see [Work together in a shared folder or set list](/guide/work-together-in-a-shared-folder-or-set-list).

## Contact us

If your music still isn't syncing after these checks, [contact us](/contact). It helps to include:

- The devices involved and their iOS, iPadOS or macOS versions
- The Music Folder version on each device (**Account › About › Version**)
- What **iCloud Sync** says on each device
- What you added or changed, on which device, and roughly when
