import re

def encode(string):
    final = list()
    previous = ''
    count = 0
    for char in string:
        if previous == '':
            previous = char
            count +=1
            continue
        if char == previous:
            count +=1
        else:
            if count == 1:
                count = ''
            final.append(str(count))
            final.append(str(previous))
            previous = char
            count= 1
    if count != 1:
        final.append(str(count))
    final.append(previous)
    final = ''.join(final)
    return final


def decode(i_stripe):
    buf = ''
    decoded_str = ''
    lst = list()
    for symbol in i_stripe:
        s = re.match('\d', symbol)        
        if s:
            buf = buf + symbol
            continue
        else:
            if buf != '':
                lst.append((symbol, int(buf)))
            else:
                lst.append((symbol, 1))
            buf = ''
    lst1 = [key*value for key,value in lst]
    decoded_str = ''.join(lst1)
    return decoded_str

print(encode('AABBBCCCC'))


