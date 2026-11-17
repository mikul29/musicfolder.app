---
{
 "slug": "use-the-metronome",
 "h1": "Use the metronome",
 "seo_title": "Use the Metronome With Your Sheet Music | Music Folder",
 "description": "Use Music Folder's metronome: set the tempo with the dial or tap tempo, choose a time signature, subdivisions and accents, and follow each piece's tempo.",
 "intent": "general",
 "intent_note": "Musicians looking for a metronome app that sits on top of their sheet music, and users who want to know how tempo, tap tempo, accents and section tempos work.",
 "searches": ["click track", "bpm", "tap tempo", "time signature", "subdivision", "accent", "downbeat", "tempo marking", "click sound", "metronome volume"],
 "availability": [{"kind": "premium", "text": "Playing the metronome needs Premium."}],
 "related": ["tune-and-play-reference-tones", "play-a-set-list", "add-sections-to-a-book", "cant-hear-the-metronome-or-a-recording"],
 "feature_link": {"href": "/features/toolkit", "text": "the musician's toolkit"},
 "documents": ["Tools/Metronome.swift", "Tools/MetronomeController.swift", "Tools/MetronomeEngine.swift", "Tools/MetronomeTypes.swift", "PDF Reader/PDFReaderToolbar.swift", "PDF Reader/SectionTempoFollower.swift", "App/ToolsView.swift", "Tools/AudioSessionCoordinator.swift", "R66", "R67"],
 "verified": "76048e78",
 "differs_from_4_2": null,
 "shots": [
  {"id": "metronome-dial", "kind": "crop", "device": "iphone", "orientation": "portrait", "state": "The metronome opened from the Tools tab on iPhone, stopped, at 60 BPM (Larghetto) in 4/4 with quarter-note subdivision: beat bars at the top, the BPM readout, the dial with the play button and the ‹ › arrows, and the TIME SIG, SUB DIV and TAP tiles at the bottom.", "alt": "The metronome showing 60 BPM, a row of four beat bars above it, a round dial with a play button in the middle, and tiles for time signature, subdivision and tap tempo.", "caption": null, "reuse": "tool-metronome.jpg"}
 ],
 "open_questions": []
}
---
The metronome lives on top of your music, so you can start a click without leaving the page. It opens at the piece's own tempo and time signature, and it can follow the tempos of the sections in a book.

## Open the metronome

- **In a piece**, tap {sf:metronome} **Metronome** in the toolbar to start or stop the click. To see the full metronome, tap the small {sf:chevron.up} in the corner of the metronome button. Where there's room, the toolbar shows the current tempo next to it.
- **Without a piece**, open the **Tools** tab and tap **Metronome**.

If the metronome isn't on your toolbar, look in the **⋯** menu, or add it with **Customize Toolbar**.

Note: Without Premium, you can open the full metronome from a piece and set the tempo, time signature and accents, but starting the click opens the upgrade screen. In the Tools tab, **Metronome** opens the upgrade screen. See [Free and Premium](/guide/free-and-premium).

{shot:metronome-dial}

## Set the tempo

The tempo range is 30 to 300 BPM. The Italian tempo marking above the number (Andante, Allegro and so on) follows as you change it.

- Turn the dial to change the tempo in single steps.
- Tap the ‹ and › arrows inside the dial to go down or up by one.
- Tap **TAP** in time with the music. After two taps the tempo follows your tapping, averaged over your last few taps. Pause for a couple of seconds to start fresh.

Tap the play button in the middle of the dial to start or stop. You can change the tempo while it's playing.

## Choose a time signature and subdivision

- Tap **TIME SIG** and pick the beats (1 to 16) and the note value (2, 4, 8 or 16).
- Tap **SUB DIV** and choose **Quarter**, **Eighth**, **Triplet** or **Sixteenth** to hear clicks between the beats.

## Set accents and sounds

The bars across the top stand for the beats in a bar. Tap a beat's bar to cycle it through low, medium, high and silent. Fill the first bar for a strong downbeat, or silence a beat to practice holding time on your own.

For the sounds, tap {sf:gearshape} to open **Metronome Settings**:

1. Under **Accent marker**, choose the accent level you want to change.
2. Under **Sound**, choose **Click**, **Tick**, **Wood**, **Beep** or **Cowbell**. You hear it right away.
3. Use **Accent Volume** to make that accent louder or softer, and **Master Volume** for the metronome as a whole.

## Use the tempo saved with a piece

The metronome opens at the tempo and time signature in the piece's details. A piece with no tempo starts at 60 BPM.

- If you change the time signature in the metronome, it's saved to the piece when you close the metronome.
- If you change the tempo, the reader asks **Save Tempo Change?** when you leave the piece. Tap **Save** to make it the piece's tempo, or **Don't Save** to keep the old one.

In a set list, each piece starts at its own tempo, and a tempo you change during the set isn't saved to the piece. See [Play a set list](/guide/play-a-set-list).

## Follow section tempos in a book

When a book's sections have their own tempos (a Largo, then an Allegro), the metronome follows the section on the page as you turn. If it's already playing, it moves to the new tempo without stopping. A section without a tempo keeps the current one. For setting section tempos, see [Add sections to a book](/guide/add-sections-to-a-book).

Once you change the tempo yourself, the metronome stops following the sections, so your tempo isn't overridden at the next page. To go back to following them, choose **⋯ › Follow Section Tempos**.

## Keep it playing

The metronome plays alongside music from other apps, and it sounds even when your iPhone is set to silent. It keeps going when you lock the screen or switch to another app; come back to the app to stop it. Closing the piece, or leaving the metronome in the Tools tab, stops it.

If you can't hear it, see [I can't hear the metronome or a recording](/guide/cant-hear-the-metronome-or-a-recording).
