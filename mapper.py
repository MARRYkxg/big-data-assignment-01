#!/usr/bin/env python
#
# This file has been provided as a starting point. You need to modify this file.
# Reads whole lines stdin; writes key/value pairs to stdout
# --- DO NOT MODIFY ANYTHING ABOVE THIS LINE ---

import re
import datetime
import sys

form = re.compile('\[\d\d\/\w\w\w\/\d\d\d\d')

if __name__ == "__main__":
	for line in sys.stdin:
		for word in line.split():
			if form.match(word):
				word = word[4:12]
				word = datetime.datetime.strptime(word, '%b/%Y')
				word = word.strftime('%Y-%m')
				print(word + "\t" + "1")

