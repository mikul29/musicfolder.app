---
{
 "slug": "find-music-with-search-and-filters",
 "h1": "Find music with search and filters",
 "seo_title": "Search and Filter Your Sheet Music Library | Music Folder",
 "description": "Search your sheet music by title, composer or chart lyrics, and narrow the list with filters for folder, key, tag, composer and books in Music Folder.",
 "intent": "existing",
 "intent_note": "Musicians with a large library who need to find a piece quickly, by key, tag or composer.",
 "searches": [
  "search",
  "find",
  "filter",
  "key",
  "tag",
  "composer",
  "books",
  "lyrics",
  "sort",
  "find a song"
 ],
 "availability": [],
 "related": [
  "edit-or-delete-a-piece",
  "organize-music-in-folders",
  "get-free-sheet-music",
  "create-and-edit-a-set-list"
 ],
 "feature_link": null,
 "documents": [
  "Services/SongFilterTokens.swift",
  "Shared UI/SongFilterTokenField.swift",
  "Services/SongFilter.swift",
  "Shared UI/SongListViewController.swift (matchesSearch, applyFiltersAndSearch, searchBarPlaceholder)",
  "Songs/Song View/SongListScreen.swift (songFilterDimensions)",
  "Groups/Songs View/GroupsViewSongs.swift (songFilterDimensions)",
  "Discover/DiscoverLandingViewController.swift",
  "Discover/BrowseSearchView.swift",
  "Set Lists/Add Set List/PickSongsForSetList.swift",
  "Set Lists/Songs View/SetListLibraryPane.swift",
  "R43"
 ],
 "verified": "76048e78",
 "differs_from_4_2": null,
 "shots": [
  {
   "id": "filter-menu",
   "kind": "crop",
   "device": "ipad",
   "orientation": "landscape",
   "state": "Music list with the Filter menu open from the search field (no filter chosen).",
   "alt": "The Filter menu open from the search field, listing Composer, each folder with its number of pieces, Key and Tag.",
   "caption": null,
   "reuse": null
  }
 ],
 "open_questions": []
}
---
Search finds pieces by title, composer and the lyrics of your chord charts. Filters narrow the list by folder, key, tag, composer or type, and you can combine them with a search.

## Search your music

1. Open **Library**, then **Music** (on iPad, choose **Music** in the sidebar).
2. Tap the search field at the top of the list and type. The placeholder reads "Title or Composer."

The list shows every piece whose title or composer contains what you typed, and every chord chart whose text contains it, so you can find a song by a line of its lyrics. Searching inside a folder works the same way and looks only at that folder's pieces.

## Filter the list

{shot:filter-menu}

1. Tap {sf:line.3.horizontal.decrease.circle} **Filter** at the end of the search field.
2. Choose a value. Each option shows how many pieces it matches.

The menu has a section for each kind of filter your library has values for:

- **Source**, when you've connected Planning Center or have shared folders and set lists: **My Music**, **Planning Center**, or one shared collection.
- **Composer**
- **Folder**
- **Type**: **Pieces** or **Books** (pieces shown with Display as Book), when your library has both.
- **Key**, listed in musical order.
- **Tag**

Each filter you choose appears as a token in the search field, such as "Key: D Major", "Folder: Spring Concert" or "#christmas." You can use one value of each kind, and different kinds combine: Folder and Key together show only the pieces in that folder in that key. Choosing a different value of the same kind replaces the first; choosing the active value again turns it off.

The Filter button turns orange and filled while any filter is on. To remove one filter, delete its token in the search field. To remove them all, choose **Clear Filters** at the bottom of the menu. Cancelling a search clears the text you typed but keeps your filters.

Inside a folder, the menu offers **Composer** and **Type**.

## Let suggestions add a filter

As you type two or more letters, up to three suggestions appear above the results: folders, keys, tags and composers with a word that starts with what you typed. Tap one to add it as a filter. Typing "#" lists your tags.

For example, typing "bach" suggests the composer, and typing "Eb" or "e flat" suggests E♭ Major and E♭ Minor if your library has pieces in those keys.

## Search everything in Browse

Browse searches your library, your set lists and the free catalog at once. Tap {sf:magnifyingglass} **Search** to open Browse, and type. Its Filter button offers the same filters, which narrow the results from your library. See [Get free sheet music](/guide/get-free-sheet-music).

## Search when adding to a set list

The music picker in a set list has the same search field and Filter button. There, searching also matches the titles of sections, so you can find a hymn inside a hymnal. See [Create and edit a set list](/guide/create-and-edit-a-set-list).

On iPhone: the **Library** screen also lists your tags. Tap a tag to see its pieces.
