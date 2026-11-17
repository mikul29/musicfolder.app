---
{
 "slug": "use-music-folder-on-a-mac",
 "h1": "Use Music Folder on a Mac",
 "seo_title": "Use Music Folder on a Mac",
 "description": "Run Music Folder on a Mac with Apple silicon: install it, use the menu bar, drag PDFs from the Finder, resize the window, and learn every keyboard shortcut.",
 "intent": "existing",
 "intent_note": "Musicians with a Mac (often a laptop on a music stand or a desktop for preparing parts) who want to know whether the app runs there and how to drive it with a keyboard.",
 "searches": [
  "macbook",
  "macos",
  "desktop",
  "keyboard shortcuts",
  "hotkeys",
  "menu bar",
  "finder",
  "apple silicon",
  "m1"
 ],
 "availability": [
  {
   "kind": "device",
   "text": "Requires a Mac with Apple silicon, where Music Folder runs as its iPad app."
  }
 ],
 "related": [
  "sync-with-icloud",
  "import-music",
  "turn-pages",
  "transpose-capo-and-numbers"
 ],
 "feature_link": null,
 "documents": [
  "App/MainMenu.swift",
  "App/SceneDelegate.swift",
  "Shared UI/SongListViewController.swift",
  "PDF Reader/PDFReaderToolbar.swift",
  "PDF Reader/PageTurnerKeys.swift",
  "PDF Reader/ScoreLinkNavigator.swift",
  "Chords/ChordKeyControl.swift",
  "Chords/ChartEditorViewController.swift",
  "Notes/NotesPanelViewController.swift",
  "Groups/FolderEditorSheet.swift",
  "Set Lists/Songs View/SetListViewSongs.swift",
  "PDF Reader/FaceTurnSettings.swift",
  "Premium/PremiumPlanView.swift",
  "R23",
  "R50"
 ],
 "verified": "76048e78",
 "differs_from_4_2": "4.3 needs iOS 17 or later, which raises the oldest macOS that can run the app (see open questions).",
 "shots": [],
 "open_questions": [
  "Minimum macOS: the project sets no LSMinimumSystemVersion; IPHONEOS_DEPLOYMENT_TARGET is 17.0 (pbxproj). For iPad apps on Mac that normally means macOS 14 Sonoma or later. Please confirm in App Store Connect (Mac availability) before we state a version; the article currently names none. (MyBandProject.xcodeproj/project.pbxproj)",
  "Sidebar on Mac: the iPad sidebar shell needs iOS 18 APIs (MainTabBarController+Pad.swift). Does a Mac on macOS 14 get the bottom tab bar instead of the sidebar? The article describes the layout as matching the iPad without naming macOS versions. (App/MainTabBarController+Pad.swift)",
  "Is Mac availability turned on for Music Folder in App Store Connect (Designed for iPad apps on Mac), so it's found in the Mac App Store? The article says to find it there. (App Store Connect)"
 ]
}
---
On a Mac with Apple silicon, Music Folder runs as its iPad app. With iCloud sync, your library, set lists and annotations are the same as on your iPhone or iPad, and on the Mac you also get a menu bar, keyboard shortcuts and drag and drop from the Finder.

## Install and sign in

1. On your Mac, open the App Store and search for Music Folder. It's listed with the iPhone and iPad apps.
2. Install it with the same Apple Account you use on your iPhone or iPad.
3. Open the app. If iCloud is on for your Mac, your library syncs in the same way it does on your other devices (see [Sync with iCloud](/guide/sync-with-icloud)).

Premium carries over: a subscription or Lifetime purchase made with the same Apple Account works on the Mac too. If it doesn't show, open Account, tap **Upgrade to Premium**, then **Restore Purchases**.

## The window

The window works like an iPad screen. You can resize it freely or use full screen, and the layout adapts to the space: a wide window uses the iPad layout, while a narrow one switches to the iPhone-style tab bar. The window can't be made narrower than an iPhone screen.

In a wide window, the reader can show two pages side by side. Open a piece, then choose **⋯ › Page Display & Layout › Two-Page View**.

## Add PDFs from the Finder

Drag one or more PDFs from the Finder onto the Music list. Drop them on a folder's list instead to add them to that folder. One PDF opens the **Add Music** form; several open a list where you check the titles before adding them all. Chord chart files (.cho, .chordpro, .chopro, .pro, .crd and .txt) can be dropped the same way. To pick files instead of dragging them, choose **File › Import PDF…** in the menu bar.

## Menu bar

Besides the standard macOS menus, Music Folder adds:

- **File › Import PDF…** opens a file picker to add music to your library.
- **File › Back Up Library Now** saves a backup straight away (see [Back up and restore your library](/guide/back-up-and-restore-your-library)).
- **Edit › Search Music** goes to the Music list and puts you in the search field.
- **View › Music**, **Folders** and **Set Lists** switch between the library lists.
- **Chart** works on the piece open in the reader: transpose a chord chart, change its text size, or open **Edit Details** and **Edit Chord Chart**. The items are dimmed when no reader is open.

The File, Edit and View commands above are unavailable while a piece is open in the reader or a sheet is open over the window. Escape closes the reader.

## Keyboard shortcuts

### Library

- Command-N: Import PDF
- Command-F: Search Music
- Command-1: Music
- Command-2: Folders
- Command-3: Set Lists

### Reader

- Right Arrow, Down Arrow, Page Down, Space or Command-Right Arrow: next page
- Left Arrow, Up Arrow, Page Up, Shift-Space, Return or Command-Left Arrow: previous page
- Escape: close the reader
- Command-Left Bracket ([): go back to where you were after following a Page Link
- Shift-Command-L: Page Links

Bluetooth page turner pedals send these same keys, so a pedal that works on your iPad works on your Mac. See [Turn pages hands-free](/guide/turn-pages-hands-free).

### Chart menu (with a piece open in the reader)

- Command-T: transpose up
- Shift-Command-T: transpose down
- Command-0: back to the original key
- Command-= (or Command-+): bigger text
- Command-Hyphen: smaller text
- Command-I: Edit Details
- Command-E: Edit Chord Chart

The first five work on chord charts. Transposing needs Premium, except in the two example pieces.

### Chord chart editor

- Command-S: Done
- Command-Left Bracket ([): insert chord brackets
- Shift-Command-P: show or hide the preview

### Other screens

- Command-B: bold text in the notes panel; Escape closes the panel
- Command-Return: create or save a folder in the folder editor; Escape cancels
- Escape: close the Add to Set List pane in a set list, and close the Key, Formatting and Sequence panels for chord charts

On iPad with a hardware keyboard, the same shortcuts work. Hold down the Command key to see the ones available on the current screen.

## What's different on a Mac

- **Scan Sheet Music** isn't offered, because it needs a device camera. Scan on your iPhone or iPad and the piece syncs to your Mac.
- Face Gestures aren't available on the Mac.
- **Manage Subscription** and **Redeem Offer Code** in Account take you to the App Store instead of opening a sheet in the app.
