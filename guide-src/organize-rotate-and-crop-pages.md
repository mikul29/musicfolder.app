---
{
 "slug": "organize-rotate-and-crop-pages",
 "h1": "Organize, rotate and crop pages",
 "seo_title": "Reorder, Rotate and Crop PDF Pages | Music Folder",
 "description": "Reorder, rotate, duplicate and remove the pages of a piece, add blank or staff paper and pages from another piece, and crop away wide margins.",
 "intent": "existing",
 "intent_note": "Musicians fixing a scan (sideways pages, wrong order, extra pages) or trimming margins so the music fills the screen.",
 "searches": [
  "rotate page",
  "reorder pages",
  "delete page",
  "remove page",
  "move pages",
  "insert page",
  "blank page",
  "staff paper",
  "manuscript paper",
  "crop",
  "margins",
  "trim",
  "zoom",
  "merge pdfs",
  "combine pdfs"
 ],
 "availability": [],
 "related": [
  "edit-or-delete-a-piece",
  "import-music",
  "change-the-page-view",
  "add-sections-to-a-book"
 ],
 "feature_link": null,
 "documents": [
  "Shared UI/SheetsManagerViewController.swift",
  "Shared UI/SheetTemplates.swift",
  "Shared UI/SongPagesPickerViewController.swift",
  "Services/SongPagesImport.swift",
  "Services/SheetPageEdits.swift",
  "PDF Reader/PDFCropEditorViewController.swift",
  "PDF Reader/PDFCrop.swift",
  "Services/PDFCropStore.swift",
  "PDF Reader/PDFReaderToolbar.swift (Crop Margins…)",
  "Shared UI/AddSongFormViewController.swift (Organize Pages row)",
  "R35",
  "R36",
  "R37"
 ],
 "verified": "76048e78",
 "differs_from_4_2": null,
 "shots": [
  {
   "id": "organize-pages",
   "kind": "screen",
   "device": "ipad",
   "orientation": "portrait",
   "state": "Organize Pages for Mozart's Quartet in D, K. 155 (8 pages).",
   "alt": "Organize Pages for an eight-page score: numbered page thumbnails with remove buttons, the Add Pages tile, and the crop, select and add buttons at the top.",
   "caption": null,
   "reuse": null
  },
  {
   "id": "crop-editor",
   "kind": "crop",
   "device": "ipad",
   "orientation": "portrait",
   "state": "Crop All Pages opened from the reader's ⋯ › Page Display & Layout › Crop Margins… on Fauré's Sicilienne: orange edge handles around the page, This Page / All Pages switch, Auto and Reset buttons, 'Page 1 of 1'.",
   "alt": "The crop editor showing a page of guitar music with orange handles on each edge and Auto and Reset buttons below.",
   "caption": null,
   "reuse": "reader-crop-ipad.jpg"
  }
 ],
 "open_questions": []
}
---
Organize Pages lets you fix the pages of a piece: put them in the right order, turn sideways scans upright, duplicate or remove pages, and add new ones. Crop Margins trims wide white margins so the music is larger on screen.

## Open Organize Pages

1. Touch and hold the piece in your library and choose **Edit Details**.
2. Under **Pages**, tap **Organize Pages**. You can also tap the cover at the top of the form.

{shot:organize-pages}

Your changes are kept with the form. When you're done, go back and tap the checkmark on **Edit Music** to save them; closing the form without saving discards them. Markings and sections move with their pages when you reorder, so they stay on the music they belong to.

## Reorder, rotate, duplicate or remove pages

- **Reorder**: drag a page to a new position.
- **View a page**: tap it. The preview has buttons to remove, rotate, crop and duplicate that page.
- **Rotate or duplicate**: touch and hold a page (or right-click it on a Mac) and choose **Duplicate**, **Rotate Left** or **Rotate Right**.
- **Remove**: tap the {sf:xmark} badge in the page's corner, or touch and hold it and choose **Remove**.

The big orange numbers show the order on these thumbnails only; they're never added to the PDF.

### Change several pages at once

1. Tap {sf:checkmark.circle} **Select**.
2. Tap the pages you want, or tap **Select All**.
3. In the toolbar, tap **Duplicate**, **Rotate Left**, **Rotate Right**, **Crop** or **Remove**.
4. Tap **Done**.

## Add pages

Tap {sf:plus} (**Add Pages**), or the add tile after the last page, and choose:

- **Files**, **Photos** or **Scan**: pages from a PDF, from pictures, or from the document scanner. **Scan** appears only on devices with a camera.
- **From Another Piece…**: copies all the pages of another piece in your library, with its markings, to the end of this one. The other piece isn't changed. The copied pages arrive uncropped, and a chord chart arrives as fixed pages in its original key.
- **Blank Page**: **White** or **Black**.
- **Staff Paper**: **White** or **Black**.

On Mac: the menu shows full names, such as **Import from Files**, **Black Page** and **Black Staff Paper**.

## Crop margins

Cropping hides the white space around the music so it's larger on screen. It changes only how the page is shown: the PDF itself is never changed, and your markings stay where you drew them.

From the reader:

1. Choose **⋯ › Page Display & Layout › Crop Margins…**.
2. Choose **This Page** or **All Pages**.
3. Drag an edge of the frame, or tap **Auto** to find the margins for you. **Reset** removes the crop.
4. Use the arrows below the page to check the crop on the other pages.
5. Tap the checkmark. The crop is saved right away.

{shot:crop-editor}

In Organize Pages you can crop too: tap {sf:crop} **Crop All Pages**, touch and hold a page and choose **Crop Page…**, or select several pages and tap **Crop**. Crops made there are saved with the form, like your other page changes.

Crops sync to your other devices and are included in your backups. When you share a piece as a PDF, the PDF shows the cropped pages; a Music Folder file keeps the original pages. Crops are never shared with collaborators.
