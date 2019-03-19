EEC results with WORD2VEC, GLOVE, FASTTEXT, ELMO, and BERT embeddings \

According    to    Kiritchenko    and    Mohammad(2018b),   the   Equity   Evaluation   Corpus(EEC) consists  of  8640  English  sentences  which  are carefully   generated   to   obtain   biases   towards certain  genders  and  races. EEC  is  developed using  eleven  sentence  templates,  each  of  which involves at least one race- or gender-related word, and most templates also have emotional words to express  emotion  and  sentiment.   EEC  is  used  to measure gender and racial biases on sentiments in our experiments.

1. EEC_with_CN(w2v,_GloVe,_Fasttext).ipynb includes EEC results on WORD2VEC, GLOVE and FASTTEXT before and after CN processing.\
On WORD2VEC, GLOVE, and FASTTEXT, we used racial names lists from https://gist.github.com/mbejda to calculate the corresponding conceptor. \
For sentiment embeddings, we tried single word embeddings such as 'anger', 'fear' and 'joy' itself as sentiment embeddings, as well as averaged embeddings -- using average embeddings of 5 - 10 words representing certain sentiments.
2. EEC_with_CN(ElMo,_BERT).ipynb includes EEC results on ELMO and BERT embeddings before and after CN processing. \
On ELMo and BERT, we used pre-calculated Conceptor Negation matrix directly to run our experiments.

Default aperture(alpha) for conceptor is 1. 
