import string


def rotate(to_cypher, rotate_by=26):
    newstring = ''
    if rotate_by >= 26:
        rotate_by = rotate_by - 26
    for s in to_cypher:
        if 65 <= ord(s) <= 90:
            value = ord(s) + rotate_by
            if value > 90:
                value = 65 + value - 90
            newstring += chr(value)
        elif 97 <= ord(s) <= 122:
            value = ord(s) + rotate_by
            if value > 122:
                value = 97 + value - 122
            newstring += chr(value)
        else:
            newstring += s
    return newstring
