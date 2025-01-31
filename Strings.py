print("\"\"\"\"")
s = '"hello"'
s2 = "she said"
print(s[1], s[5], s[2]) #index by position, first index is 0
# s[-1] goes the other way
print(s + " " + s2) # " " adds space between strings
print(3*"care-i cota? ")
print(len(s2))
for c in s2:
    print(c)
s = "abcdefghijklmnop"
print(s[1:4], s[6:9])
print(s[:4], s[6:])
print(s[1:10:2])
print(s[:-1])
print("racecar"[::-1])

# how to replace a letter in a string
s3 = "cat"
s3 = 'r' + s[1:]
print(s3)

s4 = "seven"
s4 = s4[:2] + "7" + s4[3:]
print(s4)

s5 = "not"
s6 = "if"
print(s5 == s6)

