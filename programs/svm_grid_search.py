from sklearn import svm
import numpy as np
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
import pandas as pd
import patch_manager
np.set_printoptions(suppress=True)
np.set_printoptions(threshold=np.nan)


#process feature vector of each file
X= patch_manager.get_X_list()
Y= patch_manager.get_Y_list()


#---- learning a SVM classifier -------------

kf = KFold(n_splits=5)

gamma_list = [1e-3, 1e-4,1e-5]
C_list = [1, 10, 100, 1000]
max_accuracy=0
max_accuracy_data=[0,0]
result_dict ={}
for gamma_val in gamma_list:
    mean_list = []
    for C_val in C_list:
        mean_val = 0
        for counter in range(2):
            model = svm.SVC(kernel='rbf', C=C_val,gamma=gamma_val)
            result = cross_val_score(model, X, Y, cv=kf)
            mean_val += result.mean()
        mean_val = round((mean_val/2),4)
        if mean_val > max_accuracy:
            max_accuracy= mean_val
            max_accuracy_data=[gamma_val,C_val]
        mean_list.append(mean_val)
    result_dict[gamma_val] = mean_list

df = pd.DataFrame(result_dict,index=C_list)
print (df)

print ('maximum accuracy at: gamma_val,C_val: ',max_accuracy_data[0]," , ",max_accuracy_data[1])




