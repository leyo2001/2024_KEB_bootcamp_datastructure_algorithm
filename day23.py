dataAry = [188, 150, 168,  162, 105, 120,  177,  50]

def quick(arr):

    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr)//2]

    left_arr, right_arr = [], []

    for i in range(len(arr)):
        if arr[i] > pivot:
            right_arr.append(arr[i])

        elif arr[i] < pivot:
            left_arr.append(arr[i])

    return quick(left_arr) + [pivot] + quick(right_arr)

print(quick(dataAry))



