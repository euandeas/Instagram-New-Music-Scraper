from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import pickle
import DataProcessor

class SVMModel():
    
    def dummy_fun(doc):
        return doc

    tfidfconverter = DataProcessor.TFIDFConverter
    clf = svm.LinearSVC()
        
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
        pickle.dump(self.clf, open("finalizedSVM_model.p", 'wb'))

    def ReadModel(self):
        self.clf = pickle.load(open("finalizedSVM_model.p", 'rb'))




