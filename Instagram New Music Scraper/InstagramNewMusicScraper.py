from InstagramScraper import InstagramScraper
from SVMClassifier import SVMModel
from NaiveBayesClassifiers import *
from DataProcessor import *

processeddata = []

data = ReadData(False)

for x in data:
    processeddata.append(Process(x[1]))

svmmodel = SVMModel()
svmmodel.TrainModel(data, processeddata)

gnbmodel = GNBModel()
gnbmodel.TrainModel(data, processeddata)

mnbmodel = MNBModel()
mnbmodel.TrainModel(data, processeddata)

conbmodel = CoNBModel()
conbmodel.TrainModel(data, processeddata)

bnbmodel = BNBModel()
bnbmodel.TrainModel(data, processeddata)

canbmodel = CaNBModel()
canbmodel.TrainModel(data, processeddata)

scraper = InstagramScraper()
newdata = scraper.scrapedataslow(10, False)
del scraper

for x in newdata:
    svmmodel.Predict(x)
    gnbmodel.Predict(x)
    mnbmodel.Predict(x)
    conbmodel.Predict(x)
    bnbmodel.Predict(x)
    canbmodel.Predict(x)
