def solve(s, t):
    if (sorted(s) == sorted(t)):
        return True
    return False

s = "rat"
t = "tar"
print(solve(s,t))

#if two words are anagrams, then the sorted version of the word will contain the same letters. If this is the case, then the words are anagrams of each other