from InstagramScraper import InstagramScraper
from SVMClassifier import SVMModel
from DataProcessor import *

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
