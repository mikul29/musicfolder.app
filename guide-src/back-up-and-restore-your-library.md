---
{
 "slug": "back-up-and-restore-your-library",
 "h1": "Back up and restore your library",
 "seo_title": "Back Up and Restore Your Sheet Music Library | Music Folder",
 "description": "Make a backup of your Music Folder library, set up automatic backups, and restore music, folders and set lists with Add Missing Items or Replace Library.",
 "intent": "existing",
 "intent_note": "Users who want a safety copy of their library, or who lost music (deleted by mistake, new device, reinstall) and want it back.",
 "searches": [
  "backup",
  "restore",
  "export library",
  "mfbackup",
  "lost music",
  "deleted by mistake",
  "recover",
  "safety copy",
  "automatic backup"
 ],
 "availability": [],
 "related": [
  "sync-with-icloud",
  "library-looks-empty-after-reinstalling",
  "free-and-premium",
  "use-music-folder-on-a-mac"
 ],
 "feature_link": null,
 "documents": [
  "App/BackupView.swift",
  "Data/BackupStore.swift",
  "App/BackupScheduler.swift",
  "Services/BackupSchedulePolicy.swift",
  "Services/BackupRestorePlan.swift",
  "Services/LibraryRestoreService.swift",
  "Sharing/BackupFormat.swift",
  "Sharing/SharedCollectionService+Backup.swift",
  "App/MainMenu.swift",
  "Premium/PremiumGate.swift",
  "R34",
  "R68",
  "R120",
  "R122",
  "R124"
 ],
 "verified": "76048e78",
 "differs_from_4_2": "Backups now also hold the shared folders and set lists you own and your notes and markings on shared pieces. A restore brings back an owned shared folder or set list only if it no longer exists, and then as your own unshared copy.",
 "shots": [
  {
   "id": "backup-restore-screen",
   "kind": "crop",
   "device": "ipad",
   "orientation": "portrait",
   "state": "Account › Library & Sync › Backup & Restore on iPad (simulator without iCloud, so Location reads On This Device).",
   "alt": "Backup & Restore with Back Up Now, the time of the last backup, the automatic backup settings and the list of backups.",
   "caption": null,
   "reuse": null
  }
 ],
 "open_questions": []
}
---
A backup is a single file that holds your whole library, so you can get your music back if you delete something by mistake, change devices or have a problem with iCloud. iCloud sync isn't a backup: it copies deletions to every device too. Backups are free.

{shot:backup-restore-screen}

## Back up now

1. Open Account: tap your picture or initials at the top of Home, or, where the app shows a sidebar, your name or **Account** at the bottom of it.
2. Under **Library & Sync**, tap **Backup & Restore**.
3. Tap **Back Up Now**.

The line under the button shows when the last backup was made, how many pieces it holds and its size. If you sync with iCloud, it can name another of your devices, because one automatic backup covers the library for all of them.

On Mac: choose **File › Back Up Library Now** in the menu bar.

## What a backup holds

- Your music and its PDFs, chord charts, sections and details
- Folders and set lists
- Notes and annotations
- Recordings attached to your pieces (always in a backup you make with Back Up Now; optional for automatic backups)
- Practice history
- Your settings, such as tuner, metronome, reader and chart preferences
- Shared folders and set lists you own, and your notes and markings on shared pieces

Folders and set lists that other people share with you aren't included; iCloud brings those back. A shared piece that hasn't downloaded to the device is left out, and the app names it when the backup finishes. The same goes for recordings that are still only in iCloud: open those pieces' audio once on the device, then back up again.

## Automatic backups

**Back Up Automatically** is on unless you turn it off. With it on, you can choose:

- **Frequency**: **Daily** or **Weekly**.
- **Include Audio**: whether recordings go into automatic backups.
- **Keep**: **3**, **5** or **10** backups. Older automatic backups are removed once there are more than this. Backups you make with Back Up Now are never removed automatically.

An automatic backup runs shortly after you open the app when one is due, and in the background while the device is charging. It's skipped when nothing has changed since the last backup, and never runs on an empty library. If your library suddenly has less than half the pieces of the last backup, automatic backups pause until you confirm with **Back Up Now** that this is the library you want to keep.

## Where backups are saved

**Location** shows where backups go. With iCloud Drive on, they're in the Files app under **iCloud Drive › Music Folder › Backups**, so they survive losing the device. Without iCloud Drive they're under **On This Device › Music Folder › Backups**, and they're deleted if you delete the app. To keep one somewhere else, open it and tap **Save to Files…**.

## Restore from a backup

1. In **Backup & Restore**, tap a backup under **Backups**. For a backup file saved elsewhere, tap **Restore from File…** and choose it. You can also open a backup file from the Files app or AirDrop, and Music Folder opens it here.
2. Check what it holds: the device it came from and the number of pieces, folders and set lists.
3. If you also want the backup's settings, turn on **Also Restore Settings**.
4. Choose how to restore (see below).

### Add Missing Items

**Add Missing Items** adds the pieces, folders and set lists the backup has and your library doesn't. Nothing already in your library is changed. The note under the button says what will be added, and if your library already has everything, the button is dimmed. This is the safe choice for getting back something you deleted.

### Replace Library

**Replace Library…** makes your library match the backup: it adds, updates and removes pieces, folders and set lists as needed. The note under it lists those changes before you confirm. Before anything changes, the app saves a safety backup of your current library, listed with the kind **Before Restore**. With iCloud sync on, the result reaches all your devices. Shared folders and set lists are left as they are.

### Shared folders and set lists

Your notes and markings on shared pieces are added back by either kind of restore. A shared folder or set list you owned comes back only if it no longer exists, and then as your own folder or set list that isn't shared. To work on it with others again, share it again.

## Restoring with the free version

If you've never had Premium, a restore brings back up to the free version's 15 pieces. The rest stay in the backup, and **Upgrade to Restore Everything** appears above the restore buttons. If you've had Premium before with the same Apple Account, everything is restored.

## Restoring with more than one device

With iCloud sync on, restore on one device only. If you open a backup on another device while a restore is running, it says which device is restoring and the restore buttons are dimmed. Your other devices update through iCloud when the restore finishes.
