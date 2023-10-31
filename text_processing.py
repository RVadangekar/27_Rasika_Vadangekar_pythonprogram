import nltk
from nltk.stem import *
wd_stem=PorterStemmer()
print(wd_stem.stem('eating'))
