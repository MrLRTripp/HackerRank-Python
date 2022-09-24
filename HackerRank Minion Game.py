def minion_game(string):
    """
    Stewart has to create all substrings that start with a consonant
    Kevin has to create all substrings that start with a vowel
    For each substring, count how many times it appears in string.
    Total the score for each player
    """

    vowels = 'aeiou'

    k_list = [string[i:j] for i in range(0,len(string)) for j in range(i+1,len(string)+1) if string[i] in vowels]
    s_list = [string[i:j] for i in range(0,len(string)) for j in range(i+1,len(string)+1) if string[i] not in vowels]

    #print(k_list)
    #print(s_list)
    # VVVVVVVVVVVVVVVVVVVVVVVVVV
    # Since the game only requires the final total and not the counts of each substring, there is no need
    # to build the dicts.
    # Just compute the len of k_list and s_list

    # Make the substrings keys in a dict. The value is count of that substring
    # stewart_dict = {k:s_list.count(k) for k in s_list}
    # kevin_dict = {k:k_list.count(k) for k in k_list}

    #print (kevin_dict, ' ', kevin_score := sum(kevin_dict.values()))
    #print (stewart_dict, ' ', stewart_score := sum(stewart_dict.values()))

    #kevin_score = sum(kevin_dict.values())
    #stewart_score = sum(stewart_dict.values())
    # ^^^^^^^^^^^^^^^^^^^^^^^^^^

    kevin_score = len(k_list)
    stewart_score = len(s_list)

    if kevin_score < stewart_score:
        print (f'Stewart  {stewart_score}')
    elif kevin_score > stewart_score:
        print (f'Kevin  {kevin_score}')
    else:
        print('Draw')


if __name__ == '__main__':
    minion_game(input('Enter a string: ').lower())
