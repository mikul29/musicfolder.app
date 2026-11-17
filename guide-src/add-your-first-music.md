---
{
 "slug": "add-your-first-music",
 "h1": "Add your first music",
 "seo_title": "Add Your First Sheet Music PDF | Music Folder",
 "description": "Import your first sheet music PDF into Music Folder from the Files app, check its title in the Add Music form, and open it in the reader.",
 "intent": "general",
 "intent_note": "A new user (or someone with a PDF score and an iPad) who wants the shortest path from a file to reading it in the app.",
 "searches": [
  "import pdf",
  "add pdf",
  "open pdf",
  "first piece",
  "files app",
  "get started"
 ],
 "availability": [
  {
   "kind": "premium",
   "text": "Free includes up to 15 pieces; Premium has no limit."
  }
 ],
 "related": [
  "import-music",
  "get-free-sheet-music",
  "the-reader-at-a-glance",
  "edit-or-delete-a-piece"
 ],
 "feature_link": null,
 "documents": [
  "Shared UI/SongListViewController.swift",
  "Shared UI/AddSongFormViewController.swift",
  "Sharing/ReviewImportViewController.swift",
  "App/HomeView.swift",
  "App/MainMenu.swift",
  "Sharing/SongMetadataAnalyzer.swift",
  "R5"
 ],
 "verified": "76048e78",
 "differs_from_4_2": null,
 "shots": [
  {
   "id": "add-first-music-menu",
   "kind": "crop",
   "device": "ipad",
   "orientation": "landscape",
   "state": "Library › Music on iPad with the + button tapped: the Add to Library menu open below it, showing the Files / Photos / Folder row, Scan Sheet Music and New Chord Chart. Crop to the menu and the top of the list.",
   "alt": "The Add to Library menu open from the + button, with Files, Photos and Folder, then Scan Sheet Music and New Chord Chart.",
   "caption": null,
   "reuse": null
  }
 ],
 "open_questions": []
}
---
The quickest way to start is to import a PDF you already have, such as a score you downloaded or a part your director emailed you. Save it somewhere in the Files app first, such as iCloud Drive or Downloads, then follow these steps.

## Import a PDF from Files

{shot:add-first-music-menu}

1. Open the Library. On iPhone, tap the **Library** tab, then **Music**. On iPad, tap **Music** under **Library** in the sidebar (with iPadOS 17, use the **Library** tab as on iPhone).
2. Tap {sf:plus} at the top of the list.
3. In the **Add to Library** menu, tap **Files**.
4. Find your PDF and tap it.
5. The **Add Music** form opens with the file's name as the title (marked "from file"). Change the title if you like, and add a composer.
6. Tap {sf:checkmark} to add the piece.

The piece now appears in your Music list. Tap it to open it in the reader, and swipe to turn pages. Tap the back button to return to the list.

Tip: On a device with Apple Intelligence and iOS 26 or later, the form can also fill in a title, composer, key, tempo or time signature printed on the first page. Anything it can't read stays blank, so check the details before you save.

If your library is still empty, Home shows an **Import from Files** button that does the same thing. When you import a single piece from there, it opens in the reader as soon as you save it.

## Add several files at once

In the Files picker, tap **Select**, choose the PDFs you want, then tap **Open**. Instead of the Add Music form, you'll see a list titled **Add 3 Pieces** (or however many you picked). Check the titles, choose a folder for them if you like, then tap {sf:checkmark}.

On Mac: in the **Add to Library** menu the item is called **Import from Files**. You can also choose **File › Import PDF…** in the menu bar (Command-N), or drag PDFs from the Finder onto the Music list. One PDF opens the Add Music form, and several open the list described above.

## Other ways to add music

The **Add to Library** menu also offers **Photos**, **Folder** (a whole folder of PDFs at once), **Scan Sheet Music** for paper scores (on devices with a camera) and **New Chord Chart**. You can also open a PDF from another app with the share sheet or AirDrop. [Import music](/guide/import-music) covers each of these, and [Get free sheet music](/guide/get-free-sheet-music) shows how to add public-domain scores from the built-in catalog.

Note: The free version holds up to 15 pieces, 5 sections and 1 folder. See [Free and Premium](/guide/free-and-premium).
