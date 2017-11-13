import sys
sys.path.append('lib/')
sys.path.append('util/')
import numpy as np
import os
import lbp as lbp
import quicksort as qsort
import load_label as ll
import Hist
np.set_printoptions(suppress=True)
np.set_printoptions(threshold=np.nan)

Xfile = open('../files/X.txt','w')
Yfile = open('../files/Y.txt','w')
f = open('../files/filelist','w')
def read_file(filename):
    file  = open(filename,"r")
    data=[]
    for line in file:
        values = line.split(',')
        float_vals=[float(x) for x in values]
        data.append(float_vals)
    return data

# Find the min and max values for each column
def dataset_minmax(dataset):
	stats = [[min(column), max(column)] for column in zip(*dataset)]
	return stats

# Rescale dataset columns to the range 0-1
def normalize_dataset(dataset):
    minmax = dataset_minmax(dataset)
    for row in dataset:
        for i in range(len(row)):
            row[i]=float(row[i])
            #print minmax[i][1], " , ",minmax[i][0]
            row[i] =round( ((row[i] - minmax[i][0]) / (minmax[i][1] - minmax[i][0])),6)

file_count = 0
file_list = []
for root, dirs, files in os.walk('../training_data/patches'):
    for file in files:
        if file[0]=='.':
            continue
        image_path =  os.path.join(root, file)
        file_count += 1
        file_list.append(image_path)
    


#sort file in as per its path 
file_list = qsort.quicksort(file_list,0,len(file_list)-1)

#process feature vector of each file
X=[]
Y=[]
label_dict = ll.load_label('../files/label.txt')
for counter,file_path in enumerate(file_list):
    if counter > 5000:
        break
    file_name = file_path[file_path.rfind('/')+1:]
    file_name = file_name[:file_name.rfind('.')]
    f.write(file_name+'\n')
    data = read_file(file_path)
    feature_vector_lbp = lbp.lbp_calc(data).tolist()
    feature_vector_itn = Hist.intensity(data)
    feature_vector_lbp.extend(feature_vector_itn)
    X.append(feature_vector_lbp)
    Y.append(label_dict[file_name])

normalize_dataset(X)
#print X
#print Y

#Accuracy
for val in X:
    lenval = len(val)
    for counter,num in enumerate(val):
        Xfile.write(str(num))
        if counter != lenval-1:
            Xfile.write(',')
    Xfile.write('\n')

Xfile.close()

counter = 0
for val in Y:
    Yfile.write(str(val))
    Yfile.write('\n')
    counter += 1
    
Yfile.close()
for val in file_list:
    f.write(str(val))


f.close()