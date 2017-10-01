
# -*- coding:utf-8 -*-

import sys

# Read data
data = [line.strip() for line in sys.stdin]

unique_notes = ['A ', 'B ', 'C ', 'D ', 'E ', 'F ', 'G ']
alternate_notes = {'A#': 'Bb',
                   'Bb': 'A#',
                   'C#': 'Db',
                   'Db': 'C#',
                   'D#': 'Eb',
                   'Eb': 'D#',
                   'F#': 'Gb',
                   'Gb': 'F#',
                   'G#': 'Ab',
                   'Ab': 'G#'}

# For each case, display the case number followed by the alternate key name, if it exists, or print UNIQUE if the key
# name is unique. Follow the format of the sample output.
for i, note in enumerate(data):

    if note[:2] in unique_notes:
        print 'Case {}: UNIQUE'.format(i + 1)

    else:
        print 'Case {}: {} {}'.format(i + 1, alternate_notes[note[:2]], note[-5:])
