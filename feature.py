import math
import pandas as pd
import numpy as np

class Feature_Extraction():
    '''
    Feature extraction based on naive knowledge.
    This basically deterministically exposes the answers to the model on some hands. 
    I hope this is acceptable..

    Such as type of Feature Generation:

    Number of same suites/card
    Standard Deviation of same card
    Find the important feature for prediction
    Bag of number of same suites/card
    ACE is important
    '''
    def __init__(self, Data):
        '''
        Init list type of feature generation.
        Args: 
            Data : A DataFrame, Train or Test Data 
        '''
        #Must keep raw data
        self.Raw = Data
        self.Data = None

        #Local variable contains name of feature 
        self._RAW_DATA = ['S1','C1','S2','C2','S3','C3','S4','C4','S5','C5']
        self._COUNT_CARD = ['Count_C{}'.format(i) for i in range(1, 14)]
        self._STD_COUNT_CARD = ['Std_card']
        self._COUNT_SUIT = ['Count_S{}'.format(i) for i in range(1, 5)]
        self._BAG_COUNT_SUIT = ['Bag_Count_Suit_{}'.format(i) for i in range(0,6)]
        self._BAG_COUNT_CARD = ['Bag_Count_Card_{}'.format(i) for i in range(0,6)]
        self._ACE_FLAG = ['Ace_flag']

        self.fit()

    def fit(self):
        '''
        Feature generate all type
        '''
        self.Data = self.Raw
        self.Data = self.count_card()
        self.Data = self.std_count_card()
        self.Data = self.count_suit()
        self.Data = self.bag_count_suit()
        self.Data = self.bag_count_card()
        self.DataData = self.concat_Ace_flag()

    def getNameColumns(self, list_type):
        '''
        Get columns of feature generation to access data

        Args:
            List_type : A list is recevied from check box in UI

        Return:
            columns : names of feature generatetion
        '''
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
        '''
        Only get X Feature 
        Return X Data Frame
        '''
        columns = self.getNameColumns(list_type)
        return self.Data[columns]

    def getFullFeature(self, list_type):
        '''
        Get Full Feature include X and Y Data
        Return FullFeature Data Frame
        '''
        columns = self.getNameColumns(list_type)
        columns.extend(['Type'])
        return self.Data[columns]

    def getY(self):
        '''
        Return DataFrame Y Data 
        '''
        return self.Data.Type

    def getRawData(self):
        '''
        Return Raw DataFrame Data
        '''
        return self.Raw

    def count_card(self):
        '''
        Count number of same card
        EX: Card 1: 1 (ACE) , Card 2 : 2, Card 3 : 2 
        => Count_C1 = 1, Count_C2 = 2, Count_C3 = 0...Count_C13 = 0

        Return: A Data Frame feature is processed
        '''
        count_card = []
        #Count 13 card from ACE (1) to K (13)
        for i in range(1, 14):
            each_counts = pd.concat([self.Data.C1 ==i, 
                                    self.Data.C2 == i, 
                                    self.Data.C3 ==i, 
                                    self.Data.C4 == i, 
                                    self.Data.C5 ==i], axis = 1)
            count_card.append(np.sum(each_counts, axis = 1))
        #Convert to The array formed by stacking the given arrays
        count_card = np.vstack(count_card)
        #Convert to DataFrame with columns name
        count_card_df = pd.DataFrame(count_card.transpose(), 
                                    columns = ['Count_C{}'.format(i) for i in range(1, 14)])
        return pd.concat([self.Data, count_card_df], axis = 1)

    def std_count_card(self):
        '''
        Standard Deviation of same card

        Calculate std with 1, then replace all 1 with 14, 
        calculate again, if the std is smaller, then replace old one with this one
        '''
        hands = self.Data[['C1','C2','C3','C4','C5']].as_matrix()
        std = np.std(hands, axis = 1)
        hands[hands == 1] = 14
        new_std = np.std(hands, axis = 1)
        std[new_std < std] = new_std[new_std < std]
        std_df = pd.DataFrame(std, columns=['Std_card'])
        return pd.concat([self.Data, std_df],axis = 1)

    def count_suit(self):
        '''
        Count number of same suit
        EX: Suit 1: 1 (Hearts) , Suit 2 : 2 (Spades), Suit 3 : 2 (Spades)
        => Count_S1 = 1, Count_S2 = 2, Count_S3 = 0, Count_S4 = 0

        Return: A Data Frame feature is processed
        '''
        count_suit = []
        #Count 4 suit in {Hearts, Spades, Diamonds, Clubs}
        for i in range(1, 5):
            each_count = pd.concat([self.Data.S1 == i, 
                                    self.Data.S2 == i, 
                                    self.Data.S3 == i, 
                                    self.Data.S4 == i, 
                                    self.Data.S5 == i], axis = 1)
            count_suit.append(np.sum(each_count, axis = 1))
        #Convert to The array formed by stacking the given arrays
        count_suit = np.vstack(count_suit)
        #Convert to DataFrame with columns name
        count_suit_df = pd.DataFrame(count_suit.transpose(), 
                                    columns = ['Count_S{}'.format(i) for i in range(1, 5)])
        return pd.concat([self.Data, count_suit_df], axis = 1)
    
    def bag_count_suit(self):
        '''
        Bag of number of same suites [0, 5]
        Ex: Count_S1 = 1, Count_S2 = 2, Count_S3 = 1, Count_S4 = 1
        => Bag_Count_1 = 3 , Bag_Count_2 = 1, Bag_Count_3...4...5 = 0
        '''
        bag_count_suit = []
        for i in range(0, 6):
            each_counts = pd.concat([self.Data.Count_S1 == i, 
                                    self.Data.Count_S2 == i, 
                                    self.Data.Count_S3 == i, 
                                    self.Data.Count_S3 == i], axis=1)
            bag_count_suit.append(np.sum(each_counts, axis=1))
        #Convert to The array formed by stacking the given arrays
        bag_count_suit = np.vstack(bag_count_suit)
        #Convert to DataFrame with columns name
        bag_count_suit_df = pd.DataFrame(bag_count_suit.transpose(), 
                                        columns=['Bag_Count_Suit_{}'.format(i) for i in range(0,6)])
        return pd.concat([self.Data, bag_count_suit_df], axis = 1)

    def bag_count_card(self):
        '''
        Bag of number of same card in [0, 5]
        Ex: Count_C1 = 1, Count_C2 = 2, Count_C3 = 1, Count_C4 = 1
        => Bag_Count_C1 = 3 , Bag_Count_C2 = 1, Bag_Count_C3..4..5 = 0
        '''
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
        #Convert to The array formed by stacking the given arrays
        bag_count_card = np.vstack(bag_count_card)
        #Convert to DataFrame with columns name
        bag_count_card_df = pd.DataFrame(bag_count_card.transpose(),
                                    columns=['Bag_Count_Card_{}'.format(i) for i in range(0,6)])
        return pd.concat([self.Data, bag_count_card_df], axis=1)

    def concat_Ace_flag(self):
        '''
        The ACE is important
        Column important if hand have ACE
        '''
        self.Data['Ace_flag']= self.Data['Count_C1']==1
        return self.Data
    