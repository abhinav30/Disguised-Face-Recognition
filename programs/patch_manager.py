from sklearn import svm
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, auc,roc_auc_score
from sklearn.model_selection import train_test_split
np.set_printoptions(suppress=True)
np.set_printoptions(threshold=np.nan)

file_list = []
X=[]
Y=[]

#----------initialize sample lists from file ----------------
file1  = open('../files/X.txt',"r")
for line in file1:
    values = line.split(',')
    #print(values)
    float_vals=[float(x) for x in values]
    X.append(float_vals)

file2  = open('../files/Y.txt',"r")
for line in file2:
    Y.append(int(line))
    
file3  = open('../files/filelist',"r")
for line in file3:
    file_list.append(line)

def get_X_list():
    return X

def get_Y_list():
    return Y

def get_file_list():
    return file_list

#--------------train the svm -------------------------------------
model = svm.SVC(kernel='rbf', C=1000,gamma=0.001,probability=True)


def train_svm(patch_count):
    x_train = []
    y_train = []
    for i in range(patch_count):
        x_train.append(X[i])
        y_train.append(Y[i])
    model.fit(x_train, y_train)

def predict_patches(x_test):
    global model
    predicted_class = model.predict(x_test)
    return predicted_class


