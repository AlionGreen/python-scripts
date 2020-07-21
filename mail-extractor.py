#!/bin/python
from bs4 import BeautifulSoup
import requests
import re

url = 'http://sneakycorp.htb/team.php'

content = requests.get(url)

soup = BeautifulSoup(content.text,'html.parser')

tds = soup.find_all('td')

 
for td in tds:
    x = re.findall("[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+",str(td))
    if x:
        print x[0]
