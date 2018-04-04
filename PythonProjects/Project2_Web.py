'''import webbrowser

periodicElement = input("Enter the periodic element to know its details\n")

webbrowser.open('https://en.wikipedia.org/wiki/'+periodicElement)
'''
'''from pyquery import PyQuery as pq
import requests

periodicElement = input("Enter the periodic element to know its details\n")

url = 'https://en.wikipedia.org/wiki/'+periodicElement
content = requests.get(url).content
doc = pq(content)

respondent = doc("p").text()

print(respondent)'''

'''import requests
URL = 'https://www.instituteforsupplymanagement.org/about/MediaRoom/newsreleasedetail.cfm?ItemNumber=30655&SSO=1'
r = requests.get(URL)
page = r.text
from bs4 import BeautifulSoup
soup = BeautifulSoup(page, 'lxml')
import re
paras = soup.find_all('p', string=re.compile('(?:growth)|(?:contraction).*? are\:'))
saying = soup.find_all('strong', string=re.compile('WHAT RESPONDENTS ARE SAYING'))[0]
for i, para in enumerate(paras):
     'Paragraph ', i
     para'''

from bs4 import BeautifulSoup

from pyquery import PyQuery as pq
import requests

periodicElement = input("Enter the periodic element to know its details\n")

url = 'https://en.wikipedia.org/wiki/'+periodicElement
content = requests.get(url).content

soup = BeautifulSoup(content)
for strong_tag in soup.find_all('p'):
    print (strong_tag.text, strong_tag.next_sibling)
    break

# -------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------
# Issues: 
# What do lines 1 - 31 do?
# Code does not work at all
# No functions have been made
# Same issues as Project 1
# Please adhere to guidelines; Refer Project1_weather.py's comments for more information

# -------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------
