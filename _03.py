import requests
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'https://www.thesaurus.com/'

# Step 1 : Get the HTML
r = requests.get(url)
htmlcontent = r.content
#print(htmlcontent)

# Step 2 : Parser the Html
soup = BeautifulSoup(htmlcontent, 'html.parser')
#print(soup.prettify())

# Step 3 : HTML Tree transversal
# Commonly used object types
# 1. Tag
# 2. NavigableString
# 3. BeautifulSoup
# 4. Comment
title = soup.title
print(type(title.string))
