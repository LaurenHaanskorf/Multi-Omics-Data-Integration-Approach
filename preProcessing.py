# -*- coding: utf-8 -*-
from sklearn.feature_selection import SelectKBest
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd

def feature_selection_percentage(name, percentage): 
    full_name = "/Users/laure/Documents/MDICC-main/MDICC-main/data1/data1/brca/" + name
    data_ = pd.read_csv(full_name, header=0)
        
    data_T = data_.T
    data_T_ = data_T.iloc[1:,:]
    #print("Shape before pre-processing: ", data_T_.shape)
    
    # removing features that only exist out of values of zero
    data_T_no_zero = data_T_.loc[:, (data_T_ != 0).any(axis=0)]
    
    labels = pd.read_csv("/Users/laure/Documents/MDICC-main/MDICC-main/data1/data1/label.csv")
    labels_ = labels["class2"].to_numpy()
    
    
    constant = int(percentage * len(data_T_no_zero.columns))
    model = SelectKBest(k=constant)
    output = model.fit_transform(data_T_no_zero, labels_)
    
    data_T_df = pd.DataFrame(output, dtype='float64')
    data_df = data_T_df.T
    
    return data_df    
