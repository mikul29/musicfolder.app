---
{
 "slug": "keep-notes-on-a-piece",
 "h1": "Keep notes on a piece",
 "seo_title": "Keep Practice Notes on a Piece | Music Folder",
 "description": "Write notes on a piece in Music Folder, flag cues to show on the score, add dated reminders for one rehearsal, and restore an earlier version.",
 "intent": "existing",
 "intent_note": "A musician who wants to keep reminders, rehearsal instructions or practice notes with a piece and see them while playing.",
 "searches": [
  "notes",
  "comments",
  "reminders",
  "rehearsal notes",
  "practice notes",
  "cue",
  "date",
  "previous version",
  "undo note",
  "text"
 ],
 "availability": [],
 "related": [
  "the-reader-at-a-glance",
  "use-performance-mode",
  "play-a-set-list",
  "mark-up-music-with-apple-pencil"
 ],
 "feature_link": null,
 "documents": [
  "Notes/NotesPanelViewController.swift",
  "Notes/NotesPanelPresenter.swift",
  "Notes/NotesFormatBar.swift",
  "Notes/NoteMarkup.swift",
  "Notes/CueStripView.swift",
  "Services/SongNotesService.swift",
  "Shared UI/SongListViewController.swift",
  "Set Lists/Songs View/SetListViewSongs.swift"
 ],
 "verified": "76048e78",
 "differs_from_4_2": null,
 "shots": [
  {
   "id": "notes-panel-ipad",
   "kind": "crop",
   "device": "ipad",
   "orientation": "landscape",
   "state": "Après un rêve with the Notes panel docked on the right: two notes and a dated recital line.",
   "alt": "The Notes panel beside a score, with two practice notes and a dated reminder for a recital shown in orange.",
   "caption": null,
   "reuse": null
  }
 ],
 "open_questions": [
  "The panel's \"Only on your devices\" caption is driven by CollabShareService.isCollaborative (the 4.2 collaboration check). It is not clear whether it also shows for 4.3 Shared Folder / Shared Set List pieces, so the guide doesn't mention the caption. Confirm whether it should."
 ]
}
---
Each piece can have a note: rehearsal instructions, fingerings to remember, who takes the solo, or a reminder for one particular service. You write it in the Notes panel beside the music, and the most important lines can appear on the score while you play.

## Open the Notes panel

In the reader, tap {sf:text.document} **Notes**. The icon is filled in when the piece already has a note. On iPhone, Notes starts out on the bottom toolbar; when that bar isn't showing, look for it on the top bar or in the ⋯ menu.

Where the panel opens depends on the space. In an iPad-sized window held in landscape, it slides in on the right and the page moves over to make room. In portrait it opens over the right side of the page, and the page underneath still works. On iPhone and in narrow windows it opens as a sheet that leaves the page visible above it.

{shot:notes-panel-ipad}

You can also read or edit a note without opening the music: touch and hold a piece in your library or in a set list and choose **Notes**.

The note belongs to the piece, so you see the same note wherever you open it, on its own or in any set list. A Planning Center song has its own note in the same way, the same in every plan that uses the song.

## Write a note

1. Tap the text in the panel to start writing. The panel opens ready to read, so it never raises the keyboard by accident on stage.
2. Type your note. Use the buttons above the keyboard for {sf:bold} **Bold**, {sf:list.bullet} **Bulleted List**, {sf:list.number} **Numbered List**, {sf:flag} **Cue** and {sf:calendar} **Date**.
3. Tap {sf:checkmark} when you're done.

The note is saved as you type. You can also start a list by typing "- " or "1. " at the start of a line.

Some things you type become links. A page reference such as "p. 3" or "page 3" jumps to that page of the score when you tap it, and a time such as "1:24" plays the piece's recording from that point when the piece has one.

## Show cues on the score

A line marked as a cue is one you want to see while you play. Put the cursor in the line and tap {sf:flag} **Cue**, or type "! " at the start of the line. Cues appear in a small label at the top-right corner of the page, so you can read them without opening the panel; tap the label to open the note. A cue shows on the first page of the piece, or, if it mentions a page such as "p. 3", on that page instead. When a page has more than one cue, the label shows the first and how many more there are.

To hide the label, tap the panel's ⋯ button and turn off **Show Cues on Score**.

## Add a reminder for one day

A dated line is an instruction for one rehearsal or performance, such as "Take the repeat this time" for Sunday. It's highlighted in the note until its day ends, and from a week before that day it also shows on the score like a cue, ahead of your other cues. Once the day has passed it's dimmed, so it stays in the note as a record without getting in the way.

1. Put the cursor in the line.
2. Tap {sf:calendar} **Date** and choose **Today** or **Choose Date…**. When you opened the note from a set list that has a date, that date is offered too.

You can also type the date at the start of a line in the form @2026-12-24, followed by a space. To take the date off a line, tap **Date** and choose **Remove Date**.

When old dated lines pile up, tap the panel's ⋯ button and choose **Tidy Past Dates** to remove every dated line whose day has passed.

## Restore the previous version

The app keeps one previous version of each note: the text as it was before you last started changing it. If you change your mind about an edit, or tidy away lines you wanted, tap the panel's ⋯ button and choose **Restore Previous Version**. The text you replace becomes the previous version, so you can choose it again to undo the restore.

The previous version is kept for 30 days.

## Change the text size or delete a note

Tap the panel's ⋯ button and choose **Larger Text** or **Smaller Text**. The size applies to all your notes.

To delete a note, choose **Delete Note**. The note and its previous version are removed from all your devices.

## Who can see your notes

Notes are personal. They sync to your own devices with iCloud, and they're never shared with collaborators, even on a piece in a shared folder or set list. If you send someone a copy of a piece or set list as a Music Folder file, a copy of your notes goes with it.

In Performance Mode, notes open read-only, so you can see them but not change them.
