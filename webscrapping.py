# In web scrapping we fetch frontend part of website
# link for response code types https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
import time
import sys
from bs4 import BeautifulSoup
import requests
try:
    page  = requests.get('https://www.who.int/health-topics/air-pollution#tab=tab_1')
    #print(page)
except Exception as e:
    print(e)

soup = BeautifulSoup(page.text, 'html.parser')
links = soup.find_all('div', attrs={'class': 'arrowed-link'})
#print(soup)
print(links)