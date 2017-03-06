#
# Skeleton file for the Python "Bob" exercise.
#
import re

def hey(what):
    what = what.strip()
    if re.search(r'[A-Za-z0-9]+', what):
        if what.isupper():
            return 'Whoa, chill out!'
        elif what.endswith("?"):
            return 'Sure.'
        else:
            return "Whatever."

    return 'Fine. Be that way!'
