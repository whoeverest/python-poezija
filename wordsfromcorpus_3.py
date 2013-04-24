# -*- coding: utf-8 -*-
import re
import codecs

path = "corpus.txt"

def words_from_corpus():
	f = open(path)
	text = re.sub('[()0-9.,?!;:\'"\]\[]', '', f.read())
	text = text.replace('“', '')
	text = text.replace('„', '')
	text = text.replace('–', '')
	text = text.lower()
	return text.split()

f = codecs.open('words.txt', 'w', 'utf-8')
f.write('\n'.join(words_from_corpus()))
f.close()