---
{
 "slug": "tune-and-play-reference-tones",
 "h1": "Tune and play reference tones",
 "seo_title": "Tune Your Instrument and Play Drones | Music Folder",
 "description": "Tune any instrument with Music Folder's chromatic tuner, tune a guitar string by string, set A4 calibration, and play reference pitches and drones.",
 "intent": "general",
 "intent_note": "Musicians who want a tuner, a pitch pipe or a drone next to their sheet music, including brass and wind players who read in B-flat, E-flat or F.",
 "searches": [
  "tuner",
  "guitar tuner",
  "pitch pipe",
  "drone",
  "A440",
  "A 442",
  "calibration",
  "concert pitch",
  "transposing instrument",
  "tuning note",
  "intonation"
 ],
 "availability": [
  {
   "kind": "premium",
   "text": "Requires Music Folder Premium."
  }
 ],
 "related": [
  "use-the-metronome",
  "play-the-piano",
  "cant-hear-the-metronome-or-a-recording"
 ],
 "feature_link": {
  "href": "/features/toolkit",
  "text": "the musician's toolkit"
 },
 "documents": [
  "Tools/Tuner.swift",
  "Tools/GuitarTunerView.swift",
  "Tools/Drone.swift",
  "App/ToolsView.swift",
  "PDF Reader/ReaderToolbarCustomization.swift"
 ],
 "verified": "76048e78",
 "differs_from_4_2": null,
 "shots": [
  {
   "id": "tuner-in-reader",
   "kind": "crop",
   "device": "iphone",
   "orientation": "portrait",
   "state": "Ave Maria in the iPhone reader with the tuner sheet open, listening (no note yet).",
   "alt": "The tuner open from the reader on iPhone, with the Tuner and Tone switch and the needle waiting for a note.",
   "caption": null,
   "reuse": null
  }
 ],
 "open_questions": []
}
---
The tuner listens through the microphone and shows the note you're playing and how far it is from in tune. The same tool plays reference pitches and drones, so you can tune to a note or practice intonation against a held tone.

## Open the tuner

- **In a piece**, tap {sf:tuningfork} **Tuner** in the toolbar. A sheet opens over the music (a popover on iPad and Mac), with a **Tuner** and **Tone** switch at the top. If it isn't on your toolbar, look in the **⋯** menu.
- **Without a piece**, open the **Tools** tab and tap **Tuner** or **Tone**.

The first time you use the tuner, the app asks for access to the microphone. If you turned it down, the tuner shows **Microphone Access Needed**; tap **Open Settings** and allow the microphone for Music Folder.

{shot:tuner-in-reader}

## Tune your instrument

Play a single note. The tuner shows the note name and octave, a needle on a scale from −50 to +50 cents, and the exact difference in cents below it. The note turns green when you're in tune.

If you play a transposing instrument, you can have the tuner show your written note instead of concert pitch:

1. Tap {sf:gearshape} to open **Tuner Settings**.
2. Under **Display**, set **Transposition** to **B♭** (trumpet, clarinet, tenor sax), **E♭** (alto and baritone sax) or **F** (horn).

While a transposition is on, the tuner shows a "Transposed" label so you don't mistake it for concert pitch. **Accidentals** in the same section switches note names between sharps and flats.

## Tune a guitar

In **Tuner Settings**, set **Mode** to **Guitar**. The tuner shows a guitar headstock with a button for each string, and follows whichever string you play.

- Choose a **Tuning** in Tuner Settings: **Standard**, **Drop D**, **Half Step Down**, **Whole Step Down**, **Drop C**, **DADGAD**, **Open G** or **Open D**.
- Tap a string's button to hear its reference pitch and hold the meter on that string. Once the string stays in tune for a moment, the tuner goes back to following whatever you play. Tap **Auto** to go back sooner.

## Set the calibration (A4)

Most groups tune to A4 = 440 Hz. If yours tunes higher or lower, open **Tuner Settings** (or **Tone Settings**) and use **Reference Pitch** under **Calibration** to set anything from 415 to 466 Hz. The setting is shared by the tuner and the tones, and the app remembers it.

## Play a reference tone or drone

1. Switch to **Tone** (in a piece) or open **Tone** from the Tools tab.
2. Tap a note to start it. It keeps sounding until you tap the same note again, or tap another note to switch.
3. To change the octave, tap the ‹ and › arrows beside the note name, or swipe up or down on it.

The frequency under the note follows your calibration. To change the sound, tap {sf:gearshape} and choose a **Voice**: **Sine** for a pure tone, or **Strings**, **Organ**, **Brass** or **Clarinet** for a fuller drone to play scales and long tones against. You hear a short sample when you choose one.

Note: Without Premium, the tuner in a piece opens but shows **Unlock with Premium** instead of listening, and tapping a note in **Tone** or a guitar string opens the upgrade screen. In the Tools tab, **Tuner** and **Tone** are marked Premium and open the upgrade screen. See [Free and Premium](/guide/free-and-premium).
