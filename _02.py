import requests
from bs4 import BeautifulSoup

word = "angry"
url = 'https://www.thesaurus.com/browse/{}'.format(word)
r = requests.get(url)
returned_words_list = []

soup = BeautifulSoup(r.text, 'html.parser')


word_ul = soup.find("ul", {"class":'css-1lc0dpe et6tpn80'})
print(word_ul)
for idx, elem in enumerate(word_ul.findAll("a")):
    returned_words_list.append(elem.text.strip())

print (returned_words_list)