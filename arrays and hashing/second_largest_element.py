
def maximum(arr):
    high = 0
    for i in range(0, len(arr)):
        if arr[i] > high:
            high = arr[i]
    return high 

def solve(arr):
    max = maximum(arr)
    for i in range(0, len(arr)):
        if(arr[i] == max):
            arr.pop()
    max2 = maximum(arr)
    if(len(arr) == 0):
        return -1
    return max2
5

arr = [10,10,10]
print(solve(arr))