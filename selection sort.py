def selectionsort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(i+1,n):
            if arr[j]<arr[i]:
                arr[i],arr[j]=arr[j],arr[i]
                    
    return arr
    
arr=[3,5,1,8,7]
print(selectionsort(arr))

    