# -*- coding: utf-8 -*-
"""
This is code to load all of the word lists for our paper.
"""

if not 'sys_lists' in dir():
    sys_lists = dir()
sys_lists += 'sys_lists'

wikiWordsPath = '/content/' + 'enwiki-20150602-words-frequency.txt'
wikiWords = []
with open(wikiWordsPath, "r+") as f_in:
    for line in f_in:
      one_line = line.split(' ')
      if int(one_line[1]) > 200:
        wikiWords.append(one_line[0]) 
        
wikiWordsPath = '/content/' + '/SIF/auxiliary_data/enwiki_vocab_min200.txt'
with open(wikiWordsPath, "r+") as f_in:
    for line in f_in:
        wikiWords.append(line.split(' ')[0])

from ConceptorDebias.Greenwald_1998_Perez_2010_lists import *
from ConceptorDebias.WEAT_lists import *

winoWordsPath = '/content/' + 'corefBias/WinoBias/wino/extra_gendered_words.txt'
male_vino_extra = []
female_vino_extra = []
with open(winoWordsPath, "r+") as f_in:
    for line in f_in:
        male_vino_extra.append(line.split('\t')[0])
        female_vino_extra.append(line.strip().split('\t')[1])

gnGloveFemaleWordPath = '/content/' + 'gn_glove/wordlist/female_word_file.txt'
female_gnGlove = []
with open(gnGloveFemaleWordPath, "r+") as f_in:
    for line in f_in:
        female_gnGlove.append(line.strip())
gnGloveMaleWordPath = '/content/' + 'gn_glove/wordlist/male_word_file.txt'
male_gnGlove = []
with open(gnGloveMaleWordPath, "r+") as f_in:
    for line in f_in:
        male_gnGlove.append(line.strip())

cmuMaleWordPath = '/content/' + 'male.txt'
male_cmu = []
with open(cmuMaleWordPath, "r+") as f_in:
  for line in f_in:
    w = line.strip()
    if len(w)>0 and w[0] != '#':
      male_cmu.append(w)
cmuFemaleWordPath = '/content/' + 'female.txt'
female_cmu = []
with open(cmuFemaleWordPath, "r+") as f_in:
  for line in f_in:
    w = line.strip()
    if len(w)>0 and w[0] != '#':
      female_cmu.append(w)

vocab = []
for x in dir():
    if type(eval(x)) == list and x not in sys_lists:
        vocab += eval(x)
vocab = list(set(vocab))
len(vocab)
