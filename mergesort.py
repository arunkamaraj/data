def mergeSort(alist):
    print("Splitting ",alist)
    if len(alist)>1:
        mid = len(alist)//2
	print "mid value:",mid
        lefthalf = alist[:mid]
	print "Left half:",lefthalf
        righthalf = alist[mid:]
	print "Right half:",righthalf
	
	print "calling mersort for left half"
        mergeSort(lefthalf)
	print "calling mergsort for right half "
        mergeSort(righthalf)
	
	print "initializing the value "
        i=0
        j=0
        k=0
        while i<len(lefthalf) and j<len(righthalf):
            if lefthalf[i]<righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i<len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j<len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merging ",alist)

alist = [54,26,93,17,77,31]
mergeSort(alist)
print(alist)

