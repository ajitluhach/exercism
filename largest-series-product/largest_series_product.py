from functools import reduce


def largest_product(string, limit):
    largest_product = 0
    if len(string) < limit or limit < 0:  # Error inputs
        raise ValueError("Span is more than string")
    if len(string) > 1 and int(string) == 0:  # When all digits are zero
        return 0
    if limit == 0:  # Case when string is non empty and empty but span is zero
        return 1
    if len(string) == limit:
        return reduce(lambda x, y: x*y, map(int, list(string)))
    for i in range(1, len(string) - limit + 1):
        product = reduce(lambda x, y: x*y, map(int, list(string[i:i+limit])))
        if product > largest_product:
            largest_product = product
    return largest_product
