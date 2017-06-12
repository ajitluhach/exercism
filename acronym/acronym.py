import re


def abbreviate(to_abbreviate):
    return ''.join(word[0].upper() for word in 
            re.findall('[A-Z]+[a-z]*|[a-z]+', to_abbreviate))
