array=[1,3,2,5,4,6,7,10,9,8]
def heapify(array,n,i):
    smallest=i
    l=2*i+1
    r=2*i+2
    if l<n and array[l]<array[smallest]:
        smallest=l
    if r<n and array[r]<array[smallest]:
        smallest=r
    if smallest!=i:
        array[i],array[smallest]=array[smallest],array[i]
        heapify(array,n,smallest)
def heapSort(array):
    n=len(array)
    for i in range(int(n/2)-1,-1,-1):
        heapify(array,n,i)
    for i in range(n-1,0,-1):
        array[i],array[0]=array[0],array[i]
        heapify(array,i,0)
    array.reverse()
    return array
heapSort(array)
print(array)
