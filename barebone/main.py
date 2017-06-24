# =============== Bare bone scripts, that result in the app ================

from textblob import TextBlob
from bs4 import BeautifulSoup
import requests
import json
import image
# ============== getting the sentiment out of a normal text ================
# text = raw_input("Enter the input you want processed::")

# blob = TextBlob(text)

# print blob.tags

# print blob.sentiment

# polarity = blob.sentiment.polarity
# print polarity

# ================ scraping the images from wallheaven random page ================

# random images url
url = "https://alpha.wallhaven.cc/random?page=1"

# getting the document behind the url | requests
response = requests.get(url)

# code from content
text = response.text

# beautifying the code
soup = BeautifulSoup(text, 'html.parser')

# getting out the images' thumbnails for evaluation
# for link in soup.find_all('img'):
# 	# source for all the thumbnails
# 	src = link.get('data-src')

# we are getting late, so I'll pick the 
# the first image of the page
for link in soup.find_all('a', {"class":"preview"}, limit=1):
	src = link.get('href')
	print src

# ================ evaluating the images on wallhaven ============================



# ================ setting up text on the image ==================================

# as of now we have only one image coming through.
# lets overlay text on the image
image(src)