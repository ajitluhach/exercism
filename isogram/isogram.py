def is_isogram(word):
    if not word:
        return True
    else:
        word = word.lower()
        for char in word:
            if word.count(char) > 1 and char in "abcdefghijklmnopqrstwxyz":
                return False
        return True
