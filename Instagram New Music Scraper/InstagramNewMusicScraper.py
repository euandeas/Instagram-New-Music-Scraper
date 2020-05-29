from InstagramScraper import InstagramScraper
from nltk.tokenize import word_tokenize

scraper = InstagramScraper()
data = scraper.scrapedata(1)
del scraper

tokenizeddata = []

for x in data:
    tokenizeddata.append(word_tokenize(x[1]))

for y in tokenizeddata:
    print(y)

input()