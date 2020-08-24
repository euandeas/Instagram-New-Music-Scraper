from InstagramScraper import InstagramScraper
from sklearn import svm
from sklearn import naive_bayes as NB
from DataProcessor import *
from StandardClassifierModel import *

processeddata = []

data = ReadData(False)

for x in data:
    processeddata.append(Process(x[1]))

svmmodel = SCModel(svm.LinearSVC())
svmmodel.TrainModel(data, processeddata)

#mnbmodel = SCModel(NB.MultinomialNB())
#mnbmodel.TrainModel(data, processeddata)


scraper = InstagramScraper()
newdata = scraper.scrapedata(10, False)
del scraper

for x in newdata:
    svmmodel.Predict(x)
    #mnbmodel.Predict(x)

