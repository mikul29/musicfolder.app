---
{
 "slug": "use-performance-mode",
 "h1": "Use Performance Mode",
 "seo_title": "Performance Mode for Playing Sheet Music Live | Music Folder",
 "description": "Use Performance Mode on stage: the toolbars hide, taps and pedals only turn pages, and nothing on the page can be changed by accident until you leave.",
 "intent": "existing",
 "intent_note": "A performer who wants a distraction-free, accident-proof reader for a gig or service, or who is stuck in Performance Mode and wants to leave.",
 "searches": ["stage mode", "gig mode", "full screen", "lock screen", "hide toolbar", "accidental page turn", "exit performance mode", "perform set", "double turn"],
 "availability": [],
 "related": ["play-a-set-list", "turn-pages", "turn-pages-hands-free", "keep-notes-on-a-piece"],
 "feature_link": {"href": "/features/sheet-music-reader", "text": "the Sheet Music Reader"},
 "documents": ["PDF Reader/PerformanceMode.swift", "PDF Reader/PerformanceModeController.swift", "App/PerformanceModeSettingsView.swift", "Set Lists/Songs View/SetListSummaryPanel.swift", "R41"],
 "verified": "76048e78",
 "differs_from_4_2": null,
 "shots": [
  {"id": "performance-mode-ipad", "kind": "screen", "device": "ipad", "orientation": "portrait",
   "state": "Sicilienne (Fauré) open in Performance Mode: no navigation bar or status bar, the page filling the screen, and the capsule at the top right with Notes, the Metronome cell showing 50, Play and Done. A Page Link marker may be visible on the page.",
   "alt": "A page of sheet music filling an iPad screen with no toolbar, and a small capsule in the top-right corner holding Notes, Metronome, Play and Done buttons.",
   "caption": null,
   "reuse": "reader-perform-ipad.jpg"}
 ],
 "open_questions": []
}
---
Performance Mode is the reader for playing on stage or in a service. The toolbars and status bar disappear, the page gets the whole screen, and a touch on the page can only turn it, so nothing opens, zooms or gets marked up by accident in the middle of a piece.

{shot:performance-mode-ipad}

## Start Performance Mode

- **In any reader:** choose **⋯ › Performance Mode**. It's the first item in the menu.
- **From a set list:** tap **Perform Set**. The set list starts from its first item in Performance Mode. Tapping an item in the list opens it in the regular reader instead.
- **From the toolbar:** if you play this way often, add the {sf:arrow.up.left.and.arrow.down.right} **Performance Mode** button to the toolbar (see [The reader at a glance](/guide/the-reader-at-a-glance)).

Performance Mode lasts until you leave it, through every piece of a set list or Planning Center plan, and the reader opens normally the next time.

## Turn pages in Performance Mode

- Tap the right two thirds of the page to go forward, and the left third to go back.
- Swipe left or up for the next page, and right or down for the previous one.
- Pedals, keyboards and Face Gestures turn pages as usual.

Half-Page Turns and Page Links keep working: with Half-Page Turns on, each turn moves half a page, and tapping a link's marker still jumps. Pinching doesn't zoom unless you turn on **Allow Pinch to Zoom** in the settings below.

## Use tools while you perform

A small capsule in the top-right corner holds the tools you've allowed, which by default are Notes, Metronome and Audio Playback. Tap one to use it as you would on the toolbar. Notes open read-only, so you can see your notes but not change them on stage. A tool the current piece can't use is dimmed rather than removed, so the capsule doesn't shift between pieces.

The audio player, the cue label from your notes and the Up Next banner in a set list stay on screen. Anything already playing, such as a recording or the metronome, keeps playing when you enter or leave the mode.

## Leave Performance Mode

Touch and hold **Done** in the capsule. A quick tap only shows "Hold to Exit", so a stray touch can't take you out mid-piece. With a keyboard, you can also press Escape.

When you leave, the toolbars come back, and you stay on the same page at the same zoom.

## Change Performance Mode settings

Go to **Account › Preferences › Performance Mode**. The settings apply every time you use the mode.

- **Available Tools:** choose which of Notes, Tuner, Metronome, Audio Playback and Piano appear in the capsule.
- **Prevent Double Turns:** ignores a second tap or pedal press within half a second of a turn, so a bouncing pedal or a nervous double tap turns one page, not two. It's on by default.
- **Allow Pinch to Zoom:** lets you pinch to zoom in on the page while performing. It's off by default.
