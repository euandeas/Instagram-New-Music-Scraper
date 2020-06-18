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
    stopwordsremoved = [w for w in symbolsremoved if not w in set(stopwords.words('english'))]
  
    return stopwordsremoved

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


input()


