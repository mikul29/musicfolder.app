---
{
 "slug": "get-free-sheet-music",
 "h1": "Get free sheet music",
 "seo_title": "Download Free Public-Domain Sheet Music | Music Folder",
 "description": "Browse and search a catalog of free public-domain classical scores in Music Folder, preview a score's pages, and add it to your library.",
 "intent": "general",
 "intent_note": "Musicians looking for free classical sheet music, and new users who want something to open right away.",
 "searches": [
  "free scores",
  "public domain",
  "classical sheet music",
  "discover",
  "catalog",
  "download sheet music",
  "imslp",
  "starter folder",
  "classical starters"
 ],
 "availability": [
  {
   "kind": "requires",
   "text": "Needs an internet connection to browse and download."
  }
 ],
 "related": [
  "import-music",
  "organize-music-in-folders",
  "find-music-with-search-and-filters",
  "free-and-premium"
 ],
 "feature_link": {
  "href": "/features/free-sheet-music",
  "text": "free sheet music"
 },
 "documents": [
  "Discover/DiscoverLandingViewController.swift",
  "Discover/DiscoverCatalogViewController.swift",
  "Discover/CatalogPreviewViewController.swift",
  "Discover/CatalogImporter.swift",
  "Discover/BrowseSearchView.swift",
  "Discover/StarterGroup.swift",
  "Groups/Groups View/GroupsView.swift (groupsEmptyState)",
  "App/ContainerEmptyStateView.swift",
  "App/MainTabBarController.swift (UISearchTab)",
  "R5"
 ],
 "verified": "76048e78",
 "differs_from_4_2": null,
 "shots": [
  {
   "id": "browse-landing",
   "kind": "screen",
   "device": "ipad",
   "orientation": "landscape",
   "state": "Browse on iPad landscape with nothing typed: search field, Composers, Featured.",
   "alt": "The Browse screen on iPad, with the search field at the top, a row of composers with their portraits, and featured free scores below.",
   "caption": null,
   "reuse": null
  }
 ],
 "open_questions": [
  "Catalog scope: StarterGroup and the landing suggest classical / public-domain scores only (instrument rows Piano, Guitar, Voice, Woodwinds, Brass, Strings). The guide says 'classical'; confirm nothing non-classical is in the 4.3 catalog."
 ]
}
---
Music Folder includes a catalog of free public-domain classical scores. You can browse it by composer or instrument, search it, preview a score and add it to your library.

{shot:browse-landing}

## Browse the catalog

1. Tap {sf:magnifyingglass} **Search** to open **Browse**.
2. Scroll the **Featured**, **Composers** and **Instruments** rows.
3. Tap a composer or an instrument to see all of their scores.
4. Use the **Instrument** and **Composer** buttons at the top of the list to narrow it further.

## Search for a score

Type in the search field at the top of Browse. It searches your own library and set lists as well as the catalog, and lists the results in groups: **In Your Library**, **In Your Set Lists** and **Discover** (the free catalog). If you've connected Planning Center, its songs appear in their own group. Tap **Discover** in the row of buttons under the search field to see only free scores.

If nothing matches, tap **Find sheet music online** to search the IMSLP website in your web browser. Anything you download there can be imported like any other PDF; see [Import music](/guide/import-music).

## Preview and add a score

1. Tap a score to open a preview of its pages.
2. Tap **Add to Library**.

In search results you can also tap **Add** beside a score without opening it; it changes to **Added**. The piece arrives with its title and composer filled in, and its tempo and time signature when the catalog has them. Once a score is in your library, its preview offers **Remove from Library** instead.

While your library is empty, Home and Library show **Browse Free Scores**, which opens Browse. An empty folder offers **Browse Free Sheet Music**; scores you add from there go into that folder.

## Add a starter folder

When you don't have any folders yet, the Folders screen offers **Add a Starter Folder**. It creates a folder called "Classical Starters" with five well-known pieces: Brahms's Lullaby, Schubert's "Ave Maria" and "Ständchen," Fauré's "Après un rêve," and a Borodin string quartet.

## The free limit

Scores from the catalog are free, but each one counts as a piece in your library. The free version holds 15 pieces, including the five in the starter folder. When your library is full, adding a score shows the Premium offer. See [Free and Premium](/guide/free-and-premium).
