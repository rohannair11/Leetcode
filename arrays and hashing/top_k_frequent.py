def solve(nums):
    res = {}
    for i in range(len(nums)):
        res[nums[i]] = 0; 
    for i in range(len(nums)):
        if(nums[i] in res):
            res[nums[i]] += 1
    
    
    


nums =  [1,1,1,2,2,3]
print(solve(nums))