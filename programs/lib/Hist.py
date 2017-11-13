#!usr/bin/python

def intensity(img):

    num=256
    onedarray=[0 for index in range(num)]
    
    
    for row in img:
        for col in row:
            
            onedarray[int(col)] += 1
    return (onedarray)
    
#    plt.hist(onedarray,256,[0,256], color = 'r')
#    plt.xlabel('Values')
#    plt.ylabel('Frequencies')
##    plt.axis([0,256])
#    plt.xlim([0,256])
#    
#    #plt.legend(('cdf','histogram'), loc = 'upper left')
#    plt.show()
#    
#    
#
#
#l=[[1,2,1,2],[1,2,2,2],[3,3,3,2]]
#
#intensity(l)