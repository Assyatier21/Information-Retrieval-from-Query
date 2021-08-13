import re

query = input('Insert Query: ')
word_query = query.split(" ")

teks = "gua apa ya gataulah pokoknya gitu bisa ga ya adalah gini aja dah"

for word in word_query:
    # pola = re.compile("(?=(" + "|".join(map(re.escape, word_query)) + "))")
    pola = re.compile(word)
    hasil = re.search(pola, teks)
    if hasil:
        print('Find')