import pandas as pd









def getWholeTrainingData():

    inputFileName = '..\\data\\train.txt'
    data = pd.read_csv(inputFileName,  delimiter="|", skipinitialspace=True)

    return data

def getShortTrainingData():

    inputFileName = '..\\data\\trainShort.txt'
    data = pd.read_csv(inputFileName,  delimiter="|", skipinitialspace=True)

    return data
