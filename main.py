from googlesearch import search
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import nltk
import re

query = input('Insert Query: ')
word_query = query.split(" ")
i = 1
print("-" * 150)

for site in search(query, tld="com", lang='id', num=10, stop=10, pause=2.0):
    # Open Site
    req = Request(site, headers={'User-Agent': 'XYZ/3.0'})
    page = urlopen(req, timeout=20)
    html_bytes = page.read().decode("utf-8", errors="ignore")

    # Pre-Processing
    Raw = BeautifulSoup(html_bytes, "html.parser")
    paragraphs = []
    Text = ""

    print("SITE " + str(i) + ":")
    for String in Raw.stripped_strings:
        paragraphs.append(str(String))

    for paragraph in paragraphs:
        # Segmentation Text
        sentences = nltk.sent_tokenize(paragraph)
        for sentence in sentences:
            # Cleaning Text
            sentence = re.sub(r"[^\w\s]", "", sentence)
            # Filtering Text
            pattern = re.compile(r'\b(?:%s)\b' % "|".join(word_query))
            hasil = re.search(pattern, sentence)
            if hasil:
                    Text += ("- " + sentence.strip() + "\n")
    print(Text)
    i+=1
    print("-" * 50)