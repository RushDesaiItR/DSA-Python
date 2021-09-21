def getMinNum(arr, n):
    res = arr[0]
    for i in range(1, n):
        res = min(res, arr[i])
    return res
def getMaxNum(arr, n):
    res = arr[0]
    for i in range(1,n):
        res = max(res, arr[i])
    return res        
arr = [1,2,45,789,0]
n=len(arr)
print("Minimum Number IS",getMinNum(arr, n)) 
print("Maximum Number IS",getMaxNum(arr, n))    
 