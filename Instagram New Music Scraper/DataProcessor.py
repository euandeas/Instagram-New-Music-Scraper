from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
import json
import random

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

def Process(sentence):
    tokens= word_tokenize(sentence)
    tokens = [w.lower() for w in tokens]

    symbolsremoved = [word for word in tokens if word.isalpha()]
    stopwordsremoved = [w for w in symbolsremoved if not w in set(stopwords.words('english'))]
  
    return stopwordsremoved

class TFIDFConverter():

    tfidfconverter = TfidfVectorizer(analyzer='word',tokenizer=dummy_fun,preprocessor=dummy_fun,token_pattern=None)

    def Fit_Transform(self, data):
        return self.tfidfconverter.fit_transform(data).toarray()
    
    def Transform(self):
        return self.tfidfconverter.transform(processed).toarray()

    def SaveVectorizer(self):
        pickle.dump(self.tfidfconverter, open("tfidfvectorizer.p", 'wb'))

    def ReadVectorizer(self):
        self.tfidfconverter = pickle.load(open("tfidfvectorizer.p", 'rb'))