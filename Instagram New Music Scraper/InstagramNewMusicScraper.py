from InstagramScraper import InstagramScraper
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import json

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

def ReadData():
    file = open("TestData.txt")
    data = json.load(file)
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

scraper = InstagramScraper()
data = scraper.scrapedata(100)
del scraper

processeddata = []

for x in data:
    processeddata.append(processedata(x[1]))

print(cleaneddata)
input()


