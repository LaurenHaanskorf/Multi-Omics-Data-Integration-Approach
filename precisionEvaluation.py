# -*- coding: utf-8 -*-


import pandas as pd
import numpy as np
  
def MDICCscore(predicted_labels, true_labels):  

    #from sklearn.metrics.cluster import rand_score
    #RI = rand_score(true_labels, predicted_labels)

    from sklearn.metrics import adjusted_rand_score
    ARI = adjusted_rand_score(true_labels, predicted_labels)

    from sklearn.metrics.cluster import normalized_mutual_info_score
    NMI = normalized_mutual_info_score(true_labels, predicted_labels)

    from sklearn.metrics import accuracy_score
    accu = accuracy_score(np.array(true_labels), np.array(predicted_labels))

    from sklearn.metrics import f1_score
    F1 = f1_score(np.array(true_labels), np.array(predicted_labels), average='micro')
    
    level = np.array((ARI,NMI,accu,F1), dtype = "float16")
    return level


if __name__ == '__main__':     
    test_labels = pd.read_csv('.../MDICC-main/MDICC-main/data1/data1/clust.csv', header=None)
    true_labels = pd.read_csv('.../MDICC-main/MDICC-main/data1/data1/label.csv')
    true_labels = true_labels['class2'].tolist()
    true_labels = np.array(true_labels)
    
    import time
    start = time.time()
    
    #similar range as in MATLAB's demo
    precision_values = np.arange(0.01, 0.05, 0.0001)

    scores = []
    i = 0

    for col in test_labels:
        labels = test_labels[col]
        for i in range(0, len(labels)):
            if labels[i] == 1:
                labels[i] = 0
            
        for i in range(0,len(labels)):
            if labels[i] == 2:
                labels[i] = 1
          
        score_ = MDICCscore(labels, true_labels)
        #print(precision_values[col], " ", score_[0])
        scores.append(score_[0])

    
    max_value_twod_col = np.max(scores, axis = 0)
    max_val = max_value_twod_col
    
    # finding precision value with highest scores
    index = scores.index(max_val)
    optimal_precision = round(precision_values[index], 4)
    print(optimal_precision)

    #
    end = time.time()
    print(end - start)

    
    
    
    
    
    
    
    
    
    