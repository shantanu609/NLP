# import spacy
# from spacy import displacy
# from pprint import pprint
# from collections import Counter
# import en_core_web_sm
# nlp = en_core_web_sm.load()
# doc = nlp('European authorities fined Google a record $5.1 billion on Wednesday for abusing its power in the mobile phone market and ordered the company to alter its practices')
# pprint([(X.text, X.label_) for X in doc.ents])

import spacy
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
nlp = spacy.load("en")
wordset = set(stopwords.words('english'))
doc = nlp("The big grey dog ate all of the chocolate, but fortunately he wasn't sick!")
a = "The big grey dog ate all of the chocolate, but fortunately he wasn't sick!"
# a = [token.orth_ for token in doc if token not in wordset]
# print(a)

wordtoken = word_tokenize(a)

b = [token for token in wordtoken]
print(b)

