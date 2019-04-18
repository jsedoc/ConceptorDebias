#!/bin/bash

rm -r ConceptorDebias
git clone https://github.com/jsedoc/ConceptorDebias
cd ConceptorDebias; git checkout ACL-cleanup

# General word list
wget https://raw.githubusercontent.com/IlyaSemenov/wikipedia-word-frequency/master/results/enwiki-20190320-words-frequency.txt
git clone https://github.com/PrincetonML/SIF
    
# Gender word lists
git clone https://github.com/uclanlp/gn_glove
git clone https://github.com/uclanlp/corefBias
wget https://www.cs.cmu.edu/Groups/AI/areas/nlp/corpora/names/female.txt
wget https://www.cs.cmu.edu/Groups/AI/areas/nlp/corpora/names/male.txt

# Glove
if [ ! -f /content/gensim_glove.840B.300d.txt.bin ]; then gdown https://drive.google.com/uc?id=1Ty2exMyi-XOufY-v81RJfiPvnintHuy2; fi

# Word2Vec
if test -e /content/GoogleNews-vectors-negative300.bin.gz || test -e /content/GoogleNews-vectors-negative300.bin; then echo 'file already downloaded'; else echo 'starting download'; gdown https://drive.google.com/uc?id=0B7XkCwpI5KDYNlNUTTlSS21pQmM; fi
if [ ! -f /content/GoogleNews-vectors-negative300.bin ]; then gunzip GoogleNews-vectors-negative300.bin.gz; fi

# Fasttext
if [ ! -f /content/fasttext.bin ]; then gdown https://drive.google.com/uc?id=1Zl6a75Ybf8do9uupmrJWKQMnvqqme4fh; fi

# ELMo
if [ ! -f /content/elmo_embeddings_emma_brown.pkl ]; then gdown https://drive.google.com/uc?id=17TK2h3cz7amgm2mCY4QCYy1yh23ZFWDU; fi

# BERT
