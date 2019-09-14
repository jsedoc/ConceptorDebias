# Testing bias using Word Embedding Association Test (WEAT) - Conceptor debiasing

The [WEAT](https://arxiv.org/abs/1608.07187) algorithm is used to quantify bias in word embeddings by studying statistical parameters like effect size and one-sided p-value for a test statistic computing associations between different sets of words.

The WEAT algorithm to calculate the effect size and p-values has been implemented in WEAT.ipynb. 

To reproduce the results from the [paper](https://arxiv.org/abs/1906.05993), run each cell in the notebook carefully following the instructions. The code can be found in the notebook named 'WEAT(Final).ipynb' in this repository.

- The notebook loads word embeddings, computes the conceptor, applies the negated conceptor to the word embeddings and computes WEAT scores for the chosen word list pairs.
- The notebook has a step by step description which will help running the code. 
- The notebook also has code to load different pre-trained word embeddings (Glove, Word2vec, Fasttext, ELMo, BERT), apply conceptor negation to debias the embeddings and test the debiased embeddings on WEAT.
- You can change the wordlists you want to test on by updating the approriate cell in the notebook which initializes the variables.

Note: The notebook has a separate section which runs the BERT embeddings on WEAT.

Hard debiasing algorithms as proposed by [Mu et. al.](https://arxiv.org/abs/1702.01417) and [Bolukbasi et. al.](https://papers.nips.cc/paper/6228-man-is-to-computer-programmer-as-woman-is-to-homemaker-debiasing-word-embeddings.pdf) are also implemented for testing.

