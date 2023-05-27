def solve(str):
    newStr = ""
    for c in s:
        if c.isalnum():
            newStr += c.lower()
    return newStr == newStr[::-1]

s = "A man, a plan, a canal: Panama"
print(solve(s))