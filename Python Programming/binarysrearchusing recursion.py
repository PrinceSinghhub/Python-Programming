a=[2,43,5,6,7,7,9,1]

def binarysearch(a,key,start,end):
    if start <= end:
        mid = int((start+end)/2)
        if a [mid] > key:
            return binarysearch(a,key,start,mid-1)
        elif a[mid]<key:
            return binarysearch(a,key,mid+1,end)
        else:
            return mid
    
    print(key,"could not be found")
    return -1
print(binarysearch(a,9,0,len(a)-1))
    
