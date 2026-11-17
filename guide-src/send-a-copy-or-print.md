---
{
 "slug": "send-a-copy-or-print",
 "h1": "Send a copy or print",
 "seo_title": "Send or Print Sheet Music and Set Lists | Music Folder",
 "description": "Send a piece, folder or set list as a Music Folder file or a PDF, choose which markings go with it, print it, and open a copy someone sends you.",
 "intent": "existing",
 "intent_note": "A musician who wants to send music to a bandmate, email a set list as a PDF, or print a part, and needs to know what the other person receives.",
 "searches": [
  "export",
  "email sheet music",
  "airdrop",
  "share as pdf",
  "print set list",
  "mfsong",
  "mfsetlist",
  "mfgroup",
  "send to band",
  "export annotations"
 ],
 "availability": [],
 "related": [
  "share-a-folder-or-set-list",
  "mark-up-music-with-apple-pencil",
  "use-annotation-layers",
  "import-music"
 ],
 "feature_link": {
  "href": "/features/sharing",
  "text": "sharing in Music Folder"
 },
 "documents": [
  "Sharing/ShareSupport.swift",
  "App/CollectionShareMenu.swift",
  "App/SharedSendCopy.swift",
  "Sharing/SongSharing.swift",
  "Sharing/GroupSharing.swift",
  "Sharing/SetListSharing.swift",
  "Chords/ChartSharing.swift",
  "Sharing/AnnotationLayerTransport.swift",
  "Songs/Song View/SongListScreen.swift",
  "App/SceneDelegate.swift",
  "R25",
  "R32",
  "R42",
  "R127"
 ],
 "verified": "76048e78",
 "differs_from_4_2": "In 4.2, a folder or set list had its own Share button that asked for the format. In 4.3 it's Share Folder or Share Set List › Send Copy › Music Folder File or PDF, next to Collaborate. Anyone in a Shared Folder or Shared Set List can also send a copy of it. Sending a single piece works as before.",
 "shots": [
  {
   "id": "send-copy-format-picker",
   "kind": "crop",
   "device": "ipad",
   "orientation": "landscape",
   "state": "Song reader, ⋯ › Share tapped: the popover offers Share with Music Folder Users and Share as PDF.",
   "alt": "The Share popover for a piece, offering Share with Music Folder Users and Share as PDF.",
   "caption": null,
   "reuse": null
  }
 ],
 "open_questions": [
  "Opening a received file from the Files app: Info.plist declares Music Folder the Owner of the .mfsong and .mfsetlist types (check .mfgroup / .mfsongs too). Confirm on a device that tapping each file type in Files opens Music Folder directly, so the guide's hedge \"choose Music Folder if you're asked\" can be dropped. App/SceneDelegate.swift, MyBandProject/Info.plist."
 ]
}
---
You can send any piece, folder or set list to another musician as a copy. A **Music Folder file** opens in Music Folder with the piece's details, sections and markings; a **PDF** opens anywhere and can be printed. Sending a copy is free, and the person who receives it gets their own copy that doesn't change when yours does. To work on the same music together instead, see [Share a folder or set list](/guide/share-a-folder-or-set-list).

## Send a piece

1. Open the piece.
2. Tap **⋯**, then tap **Share**. If you've put {sf:square.and.arrow.up} **Share** on the toolbar, you can tap it there instead.
3. Choose **Share with Music Folder Users** or **Share as PDF**.
4. Choose how to send it in the share sheet, for example AirDrop, Messages or Mail.

To send several pieces at once, go to **Library › Music**, tap **⋯**, then tap **Select**. Select the pieces, tap {sf:square.and.arrow.up} in the toolbar, then choose the format.

{shot:send-copy-format-picker}

## Send a folder or set list

1. In **Library**, open **Folders** or **Set Lists**.
2. Touch and hold the folder or set list.
3. Choose **Share Folder** or **Share Set List**, then **Send Copy**.
4. Choose **Music Folder File** (for people who use Music Folder) or **PDF** (for anyone).
5. Choose how to send it in the share sheet.

You can also send a copy from inside the folder (tap **⋯**, then **Share Folder › Send Copy**) or inside the set list (tap {sf:square.and.arrow.up} **Share**, then **Send Copy**).

A set list sent as a PDF is one file with every piece and set-list page in order. A folder sent as a PDF is one PDF per piece.

## What goes with each format

A **Music Folder file** carries each piece's PDF or chord chart, its details (title, composer, key, tempo, time signature, duration), its sections, and all of your annotation layers, including layers you've hidden. The person who opens it can show, hide and edit those layers. A single piece also carries its notes and its recordings, and a set list carries the notes on its pieces and its set-list pages. A folder, or several pieces sent together, doesn't include notes or recordings. Chord charts travel in their written key: your transposition, capo and text size are your own view and stay with you.

A **PDF** is the music as you see it. Only the layers you have visible are drawn into the pages; hidden layers are left out, and the markings can't be edited by the recipient. Cropped margins are kept as you set them. A piece that's only a chord chart is drawn in the key you're currently showing. Notes and recordings aren't included in a PDF.

## Print music

1. Send the piece, folder or set list as a PDF, following the steps above.
2. In the share sheet, tap **Print**.

To print without your markings, hide their layers first (see [Use annotation layers](/guide/use-annotation-layers)). A set list prints as one document, in set order.

## Send a copy of a Shared Folder or Shared Set List

Anyone in a Shared Folder or Shared Set List can send a copy of it, whatever their permission. Touch and hold it in your list (or open it and tap **⋯**), choose **Share Folder** or **Share Set List** › **Send Copy**, then choose the format. The copy contains the pieces as they are now, with only your own markings (and, in a set list file, your own notes). Other members' personal markings are never included.

Pieces that aren't on your device yet are downloaded first. If some can't be downloaded, the app says "Some pieces aren't downloaded yet" and nothing is sent; connect to the internet and try again. If a piece you have open has an update waiting, close it or tap **Show** first.

To send only some pieces from a Shared Folder, tap **⋯**, then **Select**, select them and tap {sf:square.and.arrow.up}. Pieces selected in a shared folder are sent as PDFs.

## Open a copy someone sends you

Open the file on your iPhone, iPad or Mac from AirDrop, Messages, Mail or the Files app, and choose Music Folder if you're asked which app to use. Music Folder adds it to your library:

- A single piece opens in the reader.
- A folder appears in **Folders** and a set list in **Set Lists**, with their pieces added to your library.
- If something with the same name is already in your library, you can choose **Open Existing** or **Import as Duplicate**.

The pieces you receive count toward the free limits. If a file holds more than the free version allows, the app explains and offers Premium; nothing is added.
