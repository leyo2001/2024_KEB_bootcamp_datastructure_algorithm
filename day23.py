arr = [1,10,4,5,9,8,7]





for i in range(len(arr)-1):
    for j in range(i+1,len(arr)):
        if arr[j] < arr[i]:
            arr[i], arr[j] = arr[j], arr[i]

print(arr)








