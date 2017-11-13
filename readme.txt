DATASET URL :- "http://www.iab-rubric.org/databases/visible_cropped.zip"
		Due to copyright issue we are not uploading actual dataset.

Github link :- 


Steps to run and test disguised Face recognition algorithm:-

1. Run extract_feature.py
	This program will read image intensity pixels from tranining_data/patches folder
	And create files 
		X.txt: contains feature vector of all samples as "list of lists"
		Y.txt: contains label of all samples present in X.txt
		filelist: contains filename of all patches in format "Pi_j_k" , i= subject no, j= image no , k = patch no

2. Run svm_grid_search.py 
	This program will do grid search on gamma and C. It does 5-fold cross validation and print the result

3. patch_manager.py to be used by test_images training SVM.
 
4. Run test_images.py
	This program will first run patch_manager.train_svm(patch_count) to train the SVM classifer (patch_classifier)
	Once SVM is trained , it will create gallery and probe list using function:
		get_gallery_probe_list(file_list,i,j) //it will create gallery and probe list from images subject i to j

	It will then print accuracy accross various thresholds (set in thresholds list)
	And finally generate ROC curve for FAR vs GAR (for biometric patches and all patches)

 
NOTE:- other helper programs are kept in lib and util folders
some of the important lib programs are-

Hist.py :- input: patch intensity vector
	   output: list of 256 features (representing intesity histogram)

lbp.py :- input: patch intensity vector
	  output: list of 256 features (representing lbp histogram)
   
