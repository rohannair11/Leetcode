def solve(nums):

    hashset = set()
    for num in nums:
        if(num in hashset):
            return True
        hashset.add(num)
    return False

nums = [1,2,3,1]
print(solve(nums))

#used a hashset (set in python) to iterate through the array and to check if the element exists in the set. if it exists return true else false. 