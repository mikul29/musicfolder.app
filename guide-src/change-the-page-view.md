---
{
 "slug": "change-the-page-view",
 "h1": "Change the page view",
 "seo_title": "Scroll, Two-Page View and Dark Sheet Music | Music Folder",
 "description": "How to scroll through sheet music vertically, show two pages side by side on iPad and Mac, or read light notation on a dark background.",
 "intent": "existing",
 "intent_note": "A user who wants continuous scrolling, a two-page spread like an open book, or a dark page for low-light stages.",
 "searches": ["vertical scroll", "continuous scroll", "two page", "side by side", "spread", "book view", "dark mode", "night mode", "invert colors", "black background", "landscape"],
 "availability": [],
 "related": ["turn-pages", "organize-rotate-and-crop-pages", "the-reader-at-a-glance", "use-performance-mode"],
 "feature_link": {"href": "/features/sheet-music-reader", "text": "the Sheet Music Reader"},
 "documents": ["PDF Reader/PDFReaderToolbar.swift", "PDF Reader/TwoPageSpread.swift", "PDF Reader/SheetMusicAppearance.swift", "Songs/Song View/SongPDFView.swift", "Set Lists/Songs View/PDFViewInSetList.swift", "Planning Center/PCOPDFViewController.swift", "R45", "R52"],
 "verified": "76048e78",
 "differs_from_4_2": null,
 "shots": [],
 "open_questions": []
}
---
You can scroll through sheet music vertically, show two pages side by side, or read light notation on a dark background. These options are in **⋯ › Page Display & Layout**, and each is a setting you choose once: it stays on for every piece you open, in every reader that offers it, until you turn it off. A checkmark shows which ones are on.

The same menu has **Half-Page Turns**, described in [Turn pages](/guide/turn-pages), and **Crop Margins**, which trims the white border around pages; see [Organize, rotate and crop pages](/guide/organize-rotate-and-crop-pages).

## Scroll through pages vertically

Out of the box, the reader shows one page at a time and you swipe sideways to turn. With Vertical Scrolling, the pages form one continuous column that you scroll up and down, like a long document.

1. Open a piece and choose **⋯ › Page Display & Layout**.
2. Choose **Vertical Scrolling**.

Choose it again to go back to one page at a time. Vertical Scrolling is available for single pieces and for Planning Center music. When you play one of your own set lists, pages always turn one at a time.

While Vertical Scrolling is on, Two-Page View and Half-Page Turns are dimmed in the menu with "Turn off Vertical Scrolling to use". Your choice for them is kept for when you turn Vertical Scrolling off. On iPhone, the bottom toolbar's tools move to the top bar while Vertical Scrolling is on.

## Show two pages side by side

On iPad and Mac, Two-Page View shows pages in pairs like an open book: pages 1 and 2, then 3 and 4, with no separate cover page. Each turn moves to the next pair.

1. Open a piece and choose **⋯ › Page Display & Layout**.
2. Choose **Two-Page View**.

Two pages appear only when there's room for both at a readable size: an iPad held in landscape, or a wide Mac window. When you rotate to portrait, use Split View or make the window narrower, the reader goes back to one page, and the pair returns when there's room again. You don't need to turn the setting off and on.

Two-Page View is for single pieces with at least two pages. Pieces whose pages are wider than they are tall stay one page at a time. Two-Page View isn't offered on iPhone, and it doesn't apply while Vertical Scrolling is on. Half-Page Turns pause while two pages are showing.

## Read on a dark background

Dark Background shows light notation on a dark page, which is easier on your eyes on a dark stage or in a dim room. In your markings, black ink shows light and colors such as a yellow highlight stay as they are. Chord charts are drawn in dark colors too.

1. Open a piece and choose **⋯ › Page Display & Layout**.
2. Choose **Dark Background**.

Dark Background works in every reader: single pieces, set lists and Planning Center plans. To switch it with one tap, add the {sf:circle.lefthalf.filled.inverse} **Dark Background** button to the toolbar (see [The reader at a glance](/guide/the-reader-at-a-glance)). The button is highlighted while the dark background is on.

Dark Background changes only what you see in the reader. Your PDFs aren't changed, and page thumbnails, Organize Pages, exported PDFs and the copies you send stay light.

Note: Dark Background is separate from **Dark Mode** in **Account › Preferences**, which changes the look of the rest of the app (lists, menus and screens), not the page of music.
