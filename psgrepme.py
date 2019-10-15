"""functional programming"""

import re

pattern = 'root'
"""http://collabedit.com/wsxep"""

matched_lines = filter(lambda line: re.search(pattern, line, re.I), open('/etc/passwd'))

for matched_line in matched_lines:
    print(matched_line, end='')