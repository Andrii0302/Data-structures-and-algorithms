array=[1,3,2,5,4,6,7,10,9,8]
def merge(array,l,m,r):
    n1=m-l+1
    n2=r-m
    L=[0]*(n1)
    R=[0]*(n2)
    for i in range(0,n1):
        L[i]=array[l+i]
    for i in range(0,n2):
        R[i]=array[m+1+i]
    
    i=0
    j=0
    k=l
    while i<n1 and j<n2:
        if L[i]<=R[j]:
            array[k]=L[i]
            i+=1
        else:
            array[k]=R[j]
            j+=1
        k+=1
    while i<n1:
        array[k]=L[i]
        i+=1
        k+=1
    while j<n2:
            array[k]=R[j]
            j+=1
            k+=1
def mergeSort(array,l,r):
    if l<r:
        m=l+(r-l)//2
        mergeSort(array,l,m)
        mergeSort(array,m+1,r)
        merge(array,l,m,r)
    return array

mergeSort(array,0,9)
print(array)
