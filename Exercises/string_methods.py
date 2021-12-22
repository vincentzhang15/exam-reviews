"""
Program to practice algorithmic thinking by recreating Python 3's string methods.
Also demonstrates the purpose of the __name__ variable.
@author Vincent Zhang
@since 8 December 2021
"""

def rfind(string: str, sub: str) -> int:
    """

    >>> rfind('bcabcde', 'bc')

    """

    for i in range(len(string)-len(sub), -1, -1):
        if string[i:i+len(sub)] == sub:
            return i
    return -1

#print(rfind('bcabcde', 'bc'))

def lower(string: str) -> str:
    """
    """

    result = ''
    for c in string:
        if 'A' <= c <= 'Z':
            result += chr((ord(c) - ord('A')) + ord('a'))
        else:
            result += c
    return result

# print(lower('ABCDEdddd@#$@'))

def swapcase():
    """
    """

def isalpha(string):
    """
    """
    if len(string) == 0:
        return False

    for c in string:
        if not('A' <= c <= 'Z' or 'a' <= c <= 'z'):
            return False
    return True

# print(isalpha('#111####'))

def count(string, sub):
    """
    """
    # bcabcedf
    # bc
    string_2 = string[:]

    nums = 0
    index = rfind(string_2, sub)
    while index != -1:
        string_2 = string_2[:index]
        index = rfind(string_2, sub)
        nums += 1
    return nums


if __name__ == '__main__':
    pass
if __name__ == 'string_methods':
    print(count('bcabcedf', 'bc'))
    pass
