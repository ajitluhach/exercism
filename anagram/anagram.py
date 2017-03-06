def detect_anagrams(match, string):
    return_list = []
    for word in string:
        if word.lower() == match.lower():
            continue
        if len(match) == len(word):
            if set(word.lower()) == set(match.lower()):
                if sorted(match.lower()) == sorted(word.lower()):
                    return_list.append(word)
    return return_list