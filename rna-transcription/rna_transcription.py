def to_rna(dna):
    n_dna = []
    l = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}
    for i in dna.upper():
        if i not in l.keys():
            return ''
        else:
            n_dna.append(l[i])
    return ''.join(n_dna)
