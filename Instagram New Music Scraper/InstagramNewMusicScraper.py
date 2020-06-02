from InstagramScraper import InstagramScraper
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

def preparedata(sentence):
    tokens= word_tokenize(sentence)
    tokens = [w.lower() for w in tokens]

    symbolsremoved = [word for word in tokens if word.isalpha()]
    
    stop_words = set(stopwords.words('english'))
    return [w for w in symbolsremoved if not w in stop_words]

scraper = InstagramScraper()
data = scraper.scrapedata(100)
del scraper

cleandata = []

for x in data:
    cleandata.append(preparedata(x[1]))

print(cleaneddata)
input()


