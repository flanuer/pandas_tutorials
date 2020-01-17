'''
Author Scott Phillpott
Try to scrape Cybersecurity Ventures top 500 companies, add them to a stock tracking list
5/13/2017

#!/usr/bin/python3

This works!
import urllib.request
wp = urllib.request.urlopen('http://cybersecurityventures.com/cybersecurity-500-list/#home/?view_1_per_page=500&view_1_page=1&view_1_sort=field_2|desc')
pw = wp.read()
print(pw)


import requests
from bs4 import BeautifulSoup
wp=requests.get('http://cybersecurityventures.com/cybersecurity-500-list/#home/?view_1_per_page=500&view_1_page=1&view_1_sort=field_2|desc')
pw = wp.read()

print(pw)
'''

import urllib.request
wp = urllib.request.urlopen('http://cybersecurityventures.com/cybersecurity-500-list/#home/?view_1_per_page=500&view_1_page=1&view_1_sort=field_2|desc')
pw = wp.read()
print(pw)
