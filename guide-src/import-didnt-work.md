---
{
 "slug": "import-didnt-work",
 "h1": "An import didn't work",
 "seo_title": "Fix a Sheet Music PDF That Won't Import | Music Folder",
 "description": "A PDF or scan won't import into Music Folder? Check the file type, the free limit, files still in iCloud Drive, password-protected PDFs and duplicate names.",
 "intent": "troubleshooting",
 "intent_note": "Musicians whose PDF, photo, folder or scan didn't arrive in the library, or arrived without its pages.",
 "searches": [
  "can't import pdf",
  "pdf won't open",
  "import failed",
  "file greyed out",
  "file dimmed",
  "no sheet music found",
  "15 piece limit",
  "password protected pdf",
  "already taken",
  "scan not working"
 ],
 "availability": [
  {
   "kind": "premium",
   "text": "The free version holds up to 15 pieces and 5 sections; Premium has no limit."
  }
 ],
 "related": [
  "import-music",
  "free-and-premium",
  "create-a-chord-chart",
  "add-sections-to-a-book"
 ],
 "feature_link": null,
 "documents": [
  "Shared UI/SongListViewController.swift (Add to Library menu, attachFiles PDF-only picker, addFromPhotos, importFolder, scanSheetMusic, canScanDocuments, No Sheet Music Found)",
  "Sharing/ImportSourceConverter.swift (image extensions, folder scan)",
  "Services/SongLibraryService.swift (importedPDF rejects locked PDFs, LibraryError)",
  "Shared UI/AddSongFormViewController.swift (consumePendingImportFile, name already taken)",
  "Sharing/ReviewImportViewController.swift (batch free-tier check, swipe to delete)",
  "Premium/PremiumGate.swift (FreeTier.songLimit 15, sectionAllowance 5, messages)",
  "Chords/ChartImport.swift",
  "Info.plist (document types)",
  "R5",
  "R68"
 ],
 "verified": "76048e78",
 "differs_from_4_2": null,
 "shots": [],
 "open_questions": [
  "Sharing/ReviewImportViewController.swift: when one of several picked PDFs can't be read (importedPDF returns nil), the row is still saved as a piece with no PDF. The guide says such a piece 'arrives without its pages'. Owner: confirm, or should Review drop or flag that row?",
  "Info.plist registers only PDF (plus the app's own .mf* and backup types) for Open In, while SceneDelegate and SongListScreen route chord chart files (.cho, .chordpro, .pro, .crd, .txt) that are handed to the app. The guide only links to Create a chord chart for chart files; that guide's writer should confirm how chart files actually get in (drag and drop onto the Music list is confirmed in SongListViewController).",
  "ImportSourceConverter.extractSheetMusicSync reads each file in the chosen folder directly; I couldn't confirm from code whether iCloud Drive files that aren't downloaded are fetched or skipped, so the guide says they may be skipped and advises downloading the folder first."
 ]
}
---
When a PDF, photo or scan doesn't show up in your library, or shows up without its music, the reason is usually the type of file, the free version's limit, a file that's still in iCloud and not on your device, or a PDF that can't be opened. The sections below cover each one. For the ways to bring music in, see [Import music](/guide/import-music).

## Check the type of file

- **Files** in the Add to Library menu imports PDFs only. Other files appear dimmed and can't be selected.
- To import pictures of sheet music, use **Photos**, or **Folder** for a folder of files. With Photos, each picture starts as a one-page piece, and when you pick several you can combine pages into one piece before adding them. Folder import takes PDFs and JPEG, PNG, HEIC, GIF, BMP, TIFF and WebP images (each image becomes a one-page piece), and says **No Sheet Music Found** when the folder has none.
- Word documents and notation files (MusicXML, MuseScore, Sibelius, Finale, Dorico) can't be imported. Export or print them to PDF from the app that made them, then import the PDF.
- Chord chart text files (.cho, .chordpro, .chopro, .pro, .crd and .txt) become chord charts, not PDFs. See [Create a chord chart](/guide/create-a-chord-chart).

On Mac, the same menu items are called **Import from Files**, **Import from Photos** and **Import Folder**.

## Check the free version's limit

The free version holds up to 15 pieces and 5 sections in your library. When you reach the limit, adding more opens the Premium screen, headed **Keep adding to your library**, instead of the import. Adding sections past the fifth opens it headed **Unlock Unlimited Sections**. See [Free and Premium](/guide/free-and-premium).

When you import several files at once, the whole batch is checked before anything is added. If it would take you past the limit, nothing in the batch is added. To add what fits, swipe left on rows in the review list to remove them, then add the rest.

## Make sure the file is on your device

- **Files in iCloud Drive** have to download before they can be imported. If you're offline, or the download stalls, the import can't finish. In the Files app, open the file once (or touch and hold it and choose **Download Now**), wait until it has downloaded, then import it again. Before you use **Folder**, download the whole folder, since files that aren't on the device may be skipped.
- **Photos in iCloud Photos** download when you pick them. If you're offline, some may be left out. Connect to the internet and pick them again.

## Check that the PDF opens

- **Password-protected PDFs** can't be imported. Music Folder doesn't ask for a PDF's password, so a PDF that needs one to open won't come in with its pages. Remove the password in the app that created it (or save an unprotected copy), then import that copy.
- **Damaged or incomplete PDFs** can't be read. Open the file in the Files app. If it doesn't display there either, download or export a fresh copy.

When a PDF can't be read, the **Add Music** form opens without any music attached, or the piece arrives without its pages. Delete that piece and import a good copy.

## Choose a different name

Each piece in your library needs its own name. If you see a message that the name "is already taken", change the title in the **Add Music** form and save again.

## If scanning doesn't work

- **Scan Sheet Music** appears only on a device with a camera that supports document scanning, so it isn't offered on Mac.
- The scanner needs the camera. If it can't see anything, open Settings, find Music Folder, and turn on **Camera**.

## In a shared folder

If the {sf:plus} menu doesn't offer to add music in a folder someone shared with you, you have View Only access to it. Working in a shared folder also needs Premium for everyone taking part. A shared folder's menu has no **Folder** item, because a whole folder of files can only be imported into your own library. See [Work together in a shared folder or set list](/guide/work-together-in-a-shared-folder-or-set-list).

## Contact us

If an import still doesn't work, [contact us](/contact). It helps to include:

- The type of file, its size and number of pages, and where it came from (Files, Photos, AirDrop, email, a website)
- How you imported it and any message you saw
- Your device, its iOS, iPadOS or macOS version, and the Music Folder version (**Account › About › Version**)

If you can, attach the file, unless it's music you aren't allowed to share.
