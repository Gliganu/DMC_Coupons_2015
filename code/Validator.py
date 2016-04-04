from sklearn import metrics
import numpy as np
from sklearn.metrics import accuracy_score,recall_score,precision_score,f1_score



def performValidation(yPred, yTest):
    #print(metrics.mean_squared_error(yPred, yTest))
    print metrics.classification_report(yPred, yTest)