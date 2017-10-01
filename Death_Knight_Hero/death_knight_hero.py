
# -*- coding:utf-8 -*-

import sys
import re

# Count the number of battles our hero won
victory = 0

for i, line in enumerate(sys.stdin):

    # If not at index 0
    if i > 0:

        # If not Chains of Ice immediately followed by Death Grip
        bad_combo = re.search('CD', line)

        if not bad_combo:
            victory += 1

print victory
