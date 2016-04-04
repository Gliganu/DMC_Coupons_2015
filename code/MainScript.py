import FileManager
import Visualizer
import DatasetManipulator
import ClassifierTrainer
import Validator


def performJob():


    # construct Train & Test Data
    xTrain, yTrain, xTest, yTest = DatasetManipulator.getTrainAndTestData()

    # training the classifier
    classifier = ClassifierTrainer.trainClassifier(xTrain, yTrain)

    #predicting
    yPred = classifier.predict(xTest)

    #assessing the performance
    Validator.performValidation(yPred, yTest)







if __name__ == '__main__':


    performJob()




