import urllib.request
from bs4 import BeautifulSoup

word = input('Enter the word to find the meaning : ')

url = "https://www.vocabulary.com/dictionary/" + word + ""
htmlfile = urllib.request.urlopen(url)
soup = BeautifulSoup(htmlfile, 'lxml')

soup1 = soup.find(class_="short")

try:
    soup1 = soup1.get_text()
except AttributeError:
    print('Cannot find such word! Check spelling.')
    exit()

# Print short meaning
print ('-' * 25 + '->',word,"<-" + "-" * 25)
print ("SHORT MEANING: \n\n",soup1)
print ('-' * 65)