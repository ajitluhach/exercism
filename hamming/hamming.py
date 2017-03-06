def distance(dna, dna_match):
    if len(dna) != len(dna_match):
        raise ValueError('Arguments must be of different lenghs')
    return sum([1 if x != y else 0 for (x, y) in zip(dna, dna_match)])
