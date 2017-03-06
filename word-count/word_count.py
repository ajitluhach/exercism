import re


def word_count(string):
    string = re.sub(r'[\W_]', " ", string).split()
    counter = {}
    for word in string:
        word = word.lower()
        try:
            counter[word] += 1
        except KeyError:
            counter[word] = 1
    print(counter)
    return counter