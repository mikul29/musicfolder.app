---
{
 "slug": "import-music",
 "h1": "Import music",
 "seo_title": "Import Sheet Music PDFs, Photos and Scans | Music Folder",
 "description": "Import sheet music PDFs into Music Folder from Files, Photos, a folder, the document scanner, AirDrop or drag and drop, one piece at a time or many at once.",
 "intent": "existing",
 "intent_note": "A musician with PDFs, photos or paper scores who wants them in the app, often many files at once.",
 "searches": ["add pdf", "upload sheet music", "airdrop", "open in", "scan", "photos", "bulk import", "drag and drop", "import folder", "add music"],
 "availability": [{"kind": "premium", "text": "Free includes 15 pieces; Premium has no limit."}],
 "related": ["add-sections-to-a-book", "organize-music-in-folders", "import-didnt-work", "get-free-sheet-music"],
 "feature_link": {"href": "/features/sheet-music-organizer", "text": "the Sheet Music Organizer"},
 "documents": ["Shared UI/SongListViewController.swift (addToLibrarySections, routeImported, drop interaction)", "Sharing/ReviewImportViewController.swift", "Sharing/OrganizePagesViewController.swift", "Sharing/ImportSourceConverter.swift", "Sharing/ScanImport.swift", "Sharing/SongMetadataAnalyzer.swift", "Songs/Song View/SongListScreen.swift (handleReceivedFiles)", "App/SceneDelegate.swift (classifyIncoming)", "Shared UI/AddSongFormViewController.swift", "Premium/PremiumGate.swift (FreeTier)", "R5", "R62", "R68"],
 "verified": "76048e78",
 "differs_from_4_2": null,
 "shots": [],
 "open_questions": [
  "AirDrop or Open In with several plain PDFs at once: the code consumes the first file into the Add Music form and appears to open the form again for the next file after each save (SongListScreen.unwindToSongsView → handleReceivedFiles). Not stated in the guide; confirm the intended behavior before documenting it."
 ]
}
---
You can bring sheet music into your library from the Files app, your photo library, a folder of PDFs, the document scanner, AirDrop and other apps. One file opens the Add Music form so you can check its details; several files open a review screen where you add them together.

## Add music with the + button

1. Open **Library**, then **Music**. On iPad, choose **Music** in the sidebar.
2. Tap {sf:plus} to open the **Add to Library** menu.
3. Choose where the music comes from:

- **Files**: one or more PDFs from the Files app, iCloud Drive or other storage.
- **Photos**: pictures of printed music, turned into PDF pages.
- **Folder**: every PDF and image (JPEG, PNG, HEIC, GIF, TIFF, WebP and others) in a folder and its subfolders, each as its own piece.
- **Scan Sheet Music**: photograph paper music with the document scanner, saved as one PDF. It appears only on devices with a camera.

The same menu has **New Chord Chart**, which starts a blank chart instead of importing a file; see [Create a chord chart](/guide/create-a-chord-chart).

On Mac: the import sources are named **Import from Files**, **Import from Photos** and **Import Folder**, and there's no scanner.

Tip: Open a folder and use its {sf:plus} button instead, and the music you import goes straight into that folder. See [Organize music in folders](/guide/organize-music-in-folders).

## Check the details of one piece

When you import a single PDF, one photo or a scan, the **Add Music** form opens with the music attached. The title starts as the file name, marked "from file." Change what you like, then tap the checkmark to save.

Below the title and composer are **Details** (tempo, time signature, key, duration and **Display as Book**), **Folder** and **Tags**, **Pages**, **Sections** for music with two or more pages, and the chord chart and recording rows. Only the title is required, and you can fill in the rest later; [Edit or delete a piece](/guide/edit-or-delete-a-piece) explains each field.

On devices with Apple Intelligence (iOS 26 or later), the form shows "Reading the music…" while it reads the first page, then fills in the title, composer, tempo, time signature and key where they're printed. Fields it can't read stay empty.

If the PDF is a collection, such as a hymnal or a book of études, the form may show a card like "12 sections found," taken from the PDF's own table of contents. Nothing is created until you review it; see [Add sections to a book](/guide/add-sections-to-a-book).

## Import many pieces at once

When you choose more than one PDF, from Files or a folder, the review screen opens, titled with the number of pieces (for example, **Add 8 Pieces**).

1. Check the titles. Each starts as its file name; tap a title to change it.
2. To fill in more for one piece, tap its row. The full form opens; tap the checkmark to return to the list.
3. To put every piece in the same folder, tap **Folder** and choose one.
4. To leave a file out, swipe left on its row and tap **Delete**. To include more, tap **Add more Sheet Music**.
5. Tap the checkmark to add them all.

With Apple Intelligence, the review screen first reads each piece ("Reading pieces… 3 of 8") and fills in what it finds.

### Several photos

Choose more than one photo and **Organize Photos** opens first, because one piece can span several photos. Each photo starts as its own piece. Drag a page onto another piece to combine them, drag within a piece to change the page order, or drag a page onto "Drag a page here to start a new piece" to split it off. Then tap **Review** (for example, **Review 3 Pieces**) to go on.

## Open music from another app or AirDrop

Send a PDF to Music Folder from another app's share sheet, from the Files app or by AirDrop, and the app opens to the Music list with the Add Music form for that PDF. Other files are recognized by type:

- Chord chart files (.cho, .chordpro, .chopro, .pro, .crd and .txt) become chord charts. See [Create a chord chart](/guide/create-a-chord-chart).
- Music Folder files (.mfsong, .mfsetlist, .mfgroup) import with their details. See [Send a copy or print](/guide/send-a-copy-or-print).
- A library backup (.mfbackup) opens the restore screen instead. See [Back up and restore your library](/guide/back-up-and-restore-your-library).

## Drag and drop

On iPad, drag PDFs or chord chart files from the Files app or another app onto the Music list or a folder's list. On Mac, drag them from the Finder. One PDF opens the Add Music form and several open the review screen. Drops aren't accepted while you're selecting pieces.

## The free limit

The free version holds 15 pieces. With 15 already in your library, choosing a source shows the Premium offer instead of the file picker. When you import several files at once, the whole batch has to fit; if it doesn't, the Premium offer appears and nothing is added, so you can remove rows from the review screen and try again. Sections inside imported music count toward the free allowance of 5 sections. See [Free and Premium](/guide/free-and-premium).

If an import doesn't work, see [An import didn't work](/guide/import-didnt-work).
