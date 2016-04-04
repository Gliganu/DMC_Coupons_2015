from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.svm import SVC

from code import FileManager
from code.DatasetManipulator import getFeatureEngineeredData


def trainLinearRegression(xTrain, yTrain):
    classifier = LinearRegression(n_jobs=-1)

    classifier.fit(xTrain, yTrain)


    return classifier

def trainLogisticRegression(xTrain, yTrain):
    classifier = LogisticRegression(n_jobs=-1, verbose=1, penalty='f1_score')

    classifier.fit(xTrain, yTrain)


    return classifier

def trainRandomForestClassifier(xTrain, yTrain):


    # classifier = RandomForestClassifier(n_estimators=90,max_features=0.8, max_depth=9, n_jobs=-1,class_weight='balanced')

    classifier = SVC()

    classifier.fit(xTrain, yTrain)

    data = FileManager.getWholeTrainingData()

    predictionColumnId = None

    data = getFeatureEngineeredData(data,predictionColumnId)


    # importances =  zip(data.columns,classifier.feature_importances_)

    print len(data.columns)
    # print len(classifier.feature_importances_)
    # print sorted(impo rtances, key=lambda (x,y): -y)

    return classifier

def trainClassifier(xTrain,yTrain):

    print "Training classifier..."


    #classifier = trainLinearRegression(xTrain,yTrain)

    # classifier = trainLogisticRegression(xTrain,yTrain)
    #
    classifier = trainRandomForestClassifier(xTrain,yTrain)




    return classifier