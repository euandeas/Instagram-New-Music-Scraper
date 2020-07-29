from sklearn.model_selection import train_test_split
from sklearn import naive_bayes as NB
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import pickle
import DataProcessor

class GNBModel():
    
    tfidfconverter = DataProcessor.TFIDFConverter()
    clf = NB.GaussianNB()
        
    def TrainModel(self, data, processeddata):
        
        tfidfData = self.tfidfconverter.Fit_Transform(processeddata)
        X_train, X_test, y_train, y_test, raw_train, raw_test = train_test_split(tfidfData, [i[4] for i in data], data, test_size=0.35, random_state=0)

        self.clf.fit(X_train, y_train)

        y_pred = self.clf.predict(X_test)

        print(classification_report(y_test,y_pred))
        print("Accuracy:", accuracy_score(y_test, y_pred))

    def Predict(self, newdata):
        processed = []
        processed.append(DataProcessor.Process(newdata[1]))
        tfdata = self.tfidfconverter.Transform(processed)
        pred = self.clf.predict(tfdata)
        print(newdata, " ", pred)
        print(" ")

    def SaveModel(self):
        pickle.dump(self.clf, open("finalizedGNB_model.p", 'wb'))

    def ReadModel(self):
        self.clf = pickle.load(open("finalizedGNB_model.p", 'rb'))

class MNBModel():
    
    tfidfconverter = DataProcessor.TFIDFConverter()
    clf = NB.MultinomialNB()
        
    def TrainModel(self, data, processeddata):
        
        tfidfData = self.tfidfconverter.Fit_Transform(processeddata)
        X_train, X_test, y_train, y_test, raw_train, raw_test = train_test_split(tfidfData, [i[4] for i in data], data, test_size=0.35, random_state=0)

        self.clf.fit(X_train, y_train)

        y_pred = self.clf.predict(X_test)

        print(classification_report(y_test,y_pred))
        print("Accuracy:", accuracy_score(y_test, y_pred))

    def Predict(self, newdata):
        processed = []
        processed.append(DataProcessor.Process(newdata[1]))
        tfdata = self.tfidfconverter.Transform(processed)
        pred = self.clf.predict(tfdata)
        print(newdata, " ", pred)
        print(" ")

    def SaveModel(self):
        pickle.dump(self.clf, open("finalizedMNB_model.p", 'wb'))

    def ReadModel(self):
        self.clf = pickle.load(open("finalizedMNB_model.p", 'rb'))

class CoNBModel():
    
    tfidfconverter = DataProcessor.TFIDFConverter()
    clf = NB.ComplementNB()
        
    def TrainModel(self, data, processeddata):
        
        tfidfData = self.tfidfconverter.Fit_Transform(processeddata)
        X_train, X_test, y_train, y_test, raw_train, raw_test = train_test_split(tfidfData, [i[4] for i in data], data, test_size=0.35, random_state=0)

        self.clf.fit(X_train, y_train)

        y_pred = self.clf.predict(X_test)

        print(classification_report(y_test,y_pred))
        print("Accuracy:", accuracy_score(y_test, y_pred))

    def Predict(self, newdata):
        processed = []
        processed.append(DataProcessor.Process(newdata[1]))
        tfdata = self.tfidfconverter.Transform(processed)
        pred = self.clf.predict(tfdata)
        print(newdata, " ", pred)
        print(" ")

    def SaveModel(self):
        pickle.dump(self.clf, open("finalizedCoNB_model.p", 'wb'))

    def ReadModel(self):
        self.clf = pickle.load(open("finalizedCoNB_model.p", 'rb'))

class BNBModel():
    
    tfidfconverter = DataProcessor.TFIDFConverter()
    clf = NB.BernoulliNB()
        
    def TrainModel(self, data, processeddata):
        
        tfidfData = self.tfidfconverter.Fit_Transform(processeddata)
        X_train, X_test, y_train, y_test, raw_train, raw_test = train_test_split(tfidfData, [i[4] for i in data], data, test_size=0.35, random_state=0)

        self.clf.fit(X_train, y_train)

        y_pred = self.clf.predict(X_test)

        print(classification_report(y_test,y_pred))
        print("Accuracy:", accuracy_score(y_test, y_pred))

    def Predict(self, newdata):
        processed = []
        processed.append(DataProcessor.Process(newdata[1]))
        tfdata = self.tfidfconverter.Transform(processed)
        pred = self.clf.predict(tfdata)
        print(newdata, " ", pred)
        print(" ")

    def SaveModel(self):
        pickle.dump(self.clf, open("finalizedBNB_model.p", 'wb'))

    def ReadModel(self):
        self.clf = pickle.load(open("finalizedBNB_model.p", 'rb'))

class CaNBModel():
    
    tfidfconverter = DataProcessor.TFIDFConverter()
    clf = NB.BernoulliNB()
        
    def TrainModel(self, data, processeddata):
        
        tfidfData = self.tfidfconverter.Fit_Transform(processeddata)
        X_train, X_test, y_train, y_test, raw_train, raw_test = train_test_split(tfidfData, [i[4] for i in data], data, test_size=0.35, random_state=0)

        self.clf.fit(X_train, y_train)

        y_pred = self.clf.predict(X_test)

        print(classification_report(y_test,y_pred))
        print("Accuracy:", accuracy_score(y_test, y_pred))

    def Predict(self, newdata):
        processed = []
        processed.append(DataProcessor.Process(newdata[1]))
        tfdata = self.tfidfconverter.Transform(processed)
        pred = self.clf.predict(tfdata)
        print(newdata, " ", pred)
        print(" ")

    def SaveModel(self):
        pickle.dump(self.clf, open("finalizedCaNB_model.p", 'wb'))

    def ReadModel(self):
        self.clf = pickle.load(open("finalizedCaNB_model.p", 'rb'))