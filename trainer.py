#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

dictionaryFile = 'english-german.dic'
endOfDictionaryHeader = 11

englishToGerman = {}
germanToEnglish = {}
fp = open(dictionaryFile)
for index, line in enumerate(fp):
    if index >= endOfDictionaryHeader:
        (key, value) = line.split('\t')
        strippedKey = key.rstrip()
        strippedValue = value.rstrip()
        englishToGerman[strippedKey] = strippedValue
        germanToEnglish[strippedValue] = strippedKey

try:
    while True:
        germanWord = random.choice(germanToEnglish.keys())
        validEnglishWord = germanToEnglish[germanWord]
        englishWord = raw_input("\t%s = " % germanWord)
        if englishWord == validEnglishWord:
            print 'yes!!!'
        else:
            print 'sorry, right answer was "%s"' % validEnglishWord
except KeyboardInterrupt:
    exit
