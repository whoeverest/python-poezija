# -*- coding: utf-8 -*-
import codecs
from random import sample, randint, choice, uniform
from collections import defaultdict

def syllables(word):
    
    def iter_with_context(word):
        """ [1,2,3,4] => [(1,2,3), (2,3,4) ... (pre, this, post)]"""
        for pre, this, post in zip(word, word[1:], word[2:]):
            yield (pre, this, post)
   
    s = 0
    vowels = u'аеиоуАЕИОУ'

    # count the vowels
    s += sum(1 for letter in word if letter in vowels)

    # begins with 'r' and is not followed by a vowel
    if (word[0] in u'рР') and (word[1] not in vowels):
        s += 1

    # 'r' surrounded by non-vowels
    for letter in iter_with_context(word):
        pre, this, post = letter
        if (pre not in vowels) and (this in u'рР') and (post not in vowels):
            s += 1
    
    return s

def rhymes(first, second):
    """ Returns a value from 0.0 to 1.0 describing how much
    two words rhyme. Could be improved with a non-linear
    scale or maybe syllable splitting.
    """
    s = 0
    for a, b in zip(first[::-1], second[::-1]):
        if not a == b:
            break
        s += 1
    return float(s) / max(len(first), len(second))

def rhymes_sentence(sent_one, sent_two):
    # reverse and remove empty spaces
    rev_sent_one = sent_one[::-1].replace(' ', '')
    rev_sent_two = sent_two[::-1].replace(' ', '')

    print rev_sent_two, rev_sent_one

    matches = 0
    for letter_one, letter_two in zip(rev_sent_one, rev_sent_two):
        if letter_one == letter_two:
            matches += 1
        else:
            break

    return float(matches) / min(len(sent_one), len(sent_two))


words = [word.strip() for word in codecs.open('words.txt', 'r', 'utf-8').readlines()]
    
def word_and_following():
    follows = defaultdict(list)
    for first, second in zip(words, words[1:]):
        follows[first].append(second)
    return follows

follows = word_and_following()

def generate_sentance():
    length = randint(1,7)
    sentence = [choice(words)]
    while len(sentence) < length:
        if not follows[sentence[-1]]:
            break
        sentence.append(choice(follows[sentence[-1]]))
    return ' '.join(sentence)

def generate_title():
    while True:
        title = choice(words)
        if len(title) > 4:
            return title

def generate_poem():
    res = [generate_sentance()]
    length = randint(4,12)
    while True:
        if len(res) >= length:
            break
        snt = generate_sentance()
        snt_last_word = snt.split()[-1]
        res_last_word = res[-1].split()[-1]
        if len(snt_last_word) <= 3:
            continue
        if snt_last_word == res_last_word:
            continue
#        if not rhymes(snt_last_word, res_last_word) > 0.3:
#            continue
        res.append(snt)
    return '\n'.join(res)

# print generate_poem()

o = codecs.open('out.txt', 'w', 'utf-8')

for _ in range(100):
    title = generate_title()
    poem = generate_poem()
    if not poem:
        continue
    o.write(title)
    o.write('\n\n')
    o.write(poem)
    o.write('\n\n\n')
