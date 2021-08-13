import re

query = input('Insert Query: ')
word_query = query.split(" ")

teks = "this is the text in pattern search"

for word in word_query:
    pola = re.compile("(?=(" + "|".join(map(re.escape, word_query)) + "))")
    hasil = re.search(pola, teks)
    if hasil:
        print('Find')
