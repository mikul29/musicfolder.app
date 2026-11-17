---
{
 "slug": "page-turner-isnt-turning-pages",
 "h1": "My page turner isn't turning pages",
 "seo_title": "Fix a Page Turner Pedal That Won't Turn Pages | Music Folder",
 "description": "Bluetooth page turner pedal not turning pages in Music Folder? Test the pedal, set the right mode, swap directions and find what's pausing turns.",
 "intent": "troubleshooting",
 "intent_note": "Musicians with an AirTurn, PageFlip, Donner or similar pedal that doesn't turn pages in the app.",
 "searches": [
  "pedal not working",
  "airturn",
  "pageflip",
  "donner pedal",
  "bluetooth pedal",
  "foot pedal",
  "page turn pedal",
  "pedal turns wrong way",
  "media mode"
 ],
 "availability": [],
 "related": [
  "turn-pages-hands-free",
  "turn-pages",
  "use-performance-mode",
  "the-reader-at-a-glance"
 ],
 "feature_link": {
  "href": "/features/page-turner",
  "text": "page turning in Music Folder"
 },
 "documents": [
  "PDF Reader/PageTurnerKeys.swift (key map, acceptsTurn, reclaimPageTurnerFocus, PageTurnerTestReading)",
  "App/PageTurnerSettingsView.swift",
  "App/AccountView.swift (Preferences › Page Turner)",
  "PDF Reader/PerformanceMode.swift (TurnDebouncer, Prevent Double Turns)",
  "App/PerformanceModeSettingsView.swift",
  "PDF Reader/HalfPageTurn.swift",
  "PDF Reader/PDFReaderToolbar.swift (Half-Page Turns menu item)",
  "PDF Reader/PDFAnnotationSession.swift (Done Annotating)",
  "Tools/CompactToolSheetPresenter.swift",
  "R50",
  "R41",
  "R39"
 ],
 "verified": "76048e78",
 "differs_from_4_2": null,
 "shots": [],
 "open_questions": []
}
---
A Bluetooth page turner pedal connects to your iPad, iPhone or Mac as a keyboard, and each press sends a key. Music Folder turns the page when it receives one of the keys page turners send. If pressing the pedal does nothing, the pedal is usually not connected, set to a mode the app doesn't use, or something open in the reader is holding the key presses. Start by testing the pedal, which tells you which of these it is.

## Test the pedal

The Page Turner screen shows what the app receives from your pedal, without turning any pages.

1. Open **Account**, then tap **Page Turner** under **Preferences**.
2. Press each pedal and read the line under **Test Your Pedal**, for example "Right Arrow → Next Page".

What you see tells you what to do next:

- **Nothing changes:** the pedal isn't connected to this device. See "Pair the pedal" below.
- **Not a page-turn key:** the pedal is connected, but in a mode Music Folder doesn't use. See "Set the pedal's mode" below.
- **The directions are reversed:** turn on **Swap Forward and Back** on the same screen. It also swaps the arrow keys on a keyboard.
- **Next Page and Previous Page appear as expected:** the pedal is fine. See "Check what's open in the reader" below.

## Pair the pedal

Pedals pair in Settings › **Bluetooth** (System Settings › **Bluetooth** on Mac), not inside Music Folder.

1. Turn the pedal on and put it in pairing mode, as its instructions describe.
2. Select it in the Bluetooth settings and wait until it shows as connected.
3. If you've used the pedal with another device, make sure it hasn't reconnected to that one. Turn Bluetooth off on the other device, or disconnect the pedal there.
4. If the pedal connects and drops, replace or charge its batteries.

## Set the pedal's mode

Most pedals have several modes, and only some of them send keys Music Folder understands. Pedals in media or volume mode, which send play, pause or volume commands, aren't supported. Set your pedal to an Arrow or Page Up/Down mode. How you change the mode depends on the pedal, so check its instructions.

These keys turn pages:

- Next page: Right Arrow, Down Arrow, Page Down or Space
- Previous page: Left Arrow, Up Arrow, Page Up, Enter or Shift-Space

## Check what's open in the reader

A pedal turns pages in the reader: a piece, a set list you're playing, or a Planning Center plan. Turns are paused while something else needs the keys or the page:

- **You're annotating.** Tap the highlighted pencil to finish annotating.
- **You're typing in the notes panel.** Finish the note first, because key presses go into the text.
- **You're customizing the toolbar.** Finish customizing first.
- **A sheet or popover is open over the music**, such as the metronome or the tuner. Close it.

The reader takes the pedal back when you finish. If it still doesn't respond, go back to your music and open the piece again.

## If the pedal turns, but not the way you expect

- **A quick second press is ignored in Performance Mode.** With **Prevent Double Turns** on, a second press within half a second is ignored, so a pedal bounce doesn't skip a page. You can change it in **Account › Preferences › Performance Mode**.
- **Each press moves half a page.** That's **Half-Page Turns**, which shows the top of the next page before the full turn. Turn it off in **⋯ › Page Display & Layout › Half-Page Turns**.
- **The direction is wrong.** Turn on **Swap Forward and Back** in **Account › Preferences › Page Turner**.

## Contact us

If your pedal still doesn't turn pages, [contact us](/contact). It helps to include:

- The pedal's make, model and the mode it's set to
- What the **Test Your Pedal** line shows when you press each pedal
- Where you're reading (a piece, a set list or a Planning Center plan) and what's on screen
- Your device, its iOS, iPadOS or macOS version, and the Music Folder version (**Account › About › Version**)
