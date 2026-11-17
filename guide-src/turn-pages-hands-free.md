---
{
 "slug": "turn-pages-hands-free",
 "h1": "Turn pages hands-free",
 "seo_title": "Turn Sheet Music Pages Hands-Free | Music Folder",
 "description": "Use a Bluetooth page turner pedal, or a head turn, wink or mouth movement with Face Gestures, to turn sheet music pages without using your hands.",
 "intent": "general",
 "intent_note": "Musicians looking for a page turner pedal setup or a hands-free way to turn pages while playing; also users testing a new pedal.",
 "searches": [
  "page turner pedal",
  "bluetooth pedal",
  "foot pedal",
  "airturn",
  "pageflip",
  "donner",
  "head turn",
  "wink",
  "face gestures",
  "hands free",
  "swap pedal direction"
 ],
 "availability": [
  {
   "kind": "premium",
   "text": "Bluetooth pedals are free. Setting up and trying Face Gestures is free; using them with your music needs Premium."
  },
  {
   "kind": "device",
   "text": "Face Gestures need an iPhone or iPad whose front camera can track a face. They aren't available on Mac."
  }
 ],
 "related": [
  "turn-pages",
  "use-performance-mode",
  "page-turner-isnt-turning-pages",
  "free-and-premium"
 ],
 "feature_link": {
  "href": "/features/page-turner",
  "text": "page turning in Music Folder"
 },
 "documents": [
  "PDF Reader/PageTurnerKeys.swift",
  "App/PageTurnerSettingsView.swift",
  "PDF Reader/FaceGesture.swift",
  "PDF Reader/FaceTurnSettings.swift",
  "PDF Reader/FaceTurnController.swift",
  "App/FaceGestureSettingsView.swift",
  "App/FaceGestureOnboarding.swift",
  "App/FaceCameraPrimer.swift",
  "Info.plist NSCameraUsageDescription",
  "R50",
  "R51"
 ],
 "verified": "76048e78",
 "differs_from_4_2": null,
 "shots": [
  {
   "id": "page-turner-settings",
   "kind": "crop",
   "device": "iphone",
   "orientation": "portrait",
   "state": "Account › Preferences › Page Turner on iPhone after pressing Right Arrow (simulator: no Face Gestures section).",
   "alt": "The Page Turner screen after a pedal press, reading Right Arrow → Next Page, with the Swap Forward and Back switch below.",
   "caption": null,
   "reuse": null
  }
 ],
 "open_questions": []
}
---
You can turn pages without taking your hands off your instrument in two ways: with a Bluetooth page turner pedal, or with Face Gestures, which turn the page when you hold a head turn, a wink or a mouth movement. Both work in every reader, including set lists and Planning Center plans, and turns made either way follow your Half-Page Turns and Page Links settings.

## Connect a Bluetooth page turner

A Bluetooth page turner pedal (AirTurn, PageFlip and Donner make common ones) connects to your device as a keyboard, so there's nothing to set up in the app.

1. Pair the pedal in the Settings app under Bluetooth, following its maker's instructions.
2. Set the pedal to a mode that sends the arrow keys or Page Up and Page Down. A mode that sends Space and Enter works too.
3. Open a piece and press the pedal.

Pedals set to a media or volume mode aren't supported. If your pedal has those modes, switch it to an arrow key or Page Up/Down mode.

### Test your pedal

1. Go to **Account › Preferences › Page Turner**.
2. Press each pedal.
   The screen shows the key the pedal sends and what it does in a reader, such as "Right Arrow → Next Page". Nothing turns on this screen.

{shot:page-turner-settings}

If you see "Not a page-turn key", the pedal is in a mode the app doesn't use. Change the pedal's mode and press it again.

If the pedals turn the wrong way, turn on **Swap Forward and Back** on the same screen. The setting also swaps the arrow keys on a keyboard.

Pedal presses are ignored while you're annotating, typing a note, customizing the toolbar or setting up a page link, and while a sheet or popover is open over the reader. If a pedal still doesn't turn pages, see [My page turner isn't turning pages](/guide/page-turner-isnt-turning-pages).

## Turn pages with Face Gestures

Face Gestures use the front camera to watch for one movement you choose. Hold the movement for a moment and the page turns; a quick glance does nothing. Each movement turns one page, so relax your face between turns. You can choose one of these gestures:

- **Head Turn**: Turn your head right for the next page, left to go back.
- **Wink**: Wink your right eye for the next page, your left to go back.
- **Mouth Movement**: Pull your mouth to the right for the next page, to the left to go back.

Right and left are your own right and left, and Swap Forward and Back doesn't change them.

### Set up Face Gestures

Setup also calibrates the gesture to the way you move, so turns respond to your own range of movement. It's free, and you can repeat it any time.

1. In a reader, choose **⋯ › Face Gestures**. You can also go to **Account › Preferences › Page Turner › Face Gestures** and tap **Set Up Face Gestures**.
2. Read the introduction and tap **Continue**.
3. Choose a gesture, then tap the button below it, such as **Use Head Turn**.
4. Read how the camera is used, tap **Continue**, then allow camera access.
5. Follow the three steps on screen: relax and look at the screen while the ring fills, then hold the movement for the next page, then the one for the previous page.
6. Practice turning the sample pages, then tap **Start Playing** (or **Done** if you started in Account).

If you don't have Premium, the Premium screen appears when you tap **Start Playing**, and again whenever you switch Face Gestures on in a reader. Setup, calibration and Try It stay free whether or not you subscribe.

### Turn Face Gestures on and off

In any reader, choose **⋯ › Face Gestures**. A checkmark shows when it's on. If you use it often, you can add a Face Gestures button to the toolbar (see [The reader at a glance](/guide/the-reader-at-a-glance)).

While Face Gestures are on, a small face icon appears in the bottom-left corner of the page. It dims when the camera can't see your face. Tap it to read what it means or to turn Face Gestures off.

Face Gestures stay on for the piece, set list or plan you're reading. The camera stops when you close the reader, switch to another app or turn Face Gestures off, and it doesn't come back on by itself, so turn it on again the next time you need it. If your device gets too warm, Face Gestures pause until it cools down.

### Change the gesture or sensitivity

Go to **Account › Preferences › Page Turner › Face Gestures**:

- **Try It** turns sample pages so you can check the gesture without opening your music.
- **Set Up Again** lets you choose a different gesture or calibrate again.
- **Sensitivity** goes from Lowest to Highest. Raise it if turns are missed; lower it if pages turn by accident.
- **Reset Face Gestures** removes your gesture and calibration.

### Privacy

The camera is on only during setup, while you use Try It, and while Face Gestures are on, and you'll see the green camera light whenever it is. Face tracking happens on your device, and nothing is recorded or sent anywhere. The only things kept are a few measurements of how you move, which **Reset Face Gestures** removes.
