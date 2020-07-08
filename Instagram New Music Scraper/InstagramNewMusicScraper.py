from InstagramScraper import InstagramScraper
from SVMClassifier import SVMModel
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import nltk
import json
import random
import numpy

def ProcessData(sentence):
    tokens= word_tokenize(sentence)
    tokens = [w.lower() for w in tokens]

    symbolsremoved = [word for word in tokens if word.isalpha()]
    stopwordsremoved = [w for w in symbolsremoved if not w in set(stopwords.words('english'))]
  
    return stopwordsremoved

def SaveTestData(data):
    file = open("TestData.json", "w")
    json.dump(data, file, indent=2)
    file.close()

def ReadData(random):
    file = open("TestData.json", "r")
    data = json.load(file)
    file.close()
    if random == True:
        return random.shuffle(data)
    else:
        return data

def ManualClassify(data):
    for x in data:
        print(x)
        x.append(input())
    print("CLASSIFICATION COMPLETE")
    show = input("Show resulting data? y/n:")
    if show == "y":
        for y in data:
            print(y)
    return data


processeddata = []

data = ReadData(False)

for x in data:
    processeddata.append(ProcessData(x[1]))

svmmodel = SVMModel()
svmmodel.trainmodel(data, processeddata)


scraper = InstagramScraper()
data = scraper.scrapedataslow(10, False)
del scraper

for x in data:
    procinput = ProcessData(x[1])
    if procinput != []:
        tfdata = svmmodel.tfidfconverter.transform(procinput)
        new_pred = svmmodel.clf.predict([tfdata].reshape(-1, 1))
        print(x, " ", new_pred)
        print(" ")
    else:
        print(x, " misc")
        print(" ")
input()


