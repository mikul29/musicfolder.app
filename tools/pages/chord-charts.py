def _dev(src, alt, kind="tablet"):
    w, h = {"tablet": (900, 1200), "landscape": (1306, 980)}[kind]
    cls = {"tablet": "device tablet fit", "landscape": "device tablet landscape fit"}[kind]
    return (f'<div class="{cls}"><div class="screen shot"><img src="/assets/{src}" alt="{alt}" '
            f'width="{w}" height="{h}" loading="lazy"></div></div>')


CONVERT = ('<div class="shot-stack">'
           '<figure>' + _dev("chart-pdf-original-ipad.jpg?v=1", "Holy, Holy, Holy as a PDF chord sheet in Music Folder on iPad: chords in blue over the lyrics, in a typewriter font", "landscape") +
           '<figcaption><b>Before: the PDF</b>A chord sheet exactly as it arrived.</figcaption></figure>'
           '<figure>' + _dev("chart-convert-ipad.jpg?v=1", "Reviewing the converted chart of Holy, Holy, Holy in Music Folder on iPad: the editable text on the left and the finished chart in D on the right", "landscape") +
           '<figcaption><b>After: an editable chart</b>Checked against the original before you save.</figcaption></figure>'
           '</div>')

KEYS = ('<div class="shot-stack">'
        '<figure><div class="shot-crop"><img src="/assets/chart-key-g.jpg?v=1" alt="Amazing Grace in Music Folder in its written key of G: G, G7, C, D and Em over the first verse" width="1000" height="560" loading="lazy"></div>'
        '<figcaption><b>As written, in G</b></figcaption></figure>'
        '<figure><div class="shot-crop"><img src="/assets/chart-key-a.jpg?v=1" alt="The same chart played in A: A, A7, D, E and F♯m over the same verse" width="1000" height="560" loading="lazy"></div>'
        '<figcaption><b>Played in A (Premium)</b></figcaption></figure>'
        '</div>')

SEQUENCE = ('<figure class="shot-crop"><img src="/assets/chart-sequence.jpg?v=1" alt="Edit Sequence in Music Folder on iPad for Blessed Assurance: Verse 1 and Chorus in order, with Verse, Chorus, Bridge, Intro, Outro, Ending, Instrumental, Interlude and Tag ready to add" '
            'width="1000" height="936" loading="lazy"></figure>')


PAGE = {
    "slug": "chord-charts",
    "menu_name": "Chord charts",
    "crumb": "Chord charts",
    "title": "Chord Chart App: Edit & Transpose Charts | Music Folder",
    "description": "Write chord charts or import ChordPro, convert PDF chord sheets into editable charts, and play them in any key or with a capo. Writing and reading charts is free; changing key is Premium.",
    "og_title": "Chord charts you can make your own",
    "og_description": "Write, import or convert chord charts, then play them in any key.",
    "h1": "Chord charts you can <em>make your own.</em>",
    "lede": "Write a chart, import a ChordPro file or turn a PDF chord sheet into a chart you can edit. Then play it in the singer's key, with a capo, or as Nashville numbers.",
    "hero_img": {"src": "chart-hero-ipad.jpg?v=1", "device": "tablet",
                 "alt": "Blessed Assurance as a chord chart in Music Folder on iPad: key D, 72 BPM and 9/8 at the top, the order V1 and C, then the verse and chorus with chords over the lyrics"},
    "how_heading": "From a lyric sheet to the stand.",
    "how": [
        ("Write or import", "Type the chords in the lyrics, paste a chart, import a ChordPro file or convert a PDF chord sheet."),
        ("Make it yours", "Put the sections in the order you play them, choose one column or two, and set the page size."),
        ("Play it your way", "Show chords, Nashville numbers or just the lyrics, free. Changing the key or playing with a capo is part of Premium, and your original stays as written."),
    ],
    "rows": [
        {"h2": "Write it, or <em>bring it in.</em>",
         "p": "The editor shows the chart beside a live preview of the printed page. Type chords inline or paste chords written above the lyrics, and Music Folder lines them up for you.",
         "points": ["ChordPro files (.cho, .chordpro, .pro, .crd, .txt)", "Title, artist, key, tempo and time at the top", "One editable chart instead of a PDF per key"],
         "row_class": "wide-visual",
         "img": {"src": "chart-editor-ipad.jpg?v=2", "device": "landscape",
                 "alt": "Editing a chord chart in Music Folder on iPad: the ChordPro text on the left and the formatted chart preview on the right"}},
        {"h2": "From a PDF chord sheet to <em>a chart you can edit.</em>",
         "p": "Have a chord sheet as a PDF? Convert it, and Music Folder reads the chords and lyrics, lays out the verses and choruses, and marks any line it isn't sure of so you can check it against the original. From then on it's a real chart: change a line, reorder the sections, play it in another key.",
         "points": ["Your PDF is kept, unchanged", "Flagged lines to review before you save", "For chord sheets (chords over lyrics), not staff notation"],
         "visual_html": CONVERT},
        {"h2": "Any key, <em>any capo.</em>",
         "p": "The same chart, two keys. Pick the singer's key, or a capo position to keep the chord shapes you know, and every chord on the chart changes with it. Your original stays as written.",
         "points": ["Changing key or capo is part of Premium", "Chords, Nashville numbers or lyrics only, free", "One chart for every key, no extra copies"],
         "visual_html": KEYS},
        {"h2": "Verses, choruses and <em>the order you play them.</em>",
         "p": "Label each verse, chorus and bridge as you write. Then set the performance order in Edit Sequence: tap a section to add it, repeat a chorus, drag to reorder. The order shows at the top of the chart, and Follow Sequence writes the song out in that order.",
         "points": ["Intro, verse, chorus, bridge, tag and more", "Repeat a section without retyping it", "Formatting too: columns, fonts and page size"],
         "visual_html": SEQUENCE},
        {"h2": "Straight into <em>the set list.</em>",
         "p": "Charts sit in the same library as your PDFs, so one set can mix chord charts, lead sheets and full scores.",
         "points": ["Charts and PDFs in one set", "Each piece keeps its own key and tempo", "Share charts with your band (Premium)"],
         "more": '<a href="/features/set-lists">How set lists work</a>',
         "img": {"src": "setlist-worship-ipad.jpg?v=3", "device": "landscape",
                 "alt": "A set list called Sunday Service in Music Folder on iPad: six hymns in order, each with author, key and tempo"}},
    ],
    "faq_heading": "Questions about chord charts",
    "faq": [
        ("Is the chord chart editor free?",
         "Yes. Writing, importing, converting and reading charts is free, and so is switching between Chords, Numbers and Lyrics. Changing a chart's key or capo is part of Premium."),
        ("Can I import ChordPro files?",
         "Yes. Music Folder opens ChordPro files ending in .cho, .chordpro, .pro or .crd, and plain .txt chord sheets."),
        ("Which PDFs can it convert?",
         "PDF chord sheets: chords written over lyrics, with readable text or a clear scan. After converting, you check any flagged lines against the original. Sheet music written on staves isn't converted."),
        ("Does changing the key change my chart?",
         "No. The chart keeps the key it was written in, and the key or capo you choose is how you see it. You can go back to the original at any time."),
        ("Can I show Nashville numbers?",
         "Yes. Choose Numbers to show every chord as a number in the key, or Lyrics to hide the chords."),
        ("Does it work with Planning Center?",
         "Yes. With Planning Center connected (Premium), your team's charts open in the plan's key, and you can save one to your own library. See <a href=\"/planning-center\">Planning Center</a>."),
    ],
    "more": [
        ("/for/worship-teams", "Worship teams", "Charts, lyric sheets and Sunday's set for the whole team."),
        ("/for/bands", "Bands", "Charts and set lists for every gig."),
        ("/features/set-lists", "Set lists", "Mix charts and scores in one set."),
        ("/features/sheet-music-reader", "Sheet music reader", "Read and perform with confidence."),
    ],
}
