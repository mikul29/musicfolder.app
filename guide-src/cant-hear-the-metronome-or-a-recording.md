---
{
 "slug": "cant-hear-the-metronome-or-a-recording",
 "h1": "I can't hear the metronome or a recording",
 "seo_title": "Fix No Sound from the Metronome or a Recording | Music Folder",
 "description": "No sound from the metronome or a recording in Music Folder? Check Premium, volume, the metronome's own volume, Bluetooth and recordings still downloading.",
 "intent": "troubleshooting",
 "intent_note": "Existing users who start the metronome, a tone or an attached recording and hear nothing.",
 "searches": [
  "no sound",
  "metronome silent",
  "metronome not working",
  "recording won't play",
  "audio not playing",
  "silent mode",
  "bluetooth headphones",
  "volume"
 ],
 "availability": [
  {
   "kind": "premium",
   "text": "Metronome playback, the tuner's reference tones and the piano are part of Premium; recordings are free."
  }
 ],
 "related": [
  "use-the-metronome",
  "play-along-with-recordings",
  "tune-and-play-reference-tones",
  "free-and-premium"
 ],
 "feature_link": null,
 "documents": [
  "Tools/AudioSessionCoordinator.swift (.playback / .playAndRecord, mixWithOthers vs exclusivePlayback)",
  "Tools/Metronome.swift (DialTickSound, paywall, Metronome Settings: Accent Volume, Master Volume, beat bar mute)",
  "Tools/MetronomeController.swift",
  "Songs/Song View/SongPDFView.swift (metronomeTapped paywall, firstPlayableAudio)",
  "Data/SongAudioStore.swift (iCloud Drive audio, ensureDownloaded)",
  "Tools/SongAudioListViewController.swift",
  "Tools/ReaderRecorderCard.swift",
  "Tools/AudioRecordViewController.swift",
  "Premium/PremiumPaywallView.swift (compareRow)",
  "PDF Reader/ReaderToolbarCustomization.swift (ReaderTool titles/symbols)"
 ],
 "verified": "76048e78",
 "differs_from_4_2": null,
 "shots": [],
 "open_questions": [
  "SongPDFView.firstPlayableAudio plays the first recording that is already on the device and asks iCloud for the others; when none is downloaded the reader may show no playable recording at all. Owner: confirm what the reader's Play button does in that case so the guide can name it."
 ]
}
---
The metronome, the tuner's reference tones and the piano play on top of whatever else is playing on your device, at full volume. A recording attached to a piece plays like a music app: starting it pauses music playing in other apps. If you start one of them and hear nothing, try the checks below, starting with the first.

## Check that the feature is included

Starting the metronome is part of Premium, and so are the tuner's reference tones and the piano. On the free version, the metronome in the Tools tab opens so you can set it up, but tapping play shows the Premium screen instead of starting it; in the reader, the metronome button shows the Premium screen straight away. Recordings, both playing them and recording yourself, are free. See [Free and Premium](/guide/free-and-premium).

## Turn the volume up while it plays

1. Start the metronome or the recording first.
2. Press the volume up button on the device, or use the volume slider in Control Center.

Adjusting the volume while the sound is playing makes sure you're changing the playback volume. The Ring/Silent switch (or silent mode) doesn't mute the metronome or recordings, so you don't need to change it. The only sound that follows silent mode is the small tick you hear while turning the metronome's tempo dial.

## Check the metronome's own volume

The metronome has its own volume settings, and individual beats can be muted.

1. Open the metronome and tap {sf:gearshape} to open **Metronome Settings**.
2. Check **Master Volume**, and check **Accent Volume** for each accent marker you use.
3. Close Metronome Settings and look at the beat bars on the metronome. Tapping a beat's bar steps it through low, medium, high and muted, so an empty bar is a silent beat. Tap it again to bring the sound back.

## Check where the sound is going

If Bluetooth headphones, a Bluetooth speaker, AirPods or an AirPlay device is connected, the sound plays there instead of the device's speaker.

1. Open Control Center and touch and hold the audio controls to see the current output.
2. Choose the device you want, or turn off Bluetooth for a moment to test the built-in speaker.

## If a recording won't play

- Recordings sync between your devices through iCloud Drive. On a device that just received a piece, its recording may still be downloading. In the recordings list you'll see "This recording is still downloading from iCloud. Try again in a moment." Keep Music Folder open with a connection and try again.
- Make sure iCloud Drive is turned on in Settings › your name › **iCloud**. Without it, recordings don't reach your other devices.
- A phone or FaceTime call interrupts playback. Start the recording again when the call ends.

## If your own recording is silent

Recording needs access to the microphone. If you see **Microphone Access Needed**, open Settings, find Music Folder, and turn on **Microphone**. Then record again.

## Still no sound

Close Music Folder from the App Switcher, open it again, and try once more. If another app is also playing audio, pause it to rule it out.

## Contact us

If you still can't hear anything, [contact us](/contact). It helps to include:

- What you're trying to hear (metronome, a tone, the piano or a recording) and where you started it (the Tools tab or the reader)
- Any headphones, speakers or other audio devices connected
- Your device, its iOS or iPadOS version, and the Music Folder version (**Account › About › Version**)
