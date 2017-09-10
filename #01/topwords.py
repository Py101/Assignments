#!/usr/bin/env python
import re
import sys
from collections import Counter
from signal import signal, SIGPIPE, SIG_DFL
signal(SIGPIPE,SIG_DFL) 

num_words = None
text = sys.stdin.read().lower()
words = re.split('\W+', text)
cnt = Counter(words)
for word, count in cnt.most_common(num_words):
	print(word)

