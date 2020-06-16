from InstagramScraper import InstagramScraper
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import nltk
import json
import random

def ProcessData(sentence):
    tokens= word_tokenize(sentence)
    tokens = [w.lower() for w in tokens]

    symbolsremoved = [word for word in tokens if word.isalpha()]
    
    stop_words = set(stopwords.words('english'))
    return [w for w in symbolsremoved if not w in stop_words]

def SaveTestData(data):
    file = open("TestData.txt", w)
    json.dump(data, file)
    file.close()

def ReadData(random):
    file = open("TestData.txt")
    data = json.load(file)
    if random == True:
        return random.shuffle(data)
    else:
        return data

def ManualClassify(data):
    for x in data:
        x.append(input())
    print("CLASSIFICATION COMPLETE")
    show = input("Show resulting data? y/n:")
    if show == "y":
        for y in data:
            print(y)
    return data

def FindFeatures():
    return

scraper = InstagramScraper()
data = scraper.scrapedataslow(30)
del scraper

processeddata = []

for x in data:
    processeddata.append(ProcessData(x[1]))

all_words = []
for s in processeddata:
    for w in s:
        all_words.append(w)

for a in data:
    print(a)
print(all_words)

all_words = nltk.FreqDist(all_words)
print(all_words.most_common(10))
input()


