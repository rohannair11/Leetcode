import collections 

def solve(strs):
    ans = collections.defaultdict(list)
    for s in strs:
        ans[tuple(sorted(s))].append(s)
    return ans.values()




strs = ["eat","tea","tan","ate","nat","bat"]
print(solve(strs))

#iterate through all the strings in strs. 
#initialise default list dict and append the tuple typecasted sorted version of of the characters in the string as key and the words corresponding to those characters as value
#return value of dict. 
