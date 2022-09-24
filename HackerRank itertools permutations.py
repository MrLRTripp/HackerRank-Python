from itertools import permutations

def print_permutaions(word, length):
    char_list = list(word)
    char_list.sort()
    for tup in permutations(char_list,length):
        print(''.join(tup))
    return None

if __name__ == '__main__':
    # Read word and length of permutations
    # length of permutations cannot exceed word length
    word, perm_len = input('Enter word and permutation length: ').split()
    print_permutaions(word, min(len(word), int(perm_len)))