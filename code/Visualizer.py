import FileManager
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

import seaborn as sns



def plotCouponUsage():

    data = FileManager.getWholeTrainingData()

    data = data[['coupon1Used','coupon2Used','coupon3Used']]


    data.hist()

    plt.show()



def plotTime():

    data = FileManager.getWholeTrainingData()

    df = pd.DataFrame()

    # df['month']= data['orderTime'].map(lambda entryDate: float(entryDate.split(" ")[0].split("-")[1]))
    # df['day'] = data['orderTime'].map(lambda entryDate: float(entryDate.split(" ")[0].split("-")[2]))
    # df['hour'] = data['orderTime'].map(lambda entryDate: float(entryDate.split(" ")[1].split(":")[0]))

    # df['couponMonth'] = data['couponsReceived'].map(lambda entryDate: float(entryDate.split(" ")[0].split("-")[1]))
    # df['couponDay'] = data['couponsReceived'].map(lambda entryDate: float(entryDate.split(" ")[0].split("-")[2]))
    df['couponHour'] = data['couponsReceived'].map(lambda entryDate: float(entryDate.split(" ")[1].split(":")[0]))

    df.hist()

    plt.show()


def makeStacked():
    data = FileManager.getWholeTrainingData()

    data = data[['brand1','coupon1Used']]

    data =  data[data["coupon1Used"] == 1 ]

    data = data['brand1']

    data.hist()

    plt.show()
    print data

