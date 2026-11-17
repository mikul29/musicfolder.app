---
{
 "slug": "transpose-capo-and-numbers",
 "h1": "Transpose, capo and numbers",
 "seo_title": "Transpose Chords, Capo and Nashville Numbers | Music Folder",
 "description": "Change a chord chart's key, show capo chord shapes, switch to Nashville numbers or lyrics only, and change the text size, without changing the chart itself.",
 "intent": "general",
 "intent_note": "Guitarists, keyboard players and worship leaders who need to transpose chords to a singer's key, play with a capo, or read the number system; existing users looking for the Key control.",
 "searches": [
  "transpose",
  "change key",
  "capo",
  "nashville number system",
  "numbers",
  "chord numbers",
  "lyrics only",
  "hide chords",
  "key change",
  "text size",
  "bigger chords"
 ],
 "availability": [
  {
   "kind": "premium",
   "text": "Choosing another key or a capo needs Premium. Every chart shows in its saved key for free."
  }
 ],
 "related": [
  "create-a-chord-chart",
  "format-a-chord-chart",
  "play-a-service-plan",
  "free-and-premium"
 ],
 "feature_link": {
  "href": "/features/chord-charts",
  "text": "chord charts in Music Folder"
 },
 "documents": [
  "Chords/ChordKeyControl.swift",
  "Chords/ChartKeyAccess.swift",
  "Chords/Transposer.swift (CapoAdvisor, CapoDescription, NashvilleFormatter)",
  "Chords/ChartViewState.swift",
  "Chords/ChartReaderSession.swift",
  "App/MainMenu.swift (Chart menu)",
  "PDF Reader/PDFReaderToolbar.swift (ReaderKeyToolPolicy)",
  "Premium/PremiumPaywallView.swift",
  "R25",
  "R28",
  "R53"
 ],
 "verified": "76048e78",
 "differs_from_4_2": null,
 "shots": [
  {
   "id": "key-control",
   "kind": "crop",
   "device": "ipad",
   "orientation": "landscape",
   "state": "Amazing Grace open in the song reader as a chord chart, with the Key control popover open: G shown as the original key, the key grid with G selected, Capo set to None, Show set to Chords. Crop to the popover with a little of the chart beside it.",
   "alt": "The Key control open over a chord chart, with G as the original key selected in the key grid, Capo set to None and Show set to Chords.",
   "caption": null,
   "reuse": null
  }
 ],
 "open_questions": []
}
---
The Key control changes how a chord chart is shown to you: in another key, with capo shapes, as Nashville numbers, or as lyrics only. None of it changes the chart itself, so you can transpose for tonight's singer and still have the chart in its written key tomorrow.

## Change the key

1. Open a chord chart.
2. Tap **Key** in the toolbar. The button shows the key you're seeing, for example **Key: G**.
3. Tap a key in the grid. The chart is redrawn in that key at once.

{shot:key-control}

Each row of the grid has a key's flat, natural and sharp names, so choosing A♯ or B♭ also chooses whether the chart is spelled with sharps or flats. The key the chart is written in has an orange outline; tap it to go back to the original key.

On iPad and Mac the Key control opens as a popover. On iPhone, and in a narrow iPad window, it opens as a sheet at the bottom of the screen, so you can still see the chart.

With a keyboard, press Command-T to transpose up a half step, Shift-Command-T to transpose down, and Command-0 to go back to the original key. On iPad and Mac these are also in the **Chart** menu.

The **Key** button appears only while a chord chart is on screen. If a piece has both a PDF and a chart and you're looking at the PDF, choose **⋯ › Show › Chord Chart**. In a set list, the button shows on the chord chart pages and hides on the others.

If the chart has no written key, the Key control shows a note asking you to set one instead of the key grid. Open the chart with **⋯ › Edit Chord Chart**, tap **Original Key** and choose the key.

## Play with a capo

Tap the **Capo** menu in the Key control and choose a fret. Each choice also shows the chord shapes you'll play, for example "2 in C" means a capo on the second fret, playing C shapes. The easiest shapes are listed first.

The chart then shows the chords as you'll finger them, and a capo tile in the chart's header reminds you where the capo goes. Turn off **Highlight Capo** if you don't want that tile tinted; like the chart's formatting, this setting applies to every chart that follows your default formatting unless the chart has formatting of its own. To take the capo off, choose **No capo**.

## Show numbers or lyrics only

Use **Show** at the bottom of the Key control:

- **Chords** shows chord names.
- **Numbers** shows the chords in the Nashville number system, counted from the chart's written key. A capo or a different key doesn't change the numbers.
- **Lyrics** hides the chords and keeps the lyrics, for singers.

**Numbers** isn't available until the chart has a written key.

## Change the text size

With a keyboard, press Command-Plus or Command-Minus to make a chart's text bigger or smaller (also in the **Chart** menu on iPad and Mac). To set a chart's text size precisely, use **Size** in the chart's formatting; see [Format a chord chart](/guide/format-a-chord-chart). You can also pinch to zoom the page, as with any PDF.

## What changes and what doesn't

The key, capo and display you choose are remembered for that chart, and the reader opens it the same way next time. The chart's text stays exactly as it was written. When you share or print a chart, it goes out in its written key.

In the chord chart editor, the **Shown as** button above the preview opens the same Key control for the preview. To change the key the chart is written in, use **Original Key** in the editor instead.

Planning Center chord charts open in the key of the service plan. You can transpose them the same way; see [Play a service plan](/guide/play-a-service-plan).

## Free and Premium

Every chord chart shows in its saved key (or a Planning Center plan's key) for everyone. With the free version, tapping another key, choosing a capo, or pressing Command-T or Shift-Command-T opens the upgrade screen, and the chart stays as it is. Going back to the original key, **Numbers**, **Lyrics**, text size, Follow Sequence and formatting are free. See [Free and Premium](/guide/free-and-premium).
