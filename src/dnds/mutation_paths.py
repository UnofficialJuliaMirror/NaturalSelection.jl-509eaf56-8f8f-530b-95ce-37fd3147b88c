def short_path(codon_1, codon_2):
    ''' (str, str) -> list
    Returns the shortest mutation pathway between two codons as a list of two
    integers. The first number of the list is the amount of synonymous mutations
    and the second is the number of non-synonymous mutations required for the most
    probable mutation pathway between two codons. The pathway with the least
    overall amount of nucleotide substitutions (synonymous + non-synonymous) and
    the least amount of non-synonymous mutations is considered as the most probable.
    >>> short_path('GTG', 'AAA')
    [1, 2]
    >>> short_path('ATG', 'CTA')
    [1, 1]
    '''
    lis = []; las =[]
    if codon_1 == codon_2:
        return [0, 0]
    for i in range(len(codon_1)):
        if codon_1[i] != codon_2[i]:
            a = ''
            a = codon_1[:i] + codon_2[i] + codon_1[(i+1):]
            lis.append(a)
    for i in range(len(lis)):
        for j in range(len(codon_2)):
            if codon_2[j] != lis[i][j]:
                a = ''
                a = lis[i][:j] + codon_2[j] + lis[i][(j+1):]
                las.append(a)
    print("Lis:")
    print(lis)
    print("Las:")
    print(las)
    if lis == []:
        print("No mutation.")
        return [0,0]
    elif codon_2 in lis:
        print("A single mutation - one pathway.")
        print(codon_1, codon_2, sep = " --> ")
        print(nuc_to_aa(codon_1), nuc_to_aa(codon_2), sep = " --> ")
        if nuc_to_aa(codon_1) == nuc_to_aa(codon_2):
            return [1, 0]
        else:
            return [0, 1]
    elif codon_2 in las:
        print("Two mutations - two pathways.")
        print(codon_1, lis[0], codon_2, sep = " --> ")
        print(nuc_to_aa(codon_1), nuc_to_aa(lis[0]), nuc_to_aa(codon_2), sep = " --> ")
        print(codon_1, lis[1], codon_2, sep = " --> ")
        print(nuc_to_aa(codon_1), nuc_to_aa(lis[1]), nuc_to_aa(codon_2), sep = " --> ")
        if (nuc_to_aa(codon_1) == nuc_to_aa(lis[0]) == nuc_to_aa(codon_2)) or (nuc_to_aa(codon_1) == nuc_to_aa(lis[1]) == nuc_to_aa(codon_2)):
            return [2,0]
        elif (nuc_to_aa(codon_1) == nuc_to_aa(lis[0]) != nuc_to_aa(codon_2)) or (nuc_to_aa(codon_1) == nuc_to_aa(lis[1]) != nuc_to_aa(codon_2)):
            return [1, 1]
        elif (nuc_to_aa(codon_1) != nuc_to_aa(lis[0]) == nuc_to_aa(codon_2)) or (nuc_to_aa(codon_1) != nuc_to_aa(lis[1]) == nuc_to_aa(codon_2)):
            return [1, 1]
        else:
            return [0, 2]
    else:
        print("Three mutations - six pathways.")
        print(codon_1, lis[0], las[0], codon_2, sep = " --> ")
        print(nuc_to_aa(codon_1), nuc_to_aa(lis[0]), nuc_to_aa(las[0]), nuc_to_aa(codon_2), sep = " --> ")
        print(codon_1, lis[0], las[1], codon_2, sep = " --> ")
        print(nuc_to_aa(codon_1), nuc_to_aa(lis[0]), nuc_to_aa(las[1]), nuc_to_aa(codon_2), sep = " --> ")
        print(codon_1, lis[1], las[2], codon_2, sep = " --> ")
        print(nuc_to_aa(codon_1), nuc_to_aa(lis[1]), nuc_to_aa(las[2]), nuc_to_aa(codon_2), sep = " --> ")
        print(codon_1, lis[1], las[3], codon_2, sep = " --> ")
        print(nuc_to_aa(codon_1), nuc_to_aa(lis[1]), nuc_to_aa(las[3]), nuc_to_aa(codon_2), sep = " --> ")
        print(codon_1, lis[2], las[4], codon_2, sep = " --> ")
        print(nuc_to_aa(codon_1), nuc_to_aa(lis[2]), nuc_to_aa(las[4]), nuc_to_aa(codon_2), sep = " --> ")
        print(codon_1, lis[2], las[5], codon_2, sep = " --> ")
        print(nuc_to_aa(codon_1), nuc_to_aa(lis[2]), nuc_to_aa(las[5]), nuc_to_aa(codon_2), sep = " --> ")
        if (nuc_to_aa(codon_1) == nuc_to_aa(lis[0]) == nuc_to_aa(las[0]) == nuc_to_aa(codon_2)) or (nuc_to_aa(codon_1) == nuc_to_aa(lis[0]) == nuc_to_aa(las[1]) == nuc_to_aa(codon_2)):
            return [3, 0]
        elif (nuc_to_aa(codon_1) == nuc_to_aa(lis[1]) == nuc_to_aa(las[2]) == nuc_to_aa(codon_2)) or (nuc_to_aa(codon_1) == nuc_to_aa(lis[1]) == nuc_to_aa(las[3]) == nuc_to_aa(codon_2)):
            return [3, 0]
        elif (nuc_to_aa(codon_1) == nuc_to_aa(lis[2]) == nuc_to_aa(las[4]) == nuc_to_aa(codon_2)) or (nuc_to_aa(codon_1) == nuc_to_aa(lis[2]) == nuc_to_aa(las[5]) == nuc_to_aa(codon_2)):
            return [3, 0]
        elif (nuc_to_aa(codon_1) == nuc_to_aa(lis[0]) == nuc_to_aa(las[0]) != nuc_to_aa(codon_2)) or (nuc_to_aa(codon_1) == nuc_to_aa(lis[0]) == nuc_to_aa(las[1]) != nuc_to_aa(codon_2)):
            return [2, 1]
        elif (nuc_to_aa(codon_1) == nuc_to_aa(lis[1]) == nuc_to_aa(las[2]) != nuc_to_aa(codon_2)) or (nuc_to_aa(codon_1) == nuc_to_aa(lis[1]) == nuc_to_aa(las[3]) != nuc_to_aa(codon_2)):
            return [2, 1]
        elif (nuc_to_aa(codon_1) == nuc_to_aa(lis[2]) == nuc_to_aa(las[4]) != nuc_to_aa(codon_2)) or (nuc_to_aa(codon_1) == nuc_to_aa(lis[2]) == nuc_to_aa(las[5]) != nuc_to_aa(codon_2)):
            return [2, 1]
        elif (nuc_to_aa(codon_1) == nuc_to_aa(lis[0]) != nuc_to_aa(las[0]) == nuc_to_aa(codon_2)) or (nuc_to_aa(codon_1) == nuc_to_aa(lis[0]) != nuc_to_aa(las[1]) == nuc_to_aa(codon_2)):
            return [2, 1]
        elif (nuc_to_aa(codon_1) == nuc_to_aa(lis[1]) != nuc_to_aa(las[2]) == nuc_to_aa(codon_2)) or (nuc_to_aa(codon_1) == nuc_to_aa(lis[1]) != nuc_to_aa(las[3]) == nuc_to_aa(codon_2)):
            return [2, 1]
        elif (nuc_to_aa(codon_1) == nuc_to_aa(lis[2]) != nuc_to_aa(las[4]) == nuc_to_aa(codon_2)) or (nuc_to_aa(codon_1) == nuc_to_aa(lis[2]) != nuc_to_aa(las[5]) == nuc_to_aa(codon_2)):
            return [2, 1]
        elif (nuc_to_aa(codon_1) != nuc_to_aa(lis[0]) == nuc_to_aa(las[0]) == nuc_to_aa(codon_2)) or (nuc_to_aa(codon_1) != nuc_to_aa(lis[0]) == nuc_to_aa(las[1]) == nuc_to_aa(codon_2)):
            return [2, 1]
        elif (nuc_to_aa(codon_1) != nuc_to_aa(lis[1]) == nuc_to_aa(las[2]) == nuc_to_aa(codon_2)) or (nuc_to_aa(codon_1) != nuc_to_aa(lis[1]) == nuc_to_aa(las[3]) == nuc_to_aa(codon_2)):
            return [2, 1]
        elif (nuc_to_aa(codon_1) != nuc_to_aa(lis[2]) == nuc_to_aa(las[4]) == nuc_to_aa(codon_2)) or (nuc_to_aa(codon_1) != nuc_to_aa(lis[2]) == nuc_to_aa(las[5]) == nuc_to_aa(codon_2)):
            return [2, 1]
        elif (nuc_to_aa(codon_1) != nuc_to_aa(lis[0]) != nuc_to_aa(las[0]) == nuc_to_aa(codon_2)) or (nuc_to_aa(codon_1) != nuc_to_aa(lis[0]) != nuc_to_aa(las[1]) == nuc_to_aa(codon_2)):
            return [1, 2]
        elif (nuc_to_aa(codon_1) != nuc_to_aa(lis[1]) != nuc_to_aa(las[2]) == nuc_to_aa(codon_2)) or (nuc_to_aa(codon_1) != nuc_to_aa(lis[1]) != nuc_to_aa(las[3]) == nuc_to_aa(codon_2)):
            return [1, 2]
        elif (nuc_to_aa(codon_1) != nuc_to_aa(lis[2]) != nuc_to_aa(las[4]) == nuc_to_aa(codon_2)) or (nuc_to_aa(codon_1) != nuc_to_aa(lis[2]) != nuc_to_aa(las[5]) == nuc_to_aa(codon_2)):
            return [1, 2]
        elif (nuc_to_aa(codon_1) != nuc_to_aa(lis[0]) == nuc_to_aa(las[0]) != nuc_to_aa(codon_2)) or (nuc_to_aa(codon_1) != nuc_to_aa(lis[0]) == nuc_to_aa(las[1]) != nuc_to_aa(codon_2)):
            return [1, 2]
        elif (nuc_to_aa(codon_1) != nuc_to_aa(lis[1]) == nuc_to_aa(las[2]) != nuc_to_aa(codon_2)) or (nuc_to_aa(codon_1) != nuc_to_aa(lis[1]) == nuc_to_aa(las[3]) != nuc_to_aa(codon_2)):
            return [1, 2]
        elif (nuc_to_aa(codon_1) != nuc_to_aa(lis[2]) == nuc_to_aa(las[4]) != nuc_to_aa(codon_2)) or (nuc_to_aa(codon_1) != nuc_to_aa(lis[2]) == nuc_to_aa(las[5]) != nuc_to_aa(codon_2)):
            return [1, 2]
        elif (nuc_to_aa(codon_1) == nuc_to_aa(lis[0]) != nuc_to_aa(las[0]) != nuc_to_aa(codon_2)) or (nuc_to_aa(codon_1) == nuc_to_aa(lis[0]) != nuc_to_aa(las[1]) != nuc_to_aa(codon_2)):
            return [1, 2]
        elif (nuc_to_aa(codon_1) == nuc_to_aa(lis[1]) != nuc_to_aa(las[2]) != nuc_to_aa(codon_2)) or (nuc_to_aa(codon_1) == nuc_to_aa(lis[1]) != nuc_to_aa(las[3]) != nuc_to_aa(codon_2)):
            return [1, 2]
        elif (nuc_to_aa(codon_1) == nuc_to_aa(lis[2]) != nuc_to_aa(las[4]) != nuc_to_aa(codon_2)) or (nuc_to_aa(codon_1) == nuc_to_aa(lis[2]) != nuc_to_aa(las[5]) != nuc_to_aa(codon_2)):
            return [1, 2]
        elif (nuc_to_aa(codon_1) != nuc_to_aa(lis[0]) != nuc_to_aa(las[0]) != nuc_to_aa(codon_2)) or (nuc_to_aa(codon_1) != nuc_to_aa(lis[0]) != nuc_to_aa(las[1]) != nuc_to_aa(codon_2)):
            return [0, 3]
        elif (nuc_to_aa(codon_1) != nuc_to_aa(lis[1]) != nuc_to_aa(las[2]) != nuc_to_aa(codon_2)) or (nuc_to_aa(codon_1) != nuc_to_aa(lis[1]) != nuc_to_aa(las[3]) != nuc_to_aa(codon_2)):
            return [0, 3]
        elif (nuc_to_aa(codon_1) != nuc_to_aa(lis[2]) != nuc_to_aa(las[4]) != nuc_to_aa(codon_2)) or (nuc_to_aa(codon_1) != nuc_to_aa(lis[2]) != nuc_to_aa(las[5]) != nuc_to_aa(codon_2)):
            return [0, 3]

def nuc_to_aa(seq):
    ''' (str) -> str
    Returns a string of amino acids coded by the sequence.
    >>> nuc_to_aa('ATGGCCATG')
    'MAM'
    '''
    aa = ''
    for i in range(len(seq)):
        if i%3 == 0:
            aa += str((get_aa(seq[i:(i+3)])))
    return aa

def get_aa(codon):
    ''' (str) -> str
    Returns the aminoacid coded by the codon.
    >>> get_aa('AUG')
    'M'
    >>> get_aa('CAA')
    'Q'
    '''
    if codon in ['UUU', 'UUC', 'TTT', 'TTC']:
        return 'F'
    elif codon in ['UUA', 'UUG', 'CUU', 'CUC', 'CUA', 'CUG', 'TTA', 'TTG', 'CTT', 'CTC', 'CTA', 'CTG']:
        return 'L'
    elif codon in ['AUU', 'AUC', 'AUA', 'ATT', 'ATC', 'ATA']:
        return 'I'
    elif codon in ['AUG', 'ATG']:
        return 'M'
    elif codon in ['GUU', 'GUC', 'GUA', 'GUG', 'GTT', 'GTC', 'GTA', 'GTG']:
        return 'V'
    elif codon in ['UCU', 'UCC', 'UCA', 'UCG', 'TCT', 'TCC', 'TCA', 'TCG', 'AGU', 'AGC', 'AGT']:
        return 'S'
    elif codon in ['CCU', 'CCC', 'CCA', 'CCG', 'CCT']:
        return 'P'
    elif codon in ['ACU', 'ACC', 'ACA', 'ACG', 'ACT']:
        return 'T'
    elif codon in ['GCU', 'GCC', 'GCA', 'GCG', 'GCT']:
        return 'A'
    elif codon in ['UAU', 'UAC', 'TAT', 'TAC']:
        return 'Y'
    elif codon in ['CAU', 'CAC', 'CAT']:
        return 'H'
    elif codon in ['CAA', 'CAG']:
        return 'Q'
    elif codon in ['AAU', 'AAC', 'AAT']:
        return 'N'
    elif codon in ['AAA', 'AAG']:
        return 'K'
    elif codon in ['GAU', 'GAC', 'GAT']:
        return 'D'
    elif codon in ['GAA', 'GAG']:
        return 'E'
    elif codon in ['UGU', 'UGC', 'TGT', 'TGC']:
        return 'C'
    elif codon in ['UGG', 'TGG']:
        return 'W'
    elif codon in ['CGU', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG', 'CGT']:
        return 'R'
    elif codon in ['GGU', 'GGC', 'GGA', 'GGG', 'GGT']:
        return 'G'
    elif codon in ['UAA', 'UAG', 'UGA', 'TAA', 'TAG', 'TGA']:
        return '*'


def multi_short_path(list_of_codon):
    ''' (list) -> list
    Returns the shortest mutation pathway between a list of codons as a list of two
    integers. The first integer of the list is the amount of synonymous mutations and the
    second is the number of non-synonymous mutations required for the most probable
    mutation pathway between codons. The pathway with the least overall amount of
    nucleotide substitutions (synonymous + non-synonymous) and the least amount of
    non-synonymous mutations is considered as the most probable. Codons with incomplete
    sequences are excluded from the final computation. The computation is made using
    Kruskal's alogrithm.
    >>> multi_short_path(['AAA', 'AGA', 'AAG'])
    [1, 1]
    >>> multi_short_path(['AAA', 'AGA', 'AAG', 'CCC'])
    [3, 2]
    '''
    mat = []; p = [0,0]; g = []; h = []
    for i in range(len(list_of_codon)):
        for j in range(len(list_of_codon)):
            mat.append(short_path(list_of_codon[i], list_of_codon[j]))
            g.append(list_of_codon[i])
            g.append(list_of_codon[j])
    print(mat)
    print(g)
    for k in range(len(mat)):
        a = (get_rank(mat[k]), g[k*2], g[(k*2)+1])
        h.append(a)
    print(h)
    graph = {'vertices':list_of_codon, 'edges':set(h)}
    print(graph)
    t = kruskal(graph)
    f = list(t)
    for m in range(len(f)):
        n = get_lst(f[m][0])
        p[0] += n[0]
        p[1] += n[1]
    return p

def get_rank(lst):
    ''' (list) -> int
    Helper function for the multi_short_path() function. Ranks all possible
    nucleotide substitution combinations between two codons. The first number of
    the lst represent the number of synonymous substitutions while the second
    represents the number of non-synonymous substitutions. The ranking is done by
    the following hieararchy: [1, 0], [0, 1], [2, 0], [1, 1], [0, 2], [3, 0],
    [2, 1], [1, 2], [0, 3].
    >>> get_rank([0, 1])
    2
    >>> get_rank([0, 2])
    5
    '''
    rank = 0
    if lst == [1, 0]:
        rank = 1
    elif lst == [0, 1]:
        rank = 2
    elif lst == [2, 0]:
        rank = 3
    elif lst == [1, 1]:
        rank = 4
    elif lst == [0, 2]:
        rank = 5
    elif lst == [3, 0]:
        rank = 6
    elif lst == [2, 1]:
        rank = 7
    elif lst == [1, 2]:
        rank = 8
    elif lst == [0, 3]:
        rank = 9
    return rank



def pathways_a(codon_1, codon_2):
    ''' (str, str) -> print
    Returns all possible direct mutation pathways between two codons in
    aminoacid form.
    >>> pathways_a('AAA', 'AGA')
    K -> R
    >>> pathways_a('ATG', 'CTA')
    M -> L -> L
    M -> I -> L
    '''
    lis = []; las = []
    for i in range(len(codon_1)):
        if codon_1[i] != codon_2[i]:
            a = ''
            a = codon_1[:i] + codon_2[i] + codon_1[(i+1):]
            lis.append(a)
    for i in range(len(lis)):
        for j in range(len(codon_2)):
            if codon_2[j] != lis[i][j]:
                a = ''
                a = lis[i][:j] + codon_2[j] + lis[i][(j+1):]
                las.append(a)
    if lis == []:
        print(nuc_to_aa(codon_1) + ' -> ' + nuc_to_aa(codon_2))
    elif codon_2 in lis:
        print(nuc_to_aa(codon_1) + ' -> ' + nuc_to_aa(codon_2))
    elif codon_2 in las:
        print(nuc_to_aa(codon_1) + ' -> ' + nuc_to_aa(lis[0]) + ' -> ' + nuc_to_aa(codon_2))
        print(nuc_to_aa(codon_1) + ' -> ' + nuc_to_aa(lis[1]) + ' -> ' + nuc_to_aa(codon_2))
    else:
        print(nuc_to_aa(codon_1) + ' -> ' + nuc_to_aa(lis[0]) + ' -> ' + nuc_to_aa(las[0]) + ' -> ' + nuc_to_aa(codon_2))
        print(nuc_to_aa(codon_1) + ' -> ' + nuc_to_aa(lis[0]) + ' -> ' + nuc_to_aa(las[1]) + ' -> ' + nuc_to_aa(codon_2))
        print(nuc_to_aa(codon_1) + ' -> ' + nuc_to_aa(lis[1]) + ' -> ' + nuc_to_aa(las[2]) + ' -> ' + nuc_to_aa(codon_2))
        print(nuc_to_aa(codon_1) + ' -> ' + nuc_to_aa(lis[1]) + ' -> ' + nuc_to_aa(las[3]) + ' -> ' + nuc_to_aa(codon_2))
        print(nuc_to_aa(codon_1) + ' -> ' + nuc_to_aa(lis[2]) + ' -> ' + nuc_to_aa(las[4]) + ' -> ' + nuc_to_aa(codon_2))
        print(nuc_to_aa(codon_1) + ' -> ' + nuc_to_aa(lis[2]) + ' -> ' + nuc_to_aa(las[5]) + ' -> ' + nuc_to_aa(codon_2))

###########################################################################

def pathways_n(codon_1, codon_2):
    ''' (str, str) -> print
    Returns all possible direct mutation pathways between two codons in
    nucleotide form.
    >>> pathways_n('AAA', 'AGA')
    AAA -> AGA
    >>> pathways_n('ATG', 'CTA')
    ATG -> CTG -> CTA
    ATG -> ATA -> CTA
    '''
    lis = []; las = []
    for i in range(len(codon_1)):
        if codon_1[i] != codon_2[i]:
            a = ''
            a = codon_1[:i] + codon_2[i] + codon_1[(i+1):]
            lis.append(a)
    for i in range(len(lis)):
        for j in range(len(codon_2)):
            if codon_2[j] != lis[i][j]:
                a = ''
                a = lis[i][:j] + codon_2[j] + lis[i][(j+1):]
                las.append(a)
    if lis == []:
        print(codon_1 + ' -> ' + codon_2)
    elif codon_2 in lis:
        print(codon_1 + ' -> ' + codon_2)
    elif codon_2 in las:
        print(codon_1 + ' -> ' + lis[0] + ' -> ' + codon_2)
        print(codon_1 + ' -> ' + lis[1] + ' -> ' + codon_2)
    else:
        print(codon_1 + ' -> ' + lis[0] + ' -> ' + las[0] + ' -> ' + codon_2)
        print(codon_1 + ' -> ' + lis[0] + ' -> ' + las[1] + ' -> ' + codon_2)
        print(codon_1 + ' -> ' + lis[1] + ' -> ' + las[2] + ' -> ' + codon_2)
        print(codon_1 + ' -> ' + lis[1] + ' -> ' + las[3] + ' -> ' + codon_2)
        print(codon_1 + ' -> ' + lis[2] + ' -> ' + las[4] + ' -> ' + codon_2)
        print(codon_1 + ' -> ' + lis[2] + ' -> ' + las[5] + ' -> ' + codon_2)
