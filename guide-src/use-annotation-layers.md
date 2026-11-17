---
{
 "slug": "use-annotation-layers",
 "h1": "Use annotation layers",
 "seo_title": "Use Annotation Layers | Music Folder",
 "description": "Keep different sets of markings on the same score with annotation layers: add, hide, rename, reorder and delete layers, and choose which one you draw on.",
 "intent": "existing",
 "intent_note": "Musicians who want separate markings for a teacher, a conductor or different performances on one PDF, and users who can't find or change a layer.",
 "searches": [
  "layers",
  "hide annotations",
  "hide markings",
  "separate markings",
  "clean copy",
  "active layer",
  "delete annotations",
  "clear markings"
 ],
 "availability": [],
 "related": [
  "mark-up-music-with-apple-pencil",
  "add-text-symbols-and-shapes",
  "send-a-copy-or-print"
 ],
 "feature_link": {
  "href": "/features/annotation",
  "text": "annotation in Music Folder"
 },
 "documents": [
  "PDF Reader/AnnotationLayersViewController.swift",
  "PDF Reader/AnnotationLayerPolicy.swift",
  "PDF Reader/PDFAnnotationSession.swift (Layers bar button, presentLayersPanel)",
  "Services/AnnotationLayerStore.swift",
  "Sharing/AnnotationLayerTransport.swift (flattenVisibleLayers)",
  "R30",
  "R32"
 ],
 "verified": "76048e78",
 "differs_from_4_2": null,
 "shots": [
  {
   "id": "layers-popover",
   "kind": "crop",
   "device": "ipad",
   "orientation": "landscape",
   "state": "Brahms Wiegenlied (Lullaby) in annotation mode with the Layers popover open from the Layers button beside the highlighted pencil. Three layers: Annotations (active, orange checkmark), Lesson Notes and Recital, all visible. Crop to the popover and the part of the page beside it.",
   "alt": "The Layers popover with three layers, Annotations, Lesson Notes and Recital, each with a visibility button and a menu button; Annotations is the active layer.",
   "caption": null,
   "reuse": null
  }
 ],
 "open_questions": []
}
---
Layers let you keep different sets of markings on the same piece, such as your teacher's corrections, bowings for one orchestra, or cues for a single concert, and show or hide each set when you need it. Every piece starts with one layer, named **Annotations**.

## Open the Layers panel

1. Open a piece and tap {sf:pencil.tip.crop.circle} **Annotate**.
2. Tap {sf:square.3.layers.3d} **Layers**, beside the highlighted pencil.

{shot:layers-popover}

The panel lists the piece's layers. The checkmark shows the **active layer**, the one you're drawing on. Your pens, the eraser, and any text, symbols and shapes you add all go to the active layer. Marks on the other visible layers stay on screen, but you can't change them until you make their layer active.

To close the panel, tap {sf:xmark} **Close** or tap outside it.

## Add a layer

In the Layers panel, tap {sf:plus} **New Layer**. The new layer is named Layer 2 (or the next free number), goes to the bottom of the list, and becomes the active layer, so you can start drawing on it straight away.

## Choose the layer you draw on

Tap a layer's row. Its checkmark fills in, and what you draw from now on goes to that layer.

## Hide or show a layer

Tap {sf:eye} on a layer's row to hide it, and {sf:eye.slash} to show it again. You can hide any layer, or all of them for a clean copy of the music.

Hiding a layer doesn't change which layer is active. If you hide the active layer and then start drawing, it appears again. Tapping a hidden layer's row also shows it as it becomes active.

## Rename, duplicate, reorder, clear or delete a layer

Tap {sf:ellipsis.circle} **More** on a layer's row, or touch and hold the row, then choose an action:

- **Rename**: give the layer a name that says what it's for, such as "Lesson Notes".
- **Duplicate**: copy the layer with all its marks.
- **Move Up** or **Move Down**: change the layer's place in the list.
- **Clear**: remove every mark on the layer but keep the layer.
- **Delete**: remove the layer and every mark on it.

You can also swipe left on a row for **Rename** and **Delete**. Clear and Delete ask you to confirm when the layer has marks on it.

A piece always keeps at least one layer, so Delete isn't available for the last one; clear it instead. If you delete the active layer, the top visible layer in the list becomes active.

## Layers on your other devices

If your library syncs with iCloud, your layers, their names and order, and which ones are hidden, sync to your other devices. The active layer is chosen on each device, so you can draw on different layers on your iPad and your iPhone.

## Layers when you share

Layers are personal: people in a shared folder or set list never see them. When you send a copy with **Share as PDF**, only the visible layers are printed into the PDF, so hide a layer first to leave it out. A Music Folder file includes your layers. See [Send a copy or print](/guide/send-a-copy-or-print).
