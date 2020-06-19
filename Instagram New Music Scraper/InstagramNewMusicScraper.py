from InstagramScraper import InstagramScraper
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn import svm
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
    file = open("TestData.txt", "w")
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
        print(x)
        x.append(input())
    print("CLASSIFICATION COMPLETE")
    show = input("Show resulting data? y/n:")
    if show == "y":
        for y in data:
            print(y)
    return data

def TFIDFConverter(data):
    def dummy_fun(doc):
        return doc

    tfidfconverter = TfidfVectorizer(analyzer='word',tokenizer=dummy_fun,preprocessor=dummy_fun,token_pattern=None)
    return tfidfconverter.fit_transform(data).toarray()


scraper = InstagramScraper()
data = scraper.scrapedataslow(200)
del scraper

data = ManualClassify(data)

SaveTestData(data)

#processeddata = []

#for x in data:
#    processeddata.append(ProcessData(x[1]))

#tfidfData = TFIDFConverter(processeddata)

#X_train, X_test, y_train, y_test, raw_train, raw_test = train_test_split(tfidfData, [i[3] for i in data], data, test_size=0.5, random_state=0)

#clf = svm.SVC()
#clf.fit(X_train, y_train)

#y_pred = classifier.predict(X_test)

#print(y_pred)
#input()


