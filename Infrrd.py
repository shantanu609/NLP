from bs4 import BeautifulSoup
import requests
import spacy
import re
import numpy as np
def url_to_string(content):
    html = content
    soup = BeautifulSoup(html, 'lxml')
    for script in soup(["script", "style", 'asida']):
        script.extract()
    return " ".join(re.split(r'[\n\t]+', soup.get_text()))

text = open("test.txt", "r").read()
ny = url_to_string(text)
nlp = spacy.load('en')
article = nlp(ny)
newlabels = [(x,x.label,x.label_) for x in article.ents]
print(newlabels)
