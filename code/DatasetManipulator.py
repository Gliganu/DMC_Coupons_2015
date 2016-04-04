import pandas as pd
import numpy as np
import FileManager
from sklearn.cross_validation import train_test_split




def performDateEnginnering(rawData, dateColumn,prefix):

    rawData[prefix+'-month']= rawData[dateColumn].map(lambda entryDate: float(entryDate.split(" ")[0].split("-")[1]))
    rawData[prefix+'-day'] = rawData[dateColumn].map(lambda entryDate: float(entryDate.split(" ")[0].split("-")[2]))

    return rawData


def performDayEnginnering(rawData, dayColumn,prefix):

     rawData.loc[:,prefix+'-hour'] = rawData[dayColumn].map(lambda entryDate: float(entryDate.split(" ")[1].split(":")[0]))

     return rawData


def getFeatureEngineeredData(data,predictionColumnId = None):

    # orderID|orderTime|userID|couponsReceived|
    # couponID1|price1|basePrice1|reward1|premiumProduct1|brand1|productGroup1|categoryIDs1|
    # couponID2|price2|basePrice2|reward2|premiumProduct2|brand2|productGroup2|categoryIDs2|
    # couponID3|price3|basePrice3|reward3|premiumProduct3|brand3|productGroup3|categoryIDs3|
    # coupon1Used|coupon2Used|coupon3Used|basketValue

    keptColumns = ['orderTime', 'couponsReceived', 'price1', 'basePrice1', 'reward1', 'premiumProduct1', 'price2',
                   'basePrice2', 'reward2', 'premiumProduct2', 'price3', 'basePrice3', 'reward3', 'premiumProduct3'
                   ]

    if predictionColumnId:
        keptColumns.append(predictionColumnId)


    print "Kept columns {}".format(keptColumns)

    data = data[keptColumns]

    data = performDateEnginnering(data,'orderTime','purchase')
    data = performDayEnginnering(data,'orderTime','purchase')

    data = performDateEnginnering(data,'couponsReceived','coupon')
    data = performDayEnginnering(data,'couponsReceived','coupon')

    data =  data.drop(['orderTime','couponsReceived'],1)

    return data


def getTrainAndTestData():

    data = FileManager.getWholeTrainingData()

    predictionColumnId = 'coupon3Used'

    data = getFeatureEngineeredData(data,predictionColumnId)

    trainData, testData = train_test_split(data, test_size=0.25)

    xTrain = trainData.ix[:, trainData.columns != predictionColumnId].values
    yTrain = trainData[predictionColumnId].values

    xTest = testData.ix[:, testData.columns != predictionColumnId].values
    yTest = testData[predictionColumnId].values


    return xTrain,yTrain,xTest,yTest





















