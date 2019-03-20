# Testing bias using Word Embedding Association Test (WEAT) - Conceptor debiasing

The [WEAT](https://arxiv.org/abs/1608.07187) algorithm is used to quantify bias in word embeddings by studying statistical parameters like effect size and one-sided p-value for a test statistic computing associations between different sets of words.

The WEAT algorithm to calculate the effect size and p-values has been implemented in WEAT.ipynb. 

The notebook has a step by step description which will help running the code. 
The notebook also has code to load different pre-trained word embeddings (Glove, Word2vec, Fasttext, ELMo, BERT), apply conceptor negation to debias the embeddings and test the debiased embeddings on WEAT.

To reproduce the results, run each cell in the notebook carefully following the instructions. The code involves the followong major steps,
- Load all functions for WEAT and Conceptor negation.
- Load all (required) word embeddings.
- Apply conceptor negation to the embeddings and run WEAT.

Note: The notebook has a separate section which runs the BERT embeddings on WEAT.

Hard debiasing algorithms as proposed by [Mu et. al.](https://arxiv.org/abs/1702.01417) and [Bolukbasi et. al.](https://papers.nips.cc/paper/6228-man-is-to-computer-programmer-as-woman-is-to-homemaker-debiasing-word-embeddings.pdf) are also implemented for testing.

