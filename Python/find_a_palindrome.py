import re

def palindrome(input_string):
    # sub all non alphanumeric with ''
    letters_string = re.sub('[^0-9A-Za-z]', '', input_string)
    
    # convert to lowercase
    letters_string = letters_string.lower()
    
    # function to reverse a string
    def reversed_string(aString):
        return aString[::-1]

    rev_string = reversed_string(letters_string)

    print(rev_string)
    print(letters_string)
    print(rev_string == letters_string)

palindrome('A man, a plan, a canal. Panama')
