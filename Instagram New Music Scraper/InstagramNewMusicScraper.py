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
    file = open("TestData2.json", "w")
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
newdata = scraper.scrapedataslow(250, True)
del scraper

newdata2 = ManualClassify(newdata)

SaveTestData(newdata2)

# works for single sample testing
#for n in newdata:
#    procinput = []
#    procinput.append(ProcessData(n[1]))
#    if procinput != []:
#        tfdata = svmmodel.tfidfconverter.transform(procinput).toarray()
#        new_pred = svmmodel.clf.predict(tfdata)
#        print(n, " ", new_pred)
#        print(" ")
#    else:
#        print(x, " misc")
#        print(" ")

#input()
#testing = []
#for x in newdata:
#    testing.append(ProcessData(x[1]))
    
#tfdata = svmmodel.tfidfconverter.transform(testing).toarray()
#new_pred = svmmodel.clf.predict(tfdata)

#for n in range(5):
#    print(newdata[n], " ", new_pred[n])
#    print(" ")
