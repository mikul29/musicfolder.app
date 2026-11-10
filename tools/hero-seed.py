"""Writes the 4.2 hero seed (seed.json + PDFs) for the app's DEBUG marketing seed
(-MFSeedLibrary marketing -MFMarketingSeedDir <out>):

  python3 tools/hero-seed.py <out-dir>

Content = the home-page hero's: the onboarding film's seed-v3 (Summer Night Concert
tomorrow, the six website folders and their counts, a two-week practice streak), plus the
six public-domain scores that fly out of the folder's pocket (assets/scores/*.webp), opened
in slot order so Recently opened shows exactly those pages.
"""
import json, pathlib, shutil, sys

MF = pathlib.Path.home() / 'Documents/Me/Music_Folder'
V3 = MF / 'Onboarding-Video-Preview/screens/seed-v3'
OS = MF / 'openscore-catalog/PDFs'
out = pathlib.Path(sys.argv[1]); out.mkdir(parents=True, exist_ok=True)

seed = json.load(open(V3 / 'seed.json'))
for s in seed['songs']:
    shutil.copyfile(V3 / s['file'], out / s['file'])

# slot order on the screen (assets/scores/<sheet>.webp ↔ its PDF); Lágrima is already in seed-v3
SCORES = [
    ('dvorak.pdf', 'String Quartet No. 12 "American"', 'Antonín Dvořák', 'F', 112, '4/4',
     'Antonín Dvořák - String Quartet No12 Op96 American.pdf'),
    (None, 'Lágrima', None, None, None, None, None),
    ('widmung.pdf', 'Widmung', 'Robert Schumann', 'Ab', 72, '3/2', 'Robert Schumann - Widmung.pdf'),
    ('debussy.pdf', 'Harmonie du Soir', 'Claude Debussy', 'B', 60, '3/4', 'Claude Debussy - Harmonie du Soir.pdf'),
    ('chaminade.pdf', 'Les Rêves', 'Cécile Chaminade', 'Eb', 92, '4/4', 'Cécile Chaminade - Les Rêves.pdf'),
    ('holmes.pdf', 'Le retour du paladin', 'Augusta Holmès', 'C', 80, '4/4', 'Augusta Holmès - Le retour du paladin.pdf'),
]
for f, name, comp, key, tempo, ts, src in SCORES:
    if f:
        shutil.copyfile(OS / src, out / f)
        seed['songs'].append(dict(file=f, name=name, composer=comp, key=key, tempo=tempo,
                                  timeSignature=ts, folders=[]))
seed['recents'] = [s[1] for s in SCORES]   # first = most recent = the first slot
# tags, as the old Library screenshot showed them (#difficult #easy #hymn #pop; the seed has no jazz)
TAGS = {'pop': ['Let it Be', 'Hallelujah', 'Yesterday', 'Hey Jude', 'Imagine'],
        'easy': ['Let it Be', 'Silent Night', 'Lágrima', 'Cradle Song'],
        'difficult': ['String Quartet No. 12 "American"', 'Quartettsatz', 'Widmung', 'Harmonie du Soir'],
        'hymn': [c['name'] for c in seed['charts'] if 'Worship Team' in c['folders']]}
tags = {}
for t, names in TAGS.items():
    for n in names: tags.setdefault(n, []).append(t)
seed['tags'] = tags
json.dump(seed, open(out / 'seed.json', 'w'), ensure_ascii=False, indent=1)
print(len(seed['songs']), 'pdfs,', len(seed['charts']), 'charts,', 'recents:', seed['recents'], '→', out)
