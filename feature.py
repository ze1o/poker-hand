import math
import pandas as pd
import numpy as np

class Feature_Extraction():
    def __init__(self, Data):
        self.Raw = Data
        self.Data = None

        self._RAW_DATA = ['S1','C1','S2','C2','S3','C3','S4','C4','S5','C5']
        self._COUNT_CARD = ['Count_C{}'.format(i) for i in range(1, 14)]
        self._STD_COUNT_CARD = ['Std_card']
        self._COUNT_SUIT = ['Count_S{}'.format(i) for i in range(1, 5)]
        self._BAG_COUNT_SUIT = ['Bag_Count_Suit_{}'.format(i) for i in range(0,6)]
        self._BAG_COUNT_CARD = ['Bag_Count_Card_{}'.format(i) for i in range(0,6)]
        self._ACE_FLAG = ['Ace_flag']

        self.fit()

    def fit(self):
        self.Data = self.Raw
        self.Data = self.count_card()
        self.Data = self.std_count_card()
        self.Data = self.count_suit()
        self.Data = self.bag_count_suit()
        self.Data = self.bag_count_card()
        self.DataData = self.concat_Ace_flag()

    def getNameColumns(self, list_type):
        columns = []
        for i in list_type:
            if i == 1:
                columns.extend(self._RAW_DATA)
            elif i == 2:
                columns.extend(self._COUNT_CARD)
            elif i == 3:
                columns.extend(self._STD_COUNT_CARD)
            elif i == 4:
                columns.extend(self._COUNT_SUIT)
            elif i == 5:
                columns.extend(self._BAG_COUNT_SUIT)
            elif i == 6:
                columns.extend(self._BAG_COUNT_CARD)
            elif i == 7:
                columns.extend(self._ACE_FLAG)
        return columns
    
    def getFeature(self, list_type):
        columns = self.getNameColumns(list_type)
        return self.Data[columns]

    def getFullFeature(self, list_type):
        columns = self.getNameColumns(list_type)
        columns.extend(['Type'])
        return self.Data[columns]

    def getY(self):
        return self.Data.Type

    def getRawData(self):
        return self.Raw

    def count_card(self):
        count_card = []
        for i in range(1, 14):
            each_counts = pd.concat([self.Data.C1 ==i, 
                                    self.Data.C2 == i, 
                                    self.Data.C3 ==i, 
                                    self.Data.C4 == i, 
                                    self.Data.C5 ==i], axis = 1)
            count_card.append(np.sum(each_counts, axis = 1))
        count_card = np.vstack(count_card)
        count_card_df = pd.DataFrame(count_card.transpose(), 
                                    columns = ['Count_C{}'.format(i) for i in range(1, 14)])
        return pd.concat([self.Data, count_card_df], axis = 1)

    def std_count_card(self):
        hands = self.Data[['C1','C2','C3','C4','C5']].as_matrix()
        std = np.std(hands, axis = 1)
        hands[hands == 1] = 14
        new_std = np.std(hands, axis = 1)
        std[new_std < std] = new_std[new_std < std]
        std_df = pd.DataFrame(std, columns=['Std_card'])
        return pd.concat([self.Data, std_df],axis = 1)

    def count_suit(self):
        count_suit = []
        for i in range(1, 5):
            each_count = pd.concat([self.Data.S1 == i, 
                                    self.Data.S2 == i, 
                                    self.Data.S3 == i, 
                                    self.Data.S4 == i, 
                                    self.Data.S5 == i], axis = 1)
            count_suit.append(np.sum(each_count, axis = 1))
        count_suit = np.vstack(count_suit)
        count_suit_df = pd.DataFrame(count_suit.transpose(), 
                                    columns = ['Count_S{}'.format(i) for i in range(1, 5)])
        return pd.concat([self.Data, count_suit_df], axis = 1)
    
    def bag_count_suit(self):
        bag_count_suit = []
        for i in range(0, 6):
            each_counts = pd.concat([self.Data.Count_S1 == i, 
                                    self.Data.Count_S2 == i, 
                                    self.Data.Count_S3 == i, 
                                    self.Data.Count_S3 == i], axis=1)
            bag_count_suit.append(np.sum(each_counts, axis=1))
        bag_count_suit = np.vstack(bag_count_suit)
        bag_count_suit_df = pd.DataFrame(bag_count_suit.transpose(), 
                                        columns=['Bag_Count_Suit_{}'.format(i) for i in range(0,6)])
        return pd.concat([self.Data, bag_count_suit_df], axis = 1)

    def bag_count_card(self):
        bag_count_card = []
        for i in range(0, 6):
            each_counts = pd.concat([self.Data.Count_C1 == i,
                                    self.Data.Count_C2 == i, 
                                    self.Data.Count_C3 == i, 
                                    self.Data.Count_C4 == i,
                                    self.Data.Count_C5 == i,
                                    self.Data.Count_C6 == i, 
                                    self.Data.Count_C7 == i, 
                                    self.Data.Count_C8 == i,
                                    self.Data.Count_C9 == i,
                                    self.Data.Count_C10 == i, 
                                    self.Data.Count_C11 == i, 
                                    self.Data.Count_C12 == i,
                                    self.Data.Count_C13 == i,], axis=1)
            bag_count_card.append(np.sum(each_counts, axis=1))
        bag_count_card = np.vstack(bag_count_card)
        bag_count_card_df = pd.DataFrame(bag_count_card.transpose(),
                                    columns=['Bag_Count_Card_{}'.format(i) for i in range(0,6)])
        return pd.concat([self.Data, bag_count_card_df], axis=1)

    def concat_Ace_flag(self):
        self.Data['Ace_flag']= self.Data['Count_C1']==1
        return self.Data
    