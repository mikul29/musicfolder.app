# User Guide: open questions and release blockers

Reviewed 2026-11-17 against app commit `76048e78` (release/4.3). Every guide leaves out or carefully words anything that couldn't be confirmed, so no guide states a guess as fact. Each guide's own `open_questions` field holds the detail.

## Release blockers

1. **Music Folder 4.3 isn't on the App Store yet** (4.2.1 is live). The sharing guides (Share, Join, Work together, Send a copy), the iOS 17 minimum and several 4.3 labels describe 4.3. Publish the User Guide only after 4.3 is released. At the same time, update the iOS 15 mentions on /support, /features/sheet-music-reader and /features/sharing, and check /features/sharing against 4.3.
2. **App, not documentation: after Move to New Sharing there's no way to stop the old 4.2 share.** Once a move finishes, the original is hidden on every device (`LegacyMoves.hideMovedOriginals`). The only routes to the move screen and its **Stop Old Sharing…** are the original's own menu and Collaborate on the original. Legacy Collaborations lists only revoked shares, not moved originals. Members still on 4.2 keep their old copy and access until the owner stops it, and the owner can't. The guide describes this accurately ("it stays shared with members who haven't moved yet") and gives no steps for stopping. Owner decision: fix in the app before release, or accept.

## Minor: confirm on a device, or soon after release (guide wording is safe either way)

- **sync-with-icloud, music-isnt-syncing:** the warning that turning iCloud off for the app, or signing out, removes the synced library from that device. It comes from the 2026-07 support investigation, and it errs on the side of caution.
- **music-isnt-syncing:** a library created before signing in to iCloud is attached to iCloud on the next launch (code). Confirm its existing pieces upload.
- **share-a-folder-or-set-list:** Apple's role labels in the sharing sheet on iOS 17 and iOS 26 ("Can make changes", "View only", "Anyone with the link").
- **share-a-folder-or-set-list:** an owner's device still on 4.2 should see a converted folder disappear while its pieces stay (code).
- **join-a-shared-folder-or-set-list:** what someone on 4.2 sees when tapping a 4.3 invitation. The guide only says 4.3 or later is needed.
- **work-together-in-a-shared-folder-or-set-list:** Previous Version for a piece that is only in a Shared Set List, opened through Library › Music › Filter › Source.
- **mark-up-music-with-apple-pencil:** the current wording of the tool palette's **Draw with Finger** switch on iPadOS 18 and 26.
- **free-and-premium:** the 7-day trial on the annual plan matches the StoreKit configuration and the site. Confirm it in App Store Connect (prices and the original Premium Version purchase are confirmed on the App Store listing).
- **get-free-sheet-music:** the catalog is described as classical public-domain scores. Confirm nothing else is in the 4.3 catalog.
- **import-didnt-work:** whether Import Folder skips iCloud Drive files that aren't downloaded. The guide says they "may be skipped".
- **use-music-folder-on-a-mac:** the minimum macOS for 4.3 (iOS 17 target, probably macOS 14), and whether macOS 14 gets the tab bar instead of the sidebar. The guide names no macOS version.

## Not blocking: app behaviour worth a look (the guides describe current behaviour or leave it out)

- **library-looks-empty-after-reinstalling:** after a reinstall, "Restoring Library" never appears (the piece count lives in settings the reinstall erases), so people see empty screens while iCloud downloads.
- **join-a-shared-folder-or-set-list:** the Leave alert says notes and markings are "kept for 30 days in case you rejoin", but nothing deletes them (R110). The guide omits the 30 days.
- **connect-planning-center:** Clear Cached Files warns that annotations on Planning Center PDFs are removed, but that ink now lives in annotation layers. The guide doesn't repeat the warning.
- **create-a-chord-chart, import-didnt-work:** chord chart files (.cho, .chordpro, .chopro, .pro, .crd, .txt) can be imported by drag and drop, but Info.plist doesn't register them for Open In, AirDrop or the share sheet. The guides document drag and drop and pasting only.
- **import-didnt-work:** a PDF in a batch that can't be read seems to be saved as a piece with no pages.
- **import-music:** several plain PDFs sent at once by AirDrop or Open In open the Add Music form one after another (not documented).
- **edit-or-delete-a-piece:** no supported way to replace a library piece's whole PDF in 4.3 ("Replace Sheet Music" is unreachable). Not documented.
- **keep-notes-on-a-piece:** whether the notes panel's "Only on your devices" caption shows for 4.3 shared pieces. Not documented.
- **cant-hear-the-metronome-or-a-recording:** what Play does when no recording has downloaded yet. Not named.
- **mark-up-music-with-apple-pencil:** annotating with a mouse or trackpad on Mac. Not documented.

## Resolved in this review

- Prices ($2.99 a month, $19.99 a year, $49.99 lifetime) and the original $4.99 Premium Version purchase match the App Store listing; "bought the original one-time Premium upgrade before 3.0" is the right wording.
- Music Folder is available on Mac (App Store listing: Mac with Apple M1 or later).
- iCloud Sync row "Off" → quit and reopen: the code attaches CloudKit on the next launch once the store exists.
- Convert to Chord Chart as an optional toolbar tool is verified in code; kept in the guide.
- Recently Removed entry points, owner-only Delete Permanently after 30 days, Previous Version (shared pieces, 30 days) and Remove from Set List not going to Recently Removed are confirmed in code (R102, R110, R145).
