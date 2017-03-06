def slices(string, length):
    beauty = []
    if len(string) < length or length == 0:
        raise ValueError
    for i in range(len(string) - length + 1):
        newstring = string[i:i+length]
        newstring = [int(i) for i in newstring]
        beauty.append(newstring)
    return beauty
