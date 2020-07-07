from InstagramScraper import InstagramScraper
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
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


def dummy_fun(doc):
    return doc

processeddata = []

data = ReadData(False)

for x in data:
    processeddata.append(ProcessData(x[1]))

tfidfconverter = TfidfVectorizer(analyzer='word',tokenizer=dummy_fun,preprocessor=dummy_fun,token_pattern=None)
tfidfData = tfidfconverter.fit_transform(processeddata).toarray()

X_train, X_test, y_train, y_test, raw_train, raw_test = train_test_split(tfidfData, [i[4] for i in data], data, test_size=0.35, random_state=0)

clf = svm.LinearSVC()
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)

print(classification_report(y_test,y_pred))
print(accuracy_score(y_test, y_pred))

#for x in range(100):
    #print(X_test[x], " ", raw_test[x], " ",y_pred[x])
    #print("/n")

scraper = InstagramScraper()
data = scraper.scrapedataslow(10)
del scraper

for x in data:
    procinput = ProcessData(x[1])
    tfidfData1 = tfidfconverter.transform(procinput)
    new_pred = clf.predict(tfidfData1)
    print(x, " ", new_pred)
    print(" ")
input()


