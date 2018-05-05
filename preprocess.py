import numpy as np
import pandas as pd

class Pre_Process(object):
    '''
    Load available data to DataFrame
    Training Data
    '''
    def __init__(self):
        '''
        Set directory of train data
        and load data, split Data to X_Y
        '''
        self.Path_Train = './Data/train.data'

        #Set name of columns
        self.org_columns = ['S1','C1','S2','C2','S3','C3','S4','C4','S5','C5','Type']
        self.train = self.readData()

        #Split data to x and y
        self.x_train, self.y_train = self.split_in_out(self.train)

    def getData(self):
        '''
        Get DataFrame Train Data
        '''
        return self.train

    def readData(self):
        '''
        Read and return Data Frame Data
        '''
        train = pd.read_csv(self.Path_Train, names = self.org_columns)
        return train
    
    def split_in_out(self, data):
        '''
        Split X, Y data
        '''
        x = data[self.org_columns[:-1]]
        y = data.Type
        return x, y
    