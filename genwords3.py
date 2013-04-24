from random import sample, randint
import re
import codecs

out = codecs.open('out.txt', 'w', 'utf-8')
text = ""

for _ in range(1, 1000):
	words = [re.sub('[.\'"?!;`()\[\]:*]', '', word) for word in open('latas.txt').read().split() if len(word) > 3]
	text += " ".join(sample(words, randint(3,8))).capitalize() + '.\n'
	if _ % 4 == 0:
		text += '\n'

text = text.replace("“", "")
text = text.replace("„", "")
text = text.replace(",.", ".")

out.write(text)
out.close()