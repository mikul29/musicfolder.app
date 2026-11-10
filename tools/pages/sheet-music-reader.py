def _dev(src, alt, kind="tablet"):
    w, h = {"tablet": (900, 1200), "landscape": (1306, 980)}[kind]
    cls = {"tablet": "device tablet fit", "landscape": "device tablet landscape fit"}[kind]
    return (f'<div class="{cls}"><div class="screen shot"><img src="/assets/{src}" alt="{alt}" '
            f'width="{w}" height="{h}" loading="lazy"></div></div>')


def _pair(a, b):
    """Two real screens side by side, each with a short caption."""
    return '<div class="shot-pair">' + "".join(
        f'<figure>{_dev(src, alt)}<figcaption><b>{title}</b>{cap}</figcaption></figure>'
        for src, alt, title, cap in (a, b)) + "</div>"


HALF_PAGE = _pair(
    ("reader-half-before-ipad.jpg?v=1",
     "Fauré's Pavane in Music Folder on iPad, page 1 shown in full",
     "Playing page 1", "The whole page, as usual."),
    ("reader-half-split-ipad.jpg?v=1",
     "The same Pavane halfway through a turn: the top of page 2 above, the end of page 1 below a thin edge",
     "After one press", "Page 2 begins above; the end of page 1 stays below."),
)

LIGHT_DARK = _pair(
    ("reader-pm-light-ipad.jpg?v=1",
     "Fauré's Sicilienne in Music Folder on iPad in Performance Mode on a white page",
     "Light page", "Black notes on white, as printed."),
    ("reader-pm-dark-ipad.jpg?v=1",
     "The same Sicilienne, same view and zoom, with Dark Background: light notation on a dark page",
     "Dark Background", "Light notes on a dark page."),
)

TOOLBAR = ('<figure class="shot-crop"><img src="/assets/reader-toolbar-edit.jpg?v=2" alt="The top of the reader in '
           'Music Folder on iPad while customizing the toolbar: each tool shows a minus to remove it and a green plus '
           'adds more" width="1000" height="864" loading="lazy"></figure>')

# Page Links, animated from two real captures of the same screen (before / after the
# jump): a tap lands on the orange link, the coda is circled and Back appears; a tap on
# Back returns. The tap mark and the landing ripple are the only drawn elements. Reduced motion: the after frame.
LINK_DEMO = ('<div class="device tablet fit link-demo"><div class="screen shot">'
             '<img src="/assets/reader-page-links-before-ipad.jpg?v=1" alt="Fauré\'s Sicilienne in Music Folder on iPad: '
             'a tap on the orange Page Link beside the To Coda sign jumps to the coda, which is circled, and a Back to p. 1 '
             'button appears at the bottom; a tap on Back returns" width="900" height="1200" loading="lazy">'
             '<img class="ld-after" src="/assets/reader-page-links-ipad.jpg?v=1" alt="" aria-hidden="true" width="900" height="1200" loading="lazy">'
             '<span class="ld-land" aria-hidden="true"></span><span class="ld-tap" aria-hidden="true"></span>'
             '</div></div>')

MORE_WAYS = """
<section class="section" style="padding-top:0">
  <div class="wrap">
    <div class="display-options">
      <div class="rf-text"><h2 class="heading-sm">A page that suits <em>the room.</em></h2><p>On a dim stage or late at night, switch on Dark Background for light notation on a dark page. It changes only how the page looks on screen: your PDF, thumbnails and exports stay as they are.</p><ul class="rf-points"><li>{c}<span>On or off from the reader's menu, in every reader</span></li><li>{c}<span>Works with Performance Mode, crops and your markings</span></li><li>{c}<span>Needs iOS 16 or later</span></li></ul></div>
      <div class="rf-visual">{pair}</div>
    </div>
    <div class="section-head"><h2 class="heading-sm">Everything else <em>within reach.</em></h2></div>
    <ul class="mini-grid">
      <li><h3>Notes beside the score</h3><p>Keep reminders for each piece in a notes panel next to the music, there whenever you open it.</p></li>
      <li><h3>Hands-free page turns</h3><p>Use a Bluetooth pedal, or Face Gestures with Premium. <a href="/features/page-turner">Page turner</a></p></li>
      <li><h3>Write on the page</h3><p>Mark up any score with Apple Pencil or your finger, in layers you can hide. <a href="/features/annotation">Annotation</a></p></li>
      <li><h3>Play along with a recording</h3><p>Attach a recording to a piece and play it from the reader, slowed down or in another key.</p></li>
      <li><h3>Tuner, metronome and piano</h3><p>The practice tools open over the score, without leaving it. Part of Premium. <a href="/features/toolkit">Toolkit</a></p></li>
      <li><h3>Chord charts in any key</h3><p>Charts open in the same reader; changing key or capo is part of Premium. <a href="/features/chord-charts">Chord charts</a></p></li>
    </ul>
  </div>
</section>
""".replace("{pair}", LIGHT_DARK).replace("{c}", '<svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 8.5l3 3 7-7"/></svg>')

PAGE = {
    "slug": "sheet-music-reader",
    "menu_name": "Reader",
    "crumb": "Sheet music reader",
    "title": "Sheet Music Reader for iPad & iPhone | Music Folder",
    "description": "A PDF sheet music reader built for performing: Performance Mode, links for repeats and codas, half-page turns, a dark background and margins cropped for bigger notes.",
    "og_title": "A sheet music reader built for the moment you perform",
    "og_description": "Performance Mode, Page Links, half-page turns and a dark background, on iPad and iPhone.",
    "h1": "A sheet music reader built for <em>the moment you perform.</em>",
    "lede": "Open any PDF and perform with confidence. Keep your music front and center, navigate repeats with a tap, and turn pages without losing your place.",
    "hero_img": {"src": "reader-light-ipad.jpg?v=1", "device": "tablet",
                 "alt": "Fauré's Après un rêve open in the Music Folder reader on iPad: the first page of the song for voice and piano, with the reader's tools above it"},
    "how_heading": "From score to stage, without the fuss.",
    "how": [
        ("Open your music", "Open any PDF, scan or chord chart in your library, or go straight to one piece inside a book."),
        ("Make it yours", "If you like, crop the margins, turn on half-page turns or link the repeats. It's all optional, and remembered for next time."),
        ("Perform with confidence", "Turn on Performance Mode and play. Turn pages with a tap, a swipe or a Bluetooth pedal."),
    ],
    "rows": [
        {"h2": "Stay focused on <em>the music.</em>",
         "p": "Performance Mode clears the screen down to your score. The toolbars step aside and the whole page becomes a page-turn area, so a stray touch never opens a menu, zooms in or starts a marking in the middle of a piece.",
         "points": ["Tap the right side to go on, the left to go back", "Start a whole set list with Perform Set", "Optional protection against accidental double turns"],
         "img": {"src": "reader-pm-light-ipad.jpg?v=1", "device": "tablet",
                 "alt": "Fauré's Sicilienne in Music Folder on iPad in Performance Mode: the full page of music, with only a small metronome, play and Done control above it"}},
        {"h2": "From D.S. to coda, <em>in one tap.</em>",
         "p": "Signs like D.S. (go back to the sign) and To Coda (skip ahead to the ending) usually mean hunting for the right page mid-performance. Link each sign to where it goes once, and from then on one tap takes you there.",
         "points": ["Set up once per piece, in a short guided flow", "Tap Back to return to exactly where you were", "Links stay in place when you edit the pages"],
         "visual_html": LINK_DEMO},
        {"h2": "Read across <em>the page break.</em>",
         "p": "With Half-Page Turns, the first press brings in the top of the next page while the end of the current one stays in view, so you can keep reading through the turn. The second press finishes it.",
         "points": ["Works with a tap, a swipe or a pedal", "Back works the same way, one step at a time", "For pianists, accompanists and long parts"],
         "visual_html": HALF_PAGE, "row_class": "wide-visual"},
        {"h2": "Two pages, <em>side by side.</em>",
         "p": "Turn your iPad sideways or widen the window on a Mac and see two pages at once, the way the music sits on a piano stand.",
         "points": ["Two-Page View on iPad and Mac", "Landscape and portrait on every device", "Or scroll through the score continuously"],
         "img": {"src": "reader-two-page-ipad.jpg?v=1", "device": "landscape",
                 "alt": "Fauré's Après un rêve in Music Folder on iPad in landscape, showing pages 1 and 2 side by side"}},
        {"h2": "More music. <em>Less margin.</em>",
         "p": "Many PDFs carry wide white margins. Crop them away and the notation grows to fill the screen, easier to read from the stand. Cropping only changes how the page is shown; your PDF itself is never modified.",
         "points": ["Auto finds the music; the handles fine-tune it", "Crop one page or every page at once", "Reset always brings back the whole page"],
         "img": {"src": "reader-crop-ipad.jpg?v=1", "device": "tablet",
                 "alt": "Crop All Pages in Music Folder on iPad: the Sicilienne page with orange crop handles, This Page and All Pages, Auto and Reset"}},
        {"h2": "One PDF, many pieces, <em>instantly accessible.</em>",
         "p": "Keep a hymnal, a method book or a multi-movement work as one PDF. The Sections button lists every piece inside; tap one and you're on its first page. Each section keeps its own key and tempo, and the metronome follows the tempo of the section you're in.",
         "points": ["A checkmark shows the piece you're in", "Add a section while you read", "Metronome playback is part of Premium"],
         "img": {"src": "reader-sections-hymn-ipad.jpg?v=1", "device": "tablet",
                 "alt": "A Hymnal open in Music Folder on iPad at Be Thou My Vision, with the Sections list beside it: Abide With Me, Be Still My Soul, Be Thou My Vision (checked), Blessed Assurance and more, each with its page"}},
        {"h2": "Your reader, <em>your way.</em>",
         "p": "Read a page at a time, scroll continuously or see two pages side by side. Put the tools you reach for on the toolbar, in the order you like, and leave the rest in the menu, so the score keeps the space.",
         "points": ["Add, remove and reorder toolbar tools", "Single pages, vertical scrolling or Two-Page View", "Portrait or landscape, on iPhone, iPad and Mac"],
         "visual_html": TOOLBAR},
    ],
    "extra_section": MORE_WAYS,
    "band_cta": {"h2": "Your next performance, <em>on one screen.</em>",
                 "p": "Performance Mode, Page Links, Half-Page Turns, Two-Page View, cropping and Dark Background are all in the free version.",
                 "link_href": "/pricing", "link_text": "Compare Free and Premium"},
    "faq_heading": "Questions about the reader",
    "faq": [
        ("Is the reader free?",
         "Yes. Performance Mode, Page Links, Half-Page Turns, Two-Page View, Dark Background and cropping are all part of the free version. Metronome playback and Face Gestures in the reader are part of Premium."),
        ("What happens if I touch the page in Performance Mode?",
         "Only page turns. A tap on the right of the page goes forward and a tap on the left goes back, so nothing else opens, zooms or draws. Hold Done to leave."),
        ("How do Page Links work?",
         "In a piece, open ⋯ › Page Links and a short guided setup asks for the sign and the place it jumps to. While you play, tap the link to jump and tap Back to return."),
        ("Can I turn pages with a pedal?",
         "Yes. Bluetooth page turners work in every reader, including Performance Mode and half-page turns. See the <a href=\"/features/page-turner\">Page turner</a> page for pedals and hands-free Face Gestures."),
        ("Can I read on my iPhone too?",
         "Yes. The reader works on iPhone and iPad with iOS 15 or later, and on Macs with Apple silicon. Two-Page View needs the width of an iPad or Mac, and Dark Background needs iOS 16 or later."),
        ("Can I write on the score while I read?",
         "Yes. Tap the pencil to mark up the page with Apple Pencil or your finger. See <a href=\"/features/annotation\">Annotation</a>."),
    ],
    "more": [
        ("/features/page-turner", "Page turner", "Turn pages hands-free with a pedal or your face."),
        ("/features/annotation", "Annotation", "Write on any score with Apple Pencil or your finger."),
        ("/features/sheet-music-organizer", "Sheet music organizer", "Folders, sections and a library you can search."),
        ("/features/set-lists", "Set lists", "Play the whole set straight through."),
    ],
}
