import re

def isPalindrome(x):
    # convert to string
    x_string = str(x)
    if x < 0:
        x_string = re.sub('[^0-9]','',x_string)
        _sign = '-'
    else: 
        _sign = ''
    # reverse string
    rev_string = _sign + x_string[::-1]
    # convert back to int
    rev_x = int(rev_string)
    
    print(rev_x)
    print(x == rev_x)
    # return bool
    return x == rev_x

isPalindrome(-818)

