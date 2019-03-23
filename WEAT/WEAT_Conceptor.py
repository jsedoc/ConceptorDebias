import numpy as np
from itertools import combinations, filterfalse
from sklearn.metrics.pairwise import cosine_similarity
from gensim.models.keyedvectors import KeyedVectors
import pandas as pd
import random
import sys
import os
import pickle
from Conceptors.conceptor_fxns import *
from lists.load_word_lists import *
import nltk
from nltk.corpus import brown

def swAB(W, A, B):
  """Calculates differential cosine-similarity between word vectors in W, A and W, B
     Arguments
              W, A, B : n x d matrix of word embeddings stored row wise
  """
  WA = cosine_similarity(W,A)
  WB = cosine_similarity(W,B)
  
  #Take mean along columns
  WAmean = np.mean(WA, axis = 1)
  WBmean = np.mean(WB, axis = 1)
  
  return (WAmean - WBmean)
  
def test_statistic(X, Y, A, B):
  """Calculates test-statistic between the pair of association words and target words
     Arguments
              X, Y, A, B : n x d matrix of word embeddings stored row wise
     Returns
              Test Statistic
  """
  return (sum(swAB(X, A, B)) - sum(swAB(Y, A, B)))

def weat_effect_size(X, Y, A, B, embd):
  """Computes the effect size for the given list of association and target word pairs
     Arguments
              X, Y : List of association words
              A, B : List of target words
              embd : Dictonary of word-to-embedding for all words
     Returns
              Effect Size
  """
  
  Xmat = np.array([embd[w.lower()] for w in X if w.lower() in embd])
  Ymat = np.array([embd[w.lower()] for w in Y if w.lower() in embd])
  Amat = np.array([embd[w.lower()] for w in A if w.lower() in embd])
  Bmat = np.array([embd[w.lower()] for w in B if w.lower() in embd])
  
  XuY = list(set(X).union(Y))
  XuYmat = []
  for w in XuY:
    if w.lower() in embd:
      XuYmat.append(embd[w.lower()])
  XuYmat = np.array(XuYmat)

  
  d = (np.mean(swAB(Xmat,Amat,Bmat)) - np.mean(swAB(Ymat,Amat,Bmat)))/np.std(swAB(XuYmat, Amat, Bmat))
  
  return d

def random_permutation(iterable, r=None):
  """Returns a random permutation for any iterable object"""
  pool = tuple(iterable)
  r = len(pool) if r is None else r
  return tuple(random.sample(pool, r))

def weat_p_value(X, Y, A, B, embd, sample = 1000):
  """Computes the one-sided P value for the given list of association and target word pairs
     Arguments
              X, Y : List of association words
              A, B : List of target words
              embd : Dictonary of word-to-embedding for all words
              sample : Number of random permutations used.
     Returns
  """
  size_of_permutation = min(len(X), len(Y))
  X_Y = X + Y
  test_stats_over_permutation = []
  
  Xmat = np.array([embd[w.lower()] for w in X if w.lower() in embd])
  Ymat = np.array([embd[w.lower()] for w in Y if w.lower() in embd])
  Amat = np.array([embd[w.lower()] for w in A if w.lower() in embd])
  Bmat = np.array([embd[w.lower()] for w in B if w.lower() in embd])
  
  if not sample:
      permutations = combinations(X_Y, size_of_permutation)
  else:
      permutations = [random_permutation(X_Y, size_of_permutation) for s in range(sample)]
      
  for Xi in permutations:
    Yi = filterfalse(lambda w:w in Xi, X_Y)
    Ximat = np.array([embd[w.lower()] for w in Xi if w.lower() in embd])
    Yimat = np.array([embd[w.lower()] for w in Yi if w.lower() in embd])
    test_stats_over_permutation.append(test_statistic(Ximat, Yimat, Amat, Bmat))
    
  unperturbed = test_statistic(Xmat, Ymat, Amat, Bmat)
  
  is_over = np.array([o > unperturbed for o in test_stats_over_permutation])
  
  return is_over.sum() / is_over.size

def process_cn_matrix(subspace, alpha = 2):
  """Returns the conceptor negation matrix
  Arguments
           subspace : n x d matrix of word vectors from a oarticular subspace
           alpha : Tunable parameter
  """
  # Compute the conceptor matrix
  C,_ = train_Conceptor(subspace, alpha)
  
  # Calculate the negation of the conceptor matrix
  negC = NOT(C)
  
  return negC

def apply_conceptor(x, C):
  """Returns the conceptored embeddings
  Arguments
           x : n x d matrix of all words to be conceptored
           C : d x d conceptor matrix
  """
  # Post-process the vocab matrix
  newX = (C @ x).T
  
  return newX

def load_all_vectors(embd, wikiWordsPath):
  """Loads all word vectors for all words in the list of words as a matrix
  Arguments
           embd : Dictonary of word-to-embedding for all words
           wikiWordsPath : URL to the path where all embeddings are stored
  Returns
          all_words_index : Dictonary of words to the row-number of the corresponding word in the matrix
          all_words_mat : Matrix of word vectors stored row-wise
  """
  all_words_index = {}
  all_words_mat = []
  with open(wikiWordsPath, "r+") as f_in:
    ind = 0
    for line in f_in:
      word = line.split(' ')[0]
      if word in embd:
        all_words_index[word] = ind
        all_words_mat.append(embd[word])
        ind = ind+1
        
  return all_words_index, all_words_mat

def load_subspace_vectors(embd, subspace_words):
  """Loads all word vectors for the particular subspace in the list of words as a matrix
  Arguments
           embd : Dictonary of word-to-embedding for all words
           subspace_words : List of words representing a particular subspace
  Returns
          subspace_embd_mat : Matrix of word vectors stored row-wise
  """
  subspace_embd_mat = []
  ind = 0
  for word in subspace_words:
    if word in embd:
      subspace_embd_mat.append(embd[word])
      ind = ind+1
      
  return subspace_embd_mat

"""Load list of pronouns representing the 'Pronoun' subspace for gender debiasing"""
gender_list_pronouns = WEATLists.W_7_Male_terms + WEATLists.W_7_Female_terms + WEATLists.W_8_Male_terms + WEATLists.W_8_Female_terms
gender_list_pronouns = list(set(gender_list_pronouns))

"""Load an extended list of words representing the gender subspace for gender debiasing"""
gender_list_extended = male_vino_extra + female_vino_extra + male_gnGlove + female_gnGlove
gender_list_extended = list(set(gender_list_extended))

"""Load list of proper nouns representing the 'Proper Noun' subspace for gender debiasing"""
gender_list_propernouns = male_cmu + female_cmu
gender_list_propernouns = list(set(gender_list_propernouns))

"""Load list of all representing the gender subspace for gender debiasing"""
gender_list_all = gender_list_pronouns + gender_list_extended + gender_list_propernouns
gender_list_all = list(set(gender_list_all))

"""Load list of common black and white names for racial debiasing"""
race_list = WEATLists.W_3_Unused_full_list_European_American_names + WEATLists.W_3_European_American_names + WEATLists.W_3_Unused_full_list_African_American_names + WEATLists.W_3_African_American_names + WEATLists.W_4_Unused_full_list_European_American_names + WEATLists.W_4_European_American_names + WEATLists.W_4_Unused_full_list_African_American_names + WEATLists.W_4_African_American_names + WEATLists.W_5_Unused_full_list_European_American_names + WEATLists.W_5_European_American_names + WEATLists.W_5_Unused_full_list_African_American_names + WEATLists.W_5_African_American_names 
race_list = list(set(race_list))

"""Load the embeddings to a gensim object"""
resourceFile = ''
if 'glove' not in dir():
  glove = KeyedVectors.load_word2vec_format(resourceFile + 'gensim_glove.840B.300d.txt.bin', binary=True)
  print('The glove embedding has been loaded!')

"""Load the embeddings to a gensim object"""
resourceFile = ''
if 'word2vec' not in dir():
  word2vec = KeyedVectors.load_word2vec_format(resourceFile + 'GoogleNews-vectors-negative300.bin', binary=True)
  print('The word2vec embedding has been loaded!')

"""Load the embeddings to a gensim object"""
resourceFile = ''
if 'fasttext' not in dir():
  fasttext = KeyedVectors.load_word2vec_format(resourceFile + 'fasttext.bin', binary=True)
  print('The fasttext embedding has been loaded!')

"""Load the embeddings to a dictonary"""
data = pickle.load(open("elmo_embeddings_emma_brown.pkl", "rb"))

def pick_embeddings(corpus, sent_embs):
	X = []
	labels = {}
	sents = []
	ind = 0
	for i, s in enumerate(corpus):
	    for j, w in enumerate(s):
	        X.append(sent_embs[i][j])
	        if w.lower() in labels:
	          labels[w.lower()].append(ind)
	        else:
	          labels[w.lower()] = [ind]
	        sents.append(s)
	        ind = ind + 1
	return (X, labels, sents)
  
def get_word_list(path):
    word_list = []
    with open(path, "r+") as f_in:
      for line in f_in:
        word = line.split(' ')[0]
        word_list.append(word.lower())

    return word_list

def load_subspace_vectors_contextual(all_mat, all_index, subspace_list):
    subspace_mat = []
    for w in subspace_list:
      if w.lower() in all_index:
        for i in all_index[w.lower()]:
          #print(type(i))
          subspace_mat.append(all_mat[i])
    #subspace_mat = [all_mat[i,:] for i in all_index[w.lower()] for w in subspace_list if w.lower() in all_index]
    print("Subspace: ", np.array(subspace_mat).shape)
    return subspace_mat

nltk.download('brown')

brown_corpus = brown.sents()
elmo = data['brown_embs']

def load_bert(all_dict, subspace):
  """Loads all embeddings in a matrix and a dictonary of words to row numbers"""
  all_mat = all_dict['big_bert_' + subspace + '.pkl']['type_embedings']
  words = []
  for name in all_dict:
    all_mat = np.concatenate((all_mat, all_dict[name]['type_embedings']))
    words += all_dict[name]['words']
  
  words = [w.lower() for w in words]
  all_words_index = {}
  for i,a in enumerate(words):
    all_words_index[a] = i
    
  return all_words_index, all_mat

def load_bert_conceptor(all_dict, subspace):
  """Loads the required BERT conceptor matrix"""
  if subspace == 'gender_list_pronouns':
    cn = all_dict['big_bert_gender_list_pronouns.pkl']['GnegC']
  elif subspace == 'gender_list_propernouns':
    cn = all_dict['big_bert_gender_list_propernouns.pkl']['GnegC']
  elif subspace == 'gender_list_extended':
    cn = all_dict['big_bert_gender_list_extended.pkl']['GnegC']
  elif subspace == 'gender_list_all':
    cn = all_dict['big_bert_gender_list_all.pkl']['GnegC']
  elif subspace == 'race_list':
    cn = all_dict['big_bert_race_list.pkl']['GnegC']
  
  return cn

"""Load all bert embeddings in a dictonary"""
all_dict = {}
for filename in os.listdir('/home/saketk/bert'):
  all_dict[filename] = pickle.load(open(filename, "rb"))
  
resourceFile = ''
wikiWordsPath = resourceFile + 'SIF/auxiliary_data/enwiki_vocab_min200.txt' # https://github.com/PrincetonML/SIF/blob/master/auxiliary_data/enwiki_vocab_min200.txt

#List of all embeddings to test on
all_embd = ['glove', 'word2vec', 'fasttext','elmo']

#List of all subspaces for gender
all_subspace = ['without_conceptor','gender_list_pronouns', 'gender_list_extended','gender_list_propernouns', 'gender_list_all', 'gender_list_and']

#List of all subsoaces for race
# all_subspace = ['without_conceptor', 'race_list']

# career = WEATLists.W_6_Career
# family = WEATLists.W_6_Family
# male = WEATLists.W_6_Male_names
# female = WEATLists.W_6_Female_names

white = WEATLists.W_5_Unused_full_list_European_American_names
black = WEATLists.W_5_Unused_full_list_African_American_names
pleasant = WEATLists.W_5_Pleasant
unpleasant = WEATLists.W_5_Unpleasant

# science = WEATLists.W_8_Science
# arts = WEATLists.W_8_Arts
# male = WEATLists.W_8_Male_terms
# female = WEATLists.W_8_Female_terms


results = []

for embd in all_embd:
  #Initialize the embeddings to be used
  curr_embd = eval(embd)
  
  #Load all embeddings in a matrix of all words in the wordlist
  if embd == 'elmo' or embd == 'bert':
    #wiki_words = get_word_list('SIF/auxiliary_data/enwiki_vocab_min200.txt')
    all_words_mat, all_words_index, _ = pick_embeddings(brown_corpus, curr_embd)
    print("All mat: ", np.array(all_words_mat).shape)
    print("Number of words: ", len(list(all_words_index.keys())))
  else:
    all_words_index, all_words_mat = load_all_vectors(curr_embd, wikiWordsPath)
  
  for subspace in all_subspace:
    
    if subspace != 'without_conceptor' and subspace != 'gender_list_and':
      subspace_words_list = eval(subspace)

    
    if subspace != 'without_conceptor':
      #CN all word embeddings using the respective subspace
      if subspace == 'gender_list_and':
        if embd == 'elmo' or embd == 'bert':
          subspace_words_mat1 = load_subspace_vectors_contextual(all_words_mat, all_words_index, gender_list_pronouns)
          cn1 = process_cn_matrix(np.array(subspace_words_mat1).T, alpha = 8)

          subspace_words_mat2 = load_subspace_vectors_contextual(all_words_mat, all_words_index, gender_list_extended)
          cn2 = process_cn_matrix(np.array(subspace_words_mat2).T, alpha = 3)

          subspace_words_mat3 = load_subspace_vectors_contextual(all_words_mat, all_words_index, gender_list_propernouns)
          cn3 = process_cn_matrix(np.array(subspace_words_mat3).T, alpha = 10)

          cn = AND(cn1, AND(cn2, cn3))
          all_words_cn = apply_conceptor(np.array(all_words_mat).T, np.array(cn))
          print("All mat CN: ", np.array(all_words_cn).shape)
        else:
          subspace_words_mat1 = load_subspace_vectors(curr_embd, gender_list_pronouns)
          cn1 = process_cn_matrix(np.array(subspace_words_mat1).T)

          subspace_words_mat2 = load_subspace_vectors(curr_embd, gender_list_extended)
          cn2 = process_cn_matrix(np.array(subspace_words_mat2).T)

          subspace_words_mat3 = load_subspace_vectors(curr_embd, gender_list_propernouns)
          cn3 = process_cn_matrix(np.array(subspace_words_mat3).T)

          cn = AND(cn1, AND(cn2, cn3))
          all_words_cn = apply_conceptor(np.array(all_words_mat).T, np.array(cn))
      else:
        #Load all embeddings of the subspace as a matrix
        if embd == 'elmo' or embd == 'bert':
          subspace_words_mat = load_subspace_vectors_contextual(all_words_mat, all_words_index, subspace_words_list)
          cn = process_cn_matrix(np.array(subspace_words_mat).T, alpha = 6)
          all_words_cn = apply_conceptor(np.array(all_words_mat).T, np.array(cn))
          print("Subspace mat: ", np.array(subspace_words_mat).shape)
        else:
          subspace_words_mat = load_subspace_vectors(curr_embd, subspace_words_list)
          cn = process_cn_matrix(np.array(subspace_words_mat).T)
          all_words_cn = apply_conceptor(np.array(all_words_mat).T, np.array(cn))
    else:
      all_words_cn = all_words_mat
    all_words_cn = np.array(all_words_cn)
    print("All CN: ", all_words_cn.shape)
    #Store all conceptored words in a dictonary
    all_words = {}
    for word, index in all_words_index.items():
      #print(word, index)
      if embd == 'elmo' or embd == 'bert':
        all_words[word] = np.mean([all_words_cn[i,:] for i in index], axis = 0)
      else:
        all_words[word] = all_words_cn[index,:]
#     print("LAST: ", np.array(all_words["a"]).shape)
    if subspace == 'without_conceptor':
      #WITHOUT CONCEPTOR
      d_cn = weat_effect_size(white, black, pleasant, unpleasant, all_words)
      p_cn = weat_p_value(white, black, pleasant, unpleasant, all_words, 1000)
      print("Without conceptor")
      print('WEAT d = ', d_cn)
      print('WEAT p = ', p_cn)
    else:
      #WITH CONCEPTOR
      d_cn = weat_effect_size(white, black, pleasant, unpleasant, all_words)
      p_cn = weat_p_value(white, black, pleasant, unpleasant, all_words, 1000)
      print("With conceptor: ", embd, subspace)
      print('WEAT d = ', d_cn)
      print('WEAT p = ', p_cn)
    
    row = [embd, subspace, d_cn, p_cn]
    results.append(row)
    
pd.DataFrame(np.array(results), columns = ['Embedding', 'Subspace', 'Effect Size', 'p-value'])


