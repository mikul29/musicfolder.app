---
{
 "slug": "connect-planning-center",
 "h1": "Connect Planning Center",
 "seo_title": "Connect Planning Center to Music Folder",
 "description": "Sign in with Planning Center to see your church's song library as a folder and your services as set lists in Music Folder, and disconnect any time.",
 "intent": "general",
 "intent_note": "A worship leader or church musician who uses Planning Center Services and wants its songs, charts and service plans on an iPad or iPhone music stand.",
 "searches": [
  "pco",
  "planning center services",
  "worship",
  "church",
  "services",
  "sign in planning center",
  "disconnect planning center",
  "reconnect",
  "song library"
 ],
 "availability": [
  {
   "kind": "premium",
   "text": "Requires Music Folder Premium and a Planning Center Services account."
  }
 ],
 "related": [
  "play-a-service-plan",
  "free-and-premium",
  "find-music-with-search-and-filters"
 ],
 "feature_link": {
  "href": "/planning-center",
  "text": "Music Folder for Planning Center"
 },
 "documents": [
  "Planning Center/PCOAccountScreen.swift",
  "Planning Center/PlanningCenterPromptViewController.swift",
  "Planning Center/PCOLibraryStore.swift",
  "Planning Center/PCOKeychain.swift",
  "Planning Center/PCOFolderViewController.swift",
  "Groups/Groups View/GroupsView.swift",
  "Groups/Groups View/GroupsCell.swift",
  "Services/SetListSections.swift",
  "Services/SongFilterTokens.swift",
  "App/AccountView.swift"
 ],
 "verified": "76048e78",
 "differs_from_4_2": null,
 "shots": [],
 "open_questions": [
  "Clear Cached Files: its confirmation says \"Annotations on Planning Center PDFs are removed too.\" (PCOAccountScreen.swift line 181), but since 4.2 Planning Center ink lives in annotation layers keyed pco-att-<id> in the private store, not in the cached files (CLAUDE.md Annotations: PCOFileCache.storeAnnotated is legacy). The guide doesn't mention markings in the Clear Cached Files step. Owner: is the warning still true, or should the dialog drop it?"
 ]
}
---
If your church or worship team plans services in Planning Center Services, you can connect your account and use its songs and service plans in Music Folder. Your team's song library appears as a folder, and services appear as set lists, with their sheet music and chord charts ready to play.

## Connect your account

1. Open Account: tap your picture or initials at the top of Home. On iPad with the sidebar, tap your name at the bottom of the sidebar.
2. Under Connected Services, tap **Planning Center**.
3. Tap **Connect Planning Center**. If you don't have Premium, the Premium screen appears first.
4. Sign in with your Planning Center account and allow access.

When you're connected, the Planning Center screen shows your organization's name and how many songs and services were loaded. The first sync can take a moment for a large song library.

The connection belongs to the device, so connect on each iPhone, iPad or Mac where you want to use Planning Center. You'll see the plans and songs that your Planning Center permissions allow.

Tip: When your library is still empty, Music Folder may invite you once to connect, with "Does your team use Planning Center?" or a smaller "Use Planning Center?" banner. Connecting from there does the same as the steps above. If you dismiss it, it doesn't come back; connect from Account instead.

## What appears in Music Folder

- **A Planning Center folder.** In **Library › Folders**, a folder named after your organization holds your whole Planning Center song library. Open it to search the songs and open their sheet music. Tap **⋯** to show the songs as a list or as icons.
- **Services as set lists.** In **Library › Set Lists**, your upcoming services appear with the most recent past ones, each marked "Planning Center". With Date sorting they mix with your own set lists by date; with Manual or Title sorting they get their own section. To show only one kind, tap **⋯** and choose an option under **Show**. See [Play a service plan](/guide/play-a-service-plan).
- **Songs in your library and search.** Planning Center songs also appear in **All Music** and in search results. To see only them, or only your own music, tap the Filter button in the search field and choose **Source**.

Everything from Planning Center is read-only in Music Folder. To change a song, an arrangement or a service, edit it in Planning Center; Music Folder picks up the change the next time it refreshes. Your own notes and markings on Planning Center music are saved in Music Folder and aren't sent back to Planning Center.

## Refresh and offline use

Music Folder refreshes from Planning Center when you use it. To refresh now, open Account › **Planning Center** and tap **Refresh Now**, or pull down in the Planning Center folder or a service.

Sheet music you open is kept on the device so it works offline, up to 500 MB, with the oldest files removed first. To free the space, tap **Clear Cached Files**; files download again the next time you open them.

If your Planning Center sign-in expires, the folder's caption says "Reconnect". Tap it, or touch and hold the folder and choose **Reconnect Planning Center**, then sign in again.

## Disconnect Planning Center

1. Open Account, then tap **Planning Center**.
2. Tap **Disconnect Planning Center**.
3. Tap **Disconnect** to confirm.

The Planning Center folder, its services and all downloaded Planning Center files are removed from this device. Nothing changes in Planning Center, and your own library and set lists aren't affected.
