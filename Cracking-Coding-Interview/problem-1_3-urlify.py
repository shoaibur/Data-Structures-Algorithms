# URLify: Write a method to replace all spaces in a string with '%20: You may assume that 
# the string has sufficient space at the end to hold the additional characters, and that 
# you are given the "true" length of the string. (Note: If implementing in Java, please use 
# a character array so that you can perform this operation in place.)
# EXAMPLE
# Input: "Mr John Smith"
# Output: "Mr%20J ohn%20Smith"

def urlify(s):
    s = list(s)
    for i in range(len(s)):
        if s[i] == ' ':
            s[i] = '%20'
    return ''.join(s)
