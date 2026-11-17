---
{
 "slug": "library-looks-empty-after-reinstalling",
 "h1": "My library looks empty after reinstalling",
 "seo_title": "Library Empty After Reinstalling the App | Music Folder",
 "description": "Reinstalled Music Folder or set up a new device and your sheet music is missing? Here's how to get your library back from iCloud or from a backup.",
 "intent": "troubleshooting",
 "intent_note": "Musicians who deleted and reinstalled the app, or moved to a new iPad or iPhone, and see no music.",
 "searches": ["library gone", "music disappeared", "lost my music", "deleted the app", "new ipad", "new iphone", "restore library", "restoring library", "songs missing"],
 "availability": [],
 "related": ["music-isnt-syncing", "back-up-and-restore-your-library", "sync-with-icloud", "manage-your-subscription"],
 "feature_link": null,
 "documents": ["Data/CloudKitImportMonitor.swift (lastKnownSongCount in UserDefaults, shouldShowRestoringOverlay)", "App/EmptyStateView.swift", "App/TodayView.swift (isLibraryEmpty)", "App/WelcomeFilm.swift (FirstRunWelcome)", "App/MusicTypePickerView.swift", "App/AppDelegate.swift (CloudKit attachment gate)", "App/AccountView.swift", "App/BackupView.swift", "Data/BackupStore.swift", "Premium/PremiumGate.swift (FreeTier.restoreAllowance)", "R34"],
 "verified": "76048e78",
 "differs_from_4_2": null,
 "shots": [],
 "open_questions": [
  "CloudKitImportMonitor keeps lastKnownSongCount in UserDefaults.standard, which a reinstall erases, so the Restoring Library message does not appear after a reinstall and the guide says the ordinary empty screens show while iCloud downloads. Owner: confirm that's the intended behaviour (it means a reinstalled app shows Home's add-your-first-music card during the download)."
 ]
}
---
When you delete Music Folder and install it again, or set up a new iPad or iPhone, the app starts with nothing on the device and downloads your library from iCloud. Until that download finishes, the Music, Folders and Set Lists screens can look empty and Home may invite you to add your first music. If your library was syncing with iCloud before, it's still there, and if it wasn't, a backup can bring it back.

The app also shows its welcome screens again after a reinstall, as it would for a new user. Tap **Get Started**, then **Skip for now**, to go straight to Home.

## Wait for iCloud to bring your library back

A reinstalled app has no record of the library it had before, so it shows the ordinary empty screens while it downloads, not a "restoring" message. Pieces appear as they arrive, and a large library with many PDFs can take a while.

1. Keep Music Folder open, on Wi-Fi, ideally plugged in.
2. Don't import your music again while you wait. Anything you import now ends up as a second copy once the original arrives from iCloud.
3. Check back after a few minutes. If pieces are appearing, let it finish.

## If nothing arrives

1. Open Settings and tap your name. Make sure you're signed in with the same Apple Account you used before. A library synced to another Apple Account won't appear.
2. Tap **iCloud** and make sure Music Folder is turned on in the list of apps that use iCloud (you may need to tap **Show All** or **See All**).
3. In Music Folder, open **Account**: tap your picture or initials at the top of Home, or, where the app shows a sidebar, your name or **Account** at the bottom of it. Under **Library & Sync**, check **iCloud Sync**.
4. If it says **Off**, Music Folder was opened before the device was signed in to iCloud. Close Music Folder from the App Switcher, open it again, and check that it now says **On**.
5. If it says **Paused**, the app can't use your iCloud account right now. Check steps 1 and 2 again.

If none of this helps, work through [My music isn't syncing](/guide/music-isnt-syncing).

## If your library wasn't syncing with iCloud

If iCloud sync was off on the old installation, your library existed only on that device, and deleting the app deleted it. A backup is the way to get it back:

- Backups saved in iCloud Drive (iCloud Drive › Music Folder › Backups) are kept when you delete the app. Automatic backups go there when iCloud Drive is available.
- Backups saved **On This Device** are deleted with the app.
- A backup you saved somewhere else with **Save to Files…** can be restored from there.

## Restore from a backup

1. Open **Account**, then tap **Backup & Restore** under **Library & Sync**.
2. Under **Backups**, tap the backup you want, or tap **Restore from File…** to choose one you saved elsewhere.
3. Tap **Add Missing Items** to add what's missing, or **Replace Library…** to make the library match the backup.

Important: If your library syncs with iCloud, let iCloud finish bringing it back before you restore a backup. Restoring while pieces are still downloading can leave you with two copies of them.

If you've never had Premium, a restore brings back up to 15 pieces, and **Upgrade to Restore Everything** appears when some are held back. If you've had Premium before, everything in the backup comes back. For the details, see [Back up and restore your library](/guide/back-up-and-restore-your-library).

## Premium and shared music

Premium is restored automatically when the app starts. If it doesn't show as active, restore your purchase as described in [Manage your subscription](/guide/manage-your-subscription).

Folders and set lists other people share with you aren't part of your backups. They come back through iCloud once you're signed in with the same Apple Account.

## Contact us

If your library doesn't come back, [contact us](/contact) before you delete or reinstall the app again. It helps to include:

- Whether iCloud sync was on before you reinstalled, and roughly how many pieces you had
- What **iCloud Sync** says in Account
- Whether you see any backups under **Backup & Restore**
- Your device, its iOS or iPadOS version, and the Music Folder version (**Account › About › Version**)
