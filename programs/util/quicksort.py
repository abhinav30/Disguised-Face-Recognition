def compare(path1,path2):
    path1 = path1[path1.rfind('/')+2:]
    path1 = path1[:path1.rfind('.')]
    nums1 = path1.split('_')
    x1 = int(nums1[0])
    x2 = int(nums1[1])
    x3 = int(nums1[2])
    
    path2 = path2[path2.rfind('/')+2:]
    path2 = path2[:path2.rfind('.')]
    nums2 = path2.split('_')
    y1 = int(nums2[0])
    y2 = int(nums2[1])
    y3 = int(nums2[2])
    if x1 < y1:
        return True
    elif y1 < x1 :
        return False
    else:
        if x2 < y2:
            return True
        elif y2 < x2:
            return False
        else:
            if x3 < y3:
                return True
            else:
                return False
        

def partition(myList, start, end):
    pivot_element = myList[start]
    left = start+1
    right = end
    done = False
    while not done:
        while left <= right and compare(myList[left], pivot_element):
            left = left + 1
        while compare(pivot_element,myList[right]) and right >=left:
            right = right -1
        if right < left:
            done= True
        else:
            # swap places
            temp=myList[left]
            myList[left]=myList[right]
            myList[right]=temp
    # swap start with myList[right]
    temp=myList[start]
    myList[start]=myList[right]
    myList[right]=temp
    return right

def quicksort(myList, start, end):
    if start < end:
        # partition the list
        pivot = partition(myList, start, end)
        # sort both halves
        quicksort(myList, start, pivot-1)
        quicksort(myList, pivot+1, end)
    return myList

