'''
import requests
from bs4 import BeautifulSoup

url = "http://cybersecurityventures.com/cybersecurity-500-list/#home/?view_1_per_page=500&view_1_page=1&view_1_sort=field_2|desc"
html = requests.get(url).content

soup = BeautifulSoup(html)

print(soup)
'''



import pandas as pd
url = "http://cybersecurityventures.com/cybersecurity-500-list/#home/?view_1_per_page=500&view_1_page=1&view_1_sort=field_2|desc"

companies = pd.read_html(url)[0]

print companies
