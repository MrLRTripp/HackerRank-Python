import collections

"""
You are given n words. Some words may repeat. For each word, output its number of occurrences. 
The output order should correspond with the input order of appearance of the word.
Output 2 lines.
On the first line, output the number of distinct words from the input.
On the second line, output the number of occurrences for each distinct word according to their appearance in the input.
"""
# A defaultdict is perfect for this because it initialize a new key by calling int() which will return 0.
# If you didn't use defaultdict you would have to do this before adding 1 to it.
if __name__ == '__main__':
    word_dict = collections.defaultdict(int)
    num_words = int(input('Enter number of words: '))
    for w in range(num_words):
        word = (input('Enter a word: ').lower())
        word_dict[word] += 1

    print(f'Number of distinct words: {len(word_dict)}')
    print(f'Word counts: {" ".join([str(v) for v in word_dict.values()])}')
