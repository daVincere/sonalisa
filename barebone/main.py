# =============== Bare bone scripts, that result in the app ================

from textblob import TextBlob
from bs4 import BeautifulSoup

# ============== getting the sentiment out of a normal text ================
text = raw_input("Enter the input you want processed::")

blob = TextBlob(text)

print blob.tags

print blob.sentiment

polarity = blob.sentiment.polarity
print polarity

# ================ scraping the images from wallheaven random page ================

# random images url
url = "https://alpha.wallhaven.cc/random?page=1"