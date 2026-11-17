# User Guide: open questions for the owner
Generated from each guide's `open_questions` (tools/guide/build.py doesn't render them). Nothing here blocks publishing a guide: where a fact couldn't be confirmed, the guide leaves it out or words it carefully. Answer, then update the guide and remove the question.

## [free-and-premium](../../guide-src/free-and-premium.md)
- Prices are taken from pricing.html and match Configuration.storekit ($2.99 a month, $19.99 a year with a 7-day free trial, $49.99 lifetime). Confirm App Store Connect still matches before publishing. (Configuration.storekit, pricing.html)
- Pre-3.0 buyers: the code grandfathers the original one-time Premium upgrade (product PremiumVersion), shown in Account as Lifetime, 'Original unlock'. pricing.html says 'If you bought Music Folder before version 3.0'. Is 'bought the original Premium upgrade' the right wording, or was the app itself ever paid? (Premium/PremiumStore.swift)

## [use-music-folder-on-a-mac](../../guide-src/use-music-folder-on-a-mac.md)
- Minimum macOS: the project sets no LSMinimumSystemVersion; IPHONEOS_DEPLOYMENT_TARGET is 17.0 (pbxproj). For iPad apps on Mac that normally means macOS 14 Sonoma or later. Please confirm in App Store Connect (Mac availability) before we state a version; the article currently names none. (MyBandProject.xcodeproj/project.pbxproj)
- Sidebar on Mac: the iPad sidebar shell needs iOS 18 APIs (MainTabBarController+Pad.swift). Does a Mac on macOS 14 get the bottom tab bar instead of the sidebar? The article describes the layout as matching the iPad without naming macOS versions. (App/MainTabBarController+Pad.swift)
- Is Mac availability turned on for Music Folder in App Store Connect (Designed for iPad apps on Mac), so it's found in the Mac App Store? The article says to find it there. (App Store Connect)

## [import-music](../../guide-src/import-music.md)
- AirDrop or Open In with several plain PDFs at once: the code consumes the first file into the Add Music form and appears to open the form again for the next file after each save (SongListScreen.unwindToSongsView → handleReceivedFiles). Not stated in the guide; confirm the intended behavior before documenting it.

## [get-free-sheet-music](../../guide-src/get-free-sheet-music.md)
- Catalog scope: StarterGroup and the landing suggest classical / public-domain scores only (instrument rows Piano, Guitar, Voice, Woodwinds, Brass, Strings). The guide says 'classical'; confirm nothing non-classical is in the 4.3 catalog.

## [edit-or-delete-a-piece](../../guide-src/edit-or-delete-a-piece.md)
- Replacing a piece's PDF: the form's 'Replace Sheet Music' button title still exists in code, but in the 4.3 layout the add-file row only shows when there's no PDF. The guide doesn't describe replacing a PDF; confirm whether there is a supported way (other than Organize Pages) to swap the whole PDF of a library piece.

## [keep-notes-on-a-piece](../../guide-src/keep-notes-on-a-piece.md)
- The panel's "Only on your devices" caption is driven by CollabShareService.isCollaborative (the 4.2 collaboration check). It is not clear whether it also shows for 4.3 Shared Folder / Shared Set List pieces, so the guide doesn't mention the caption. Confirm whether it should.

## [mark-up-music-with-apple-pencil](../../guide-src/mark-up-music-with-apple-pencil.md)
- PDFAnnotationSession.swift: the code relies on Apple's tool palette for finger drawing (drawingPolicy .default; the comment names the palette's "Draw with Finger" switch). Confirm that switch's current wording in the iPadOS 18 / 26 tool palette and whether to also mention Settings › Apple Pencil › Only Draw with Apple Pencil.
- PDFAnnotationSession.swift: drawing with a mouse or trackpad on a Mac is not covered here; confirm how annotation behaves on Mac before adding it.

## [create-a-chord-chart](../../guide-src/create-a-chord-chart.md)
- Info.plist / SceneDelegate.swift / SongListViewController.swift: SceneDelegate.classifyIncoming routes .cho, .chordpro, .chopro, .pro, .crd and .txt URLs to ChartImport, but Info.plist's CFBundleDocumentTypes declares only the Music Folder types and PDF (no plain text or ChordPro type), the + menu's Files picker (attachFiles) and the document pickers elsewhere accept com.adobe.pdf only, and Import Folder takes PDFs and images only. So the guide describes drag and drop onto a music list (the only verified route) plus pasting into the editor. Please confirm on a device whether the Files app's share sheet, Open In or AirDrop offers Music Folder for a .cho or .txt file; if not, should the document types be added, or the guide stay as is?

## [turn-a-pdf-into-a-chord-chart](../../guide-src/turn-a-pdf-into-a-chord-chart.md)
- SongPDFView.swift / ReaderToolbarCustomization.swift: Convert to Chord Chart can be placed on the song reader's toolbar (ReaderTool.convert, symbol wand.and.rays; verified in code). The guide mentions it in one sentence; keep it, or leave optional toolbar tools out of this guide?

## [send-a-copy-or-print](../../guide-src/send-a-copy-or-print.md)
- Opening a received file from the Files app: Info.plist declares Music Folder the Owner of the .mfsong and .mfsetlist types (check .mfgroup / .mfsongs too). Confirm on a device that tapping each file type in Files opens Music Folder directly, so the guide's hedge "choose Music Folder if you're asked" can be dropped. App/SceneDelegate.swift, MyBandProject/Info.plist.

## [share-a-folder-or-set-list](../../guide-src/share-a-folder-or-set-list.md)
- Permission names: the app never names the roles itself; they appear only in Apple's sheets (UIActivityViewController with CKAllowedSharingOptions [.readOnly, .readWrite] × [.specifiedRecipientsOnly, .anyoneWithLink], and UICloudSharingController). The guide uses Apple's labels "Can make changes" / "View only" and "Anyone with the link". Confirm the exact wording on an iOS 17 and an iOS 26 device. Sharing/SharedShareManager.swift, App/SharedFolderActions.swift.
- Move to New Sharing: verified in code that once a move reaches converted, LegacyMoves.hideMovedOriginals hides the original on every device, and the ONLY routes to the move screen (and its Stop Old Sharing…) are the original's own context menu ("Moving to New Sharing") and Collaborate on the original (routeToMove). Nothing else opens LegacyMoveViewController and nothing un-hides the original (Account ▸ Moved Shares was removed 2026-11-16). So after a completed move the owner has no way to stop the old 4.2 sharing. The guide gives no steps for stopping it. Owner: is this intended, or does a route need restoring? App/LegacyMoveActions.swift, App/LegacyMoveViewController.swift.
- Owner's other devices still on 4.2: Collaborate removes the original library folder / set list (GroupLibraryService.deleteGroupKeepingSongs via LibraryConversionAdapter.hideOriginal) once the server verifies the copy; that delete syncs, so a 4.2 device should see the folder disappear while its pieces stay in All Music. The guide only says to update other devices. Confirm on a 4.2 device before saying more.

## [join-a-shared-folder-or-set-list](../../guide-src/join-a-shared-folder-or-set-list.md)
- What a person on Music Folder 4.2 (or without the app) sees when they tap a 4.3 invitation link isn't confirmed (06-edge-cases says the 4.2 behavior is untested). The guide only says 4.3 or later is needed. App/SceneDelegate.swift, App/SharedFolderActions.swift handleInvitation.
- Leave: the app's confirmation does say "Your notes and markings on N pieces will be kept for 30 days in case you rejoin." (SharedFolderActions.confirmLeave, line 277). leaveCollection only enqueues the zone leave; no code found that deletes the member's notes / layers after 30 days (and R110: nothing is purged automatically). The guide says they're kept in case you rejoin, without a number. Owner: should the alert drop "for 30 days", or is a cleanup planned?

## [work-together-in-a-shared-folder-or-set-list](../../guide-src/work-together-in-a-shared-folder-or-set-list.md)
- Previous Version for a piece that lives only in a Shared Set List: the menu item exists only in the song reader (SongPDFView.previousVersionMenuElement); set-list playback (PDFViewInSetList) has none. The guide routes through Library › Music with the Source filter set to the Shared Set List (SharedPieces.sourceOptions lists every listed collection, set lists included; SongListScreen opens the song reader). Confirm on a device that a shared set list's piece opens in the song reader from there and shows Previous Version. Songs/Song View/SongPDFView.swift, App/SharedPieceActions.swift.

## [connect-planning-center](../../guide-src/connect-planning-center.md)
- Clear Cached Files: its confirmation says "Annotations on Planning Center PDFs are removed too." (PCOAccountScreen.swift line 181), but since 4.2 Planning Center ink lives in annotation layers keyed pco-att-<id> in the private store, not in the cached files (CLAUDE.md Annotations: PCOFileCache.storeAnnotated is legacy). The guide doesn't mention markings in the Clear Cached Files step. Owner: is the warning still true, or should the dialog drop it?

## [sync-with-icloud](../../guide-src/sync-with-icloud.md)
- The Important note says that turning iCloud off for Music Folder, or signing out of iCloud, removes the synced library from that device and that changes not yet uploaded can be lost. This comes from the 2026-07 support investigation (NSPersistentCloudKitContainer purges its store when the account goes away), not from app code. Please confirm the wording before publishing. (App/AppDelegate.swift)
- First launch without iCloud: the store gets CloudKit only if an iCloud account is signed in at first launch; the next launch attaches it because the store file exists. The article tells people whose iCloud Sync row says Off to quit and reopen the app. Confirm that's the right advice. (App/AppDelegate.swift)

## [music-isnt-syncing](../../guide-src/music-isnt-syncing.md)
- AppDelegate.swift attachment gate: a store that was created without iCloud is CloudKit-attached on the NEXT launch (storeExists is true), so the guide tells people who signed in later to close and reopen the app. Owner: confirm that a library created before signing in uploads its existing pieces once the account appears (I could not verify NSPersistentCloudKitContainer's behaviour for a none-to-account change from the code).
- The warning that turning off iCloud for the app (or signing out) removes the synced library from the device comes from the 2026-07-08 support ticket memo (NSPersistentCloudKitContainer purge on account loss). Owner: confirm this wording is still right for 4.3.

## [library-looks-empty-after-reinstalling](../../guide-src/library-looks-empty-after-reinstalling.md)
- CloudKitImportMonitor keeps lastKnownSongCount in UserDefaults.standard, which a reinstall erases, so the Restoring Library message does not appear after a reinstall and the guide says the ordinary empty screens show while iCloud downloads. Owner: confirm that's the intended behaviour (it means a reinstalled app shows Home's add-your-first-music card during the download).

## [cant-hear-the-metronome-or-a-recording](../../guide-src/cant-hear-the-metronome-or-a-recording.md)
- SongPDFView.firstPlayableAudio plays the first recording that is already on the device and asks iCloud for the others; when none is downloaded the reader may show no playable recording at all. Owner: confirm what the reader's Play button does in that case so the guide can name it.

## [import-didnt-work](../../guide-src/import-didnt-work.md)
- Sharing/ReviewImportViewController.swift: when one of several picked PDFs can't be read (importedPDF returns nil), the row is still saved as a piece with no PDF. The guide says such a piece 'arrives without its pages'. Owner: confirm, or should Review drop or flag that row?
- Info.plist registers only PDF (plus the app's own .mf* and backup types) for Open In, while SceneDelegate and SongListScreen route chord chart files (.cho, .chordpro, .pro, .crd, .txt) that are handed to the app. The guide only links to Create a chord chart for chart files; that guide's writer should confirm how chart files actually get in (drag and drop onto the Music list is confirmed in SongListViewController).
- ImportSourceConverter.extractSheetMusicSync reads each file in the chosen folder directly; I couldn't confirm from code whether iCloud Drive files that aren't downloaded are fetched or skipped, so the guide says they may be skipped and advises downloading the folder first.
