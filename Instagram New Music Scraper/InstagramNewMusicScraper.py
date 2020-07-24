from InstagramScraper import InstagramScraper
from SVMClassifier import SVMModel
import json
import random
import numpy

def SaveTestData(data):
    file = open("TestData2.json", "w")
    json.dump(data, file, indent=2)
    file.close()

def ReadData(random):
    file = open("TestData1.json", "r")
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
#svmmodel.TrainModel(data, processeddata)
#svmmodel.SaveModel()

svmmodel.ReadModel()

scraper = InstagramScraper()
newdata = scraper.scrapedataslow(10, False)
del scraper

for x in newdata:
    svmmodel.Predict(x)
