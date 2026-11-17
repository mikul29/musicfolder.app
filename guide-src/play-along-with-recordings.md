---
{
 "slug": "play-along-with-recordings",
 "h1": "Play along with recordings",
 "seo_title": "Slow Down a Recording or Change Its Key | Music Folder",
 "description": "Attach a recording to a piece, play along in the reader, slow it down or change its key without changing the file, and record yourself over the score.",
 "intent": "general",
 "intent_note": "Musicians learning a part by ear who want a backing track or reference recording next to the score, slowed down or transposed, and players who want to record a practice take.",
 "searches": ["backing track", "audio", "mp3", "slow down", "change pitch", "transpose audio", "practice track", "record myself", "voice memo", "speed", "tempo"],
 "availability": [],
 "related": ["edit-or-delete-a-piece", "use-the-metronome", "track-your-practice", "cant-hear-the-metronome-or-a-recording"],
 "feature_link": {"href": "/features/toolkit", "text": "the musician's toolkit"},
 "documents": ["Tools/AudioAttachmentAdder.swift", "Shared UI/AddSongFormViewController.swift", "Tools/ReaderAudioBar.swift", "Tools/PlaybackAdjustmentViewController.swift", "Tools/PlaybackAdjustment.swift", "Tools/RecordingTempo.swift", "Tools/ReaderRecorderCard.swift", "Tools/RecordingTake.swift", "Services/SetTiming.swift", "R38", "R40", "R44"],
 "verified": "76048e78",
 "differs_from_4_2": null,
 "shots": [
  {"id": "tempo-and-key", "kind": "crop", "device": "iphone", "orientation": "portrait", "state": "A chord chart open in the reader on iPhone with its recording playing; the audio player under the toolbar shows 72 BPM · D on its Tempo & Key button, and the Tempo & Key sheet is open: TEMPO card at 72 BPM (Original 88 BPM) with the slider and its marks, KEY card at D (+2 from C) with the key strip.", "alt": "The Tempo and Key sheet: a tempo card reading 72 BPM with a slider, and a key card reading D with a row of keys from C to E below it.", "caption": null, "reuse": "tempo-key-iphone.jpg"}
 ],
 "open_questions": []
}
---
Each piece can have a recording attached: a reference track, a backing track or a take of your own. It plays in a small player above the score, and you can slow it down or move it to another key while you learn the part. Recordings and Tempo & Key are free.

## Attach a recording

1. Open the piece's details with **Edit Details** (in the reader's title menu or **⋯** menu, or by touching and holding the piece in your music list).
2. Tap **Add Recording** and choose **Record** (record with the microphone), **Import File** (an audio file from the Files app) or **Music Library** (a song from the Music app that's downloaded to your device).
3. Save the details.

Protected tracks from the Music app can't be imported; only songs you own can be added.

A piece holds one recording. To replace it, tap **Update Recording**; to delete it, tap **Update Recording** and choose **Remove Recording**.

If the piece has no duration yet, the recording's length fills it in, which helps set-list timing. See [Add pages and timing to a set list](/guide/add-pages-and-timing-to-a-set-list).

You can also start from the reader: tap {sf:play.fill} **Play** on a piece that has no recording, and the same three choices appear.

## Play it in the reader

Tap {sf:play.fill} **Play** in the toolbar. A player appears under the toolbar with play and pause, a button to skip back 10 seconds, and a bar you can drag to move through the track. Turning pages and opening other tools don't stop it.

- Tap {sf:chevron.up} to shrink the player to a small pill with the time, so it covers less of the score. Tap the pill to bring the player back.
- Tap {sf:xmark} to stop and close the player.

Playback continues when you lock the screen or switch apps, and you can pause from the Lock Screen or your headphones. Unlike the metronome, a recording pauses music playing in other apps. Leaving the piece stops it.

## Change the tempo and key

1. While the recording is loaded, tap {sf:slider.horizontal.3} **Tempo & Key** in the player.
2. Under **Tempo**, drag the slider or tap − and + to go slower or faster. Tap a mark under the slider to jump to half speed, three-quarter speed, the original or the fastest setting.
3. Under **Key**, tap a key in the row, or drag the row, to move the recording up or down.

Every change plays right away. The tempo goes from half speed to 125% without changing the pitch, and the key moves up to six semitones either way without changing the tempo. The recording file itself is never changed, and the app remembers your settings for that recording. Tap {sf:arrow.counterclockwise} on a card to return it to the original. Once you've changed something, the player's button shows what you're hearing (for example, "72 BPM · D") so a slowed-down track isn't mistaken for the real thing.

{shot:tempo-and-key}

### BPM or percent

The app measures the recording's tempo from the audio. It shows the tempo in BPM only when it's sure: when the recording holds a steady tempo, or when you've set the original tempo yourself. A recording whose tempo changes (common in classical music) works in percent, where 100% is the recording as played.

To fix the original tempo, tap {sf:ellipsis} on the Tempo card and choose **Set Original Tempo…**. You can type the tempo, tap it in time with the recording, or pick a suggestion such as the piece's own tempo. This is also the way to correct a measurement that came out at half or double the real tempo. Depending on what's shown, the same menu also offers **Use Detected Tempo** (back to the measured tempo) and **Use Percent** (no BPM for this recording).

The Key card's {sf:ellipsis} works the same way, with **Set Original Key…**, **Use Detected Key** and **Use Semitones**.

## Record yourself in the reader

On a piece without a recording, tap {sf:play.fill} **Play** and choose **Record**. A recorder card takes the player's place above the score, so you can keep reading and turning pages while you record.

1. Tap the record button. With **3-2-1 Countdown** on, a short count-in comes first; tap during it to cancel.
2. Play. The card shows the time and a live waveform.
3. Tap the button again to stop.
4. Listen back with play, then tap **Save** to attach the take to the piece, or {sf:arrow.counterclockwise} to record it again.

**3-2-1 Countdown** is on until you turn it off, and the app remembers your choice. If you leave the piece while holding a take, the app asks **Save Recording?**. Closing the recorder with {sf:xmark} asks before discarding a take.

The first time you record, the app asks for access to the microphone.
