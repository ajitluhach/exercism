import string
import re


def is_pangram(strr, alphabet=string.ascii_lowercase):
    strr = re.sub(r'[^\w\s]', '', strr)
    if not (set(alphabet) - set(strr.lower())):
        return True
    return False
