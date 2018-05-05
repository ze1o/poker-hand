import numpy as np
import pandas as pd

class Pre_Process(object):
    def __init__(self):
        self.Path_Train = './Data/train.data'
        self.Path_Test = './Data/test.data'

        self.org_columns = ['S1','C1','S2','C2','S3','C3','S4','C4','S5','C5','Type']
        self.train, self.test = self.readData()

        self.x_train, self.y_train = self.split_in_out(self.train)
        self.x_test, self.y_test = self.split_in_out(self.test)

    def getTrain(self):
        return self.train

    def getTest(self):
        return self.test

    def getXY_Train(self):
        return self.x_train, self.y_train

    def getXY_Test(self):
        return self.x_test, self.y_test

    def readData(self):
        train = pd.read_csv(self.Path_Train, names = self.org_columns)
        test = pd.read_csv(self.Path_Test, names = self.org_columns)
        return train, test
    
    def split_in_out(self, data):
        x = data[self.org_columns[:-1]]
        y = data.Type
        return x, y
    