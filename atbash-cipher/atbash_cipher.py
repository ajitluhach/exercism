import re


def encode(string):
    string = string.lower().replace(' ', '')
    atbash = ''
    a = ord('a')
    z = ord('z')
    for each in string:
        each = ord(each)
        if each >= 48 and each <= 57:
            atbash += chr(each)
        elif each >= 97 and each <= 122:
            each = z - each + a
            each = chr(each)
            atbash += each
    five_atbash = ' '.join(re.findall('.{1,5}', atbash))
    return five_atbash

def decode(string): 
    string = string.lower().replace(' ', '')
    atbash = ''
    a = ord('a')
    z = ord('z')
    for each in string:
        each = ord(each)
        if each >= 48 and each <= 57:
            atbash += chr(each)
        elif each >= 97 and each <= 122:
            each = z - each + a
            each = chr(each)
            atbash += each
    return atbash

