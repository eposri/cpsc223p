'''
Name: Kayla Ngo
Date: 09/17/2025
'''

# Q1
def is_palindrome(s):
    '''
    checks whether a given string, s, is a palindrome
    input: s, string
    output: boolean value, true for palindrome
    '''
    parsed_s = s.replace(' ', '').lower()
    return parsed_s == parsed_s[::-1]

# Q2
def unique_letter_count(s):
    '''
    input: single string s
    output: integer showing how many distinct letters appear in s,
            case-insensitive
    return: number of unique alphabetical characters in s
    '''
    s.strip().lower()
    s_set = set()
    
    for char in s:
        if char.isalpha():
            s_set.add(char) #will only add unique chars
    return len(s_set)