def merge_the_tools(string, k):
    # Since k is an integer factor of string length, then split the string into substrings of length k
    sub_str_list = [string[i:i+k] for i in range(0,len(string),k)]

    for s in sub_str_list:
        # Only want to keep the first occurrance of a char, so if it is not in the set of char already,  
        # then add it, else skip
        #u = ''.join([c for i,c in enumerate(s) if c not in set(s[0:i])])
        #print(u)

        # Another interesting way to do this is to use a dictionary comprehension and
        # put the chars as the keys (the value doesn't matter) and then join the keys.
        # Starting with Python 3.7, insertion order is preserved
        u = ''.join({c:i for i,c in enumerate(s)}.keys())
        print(u)

if __name__ == '__main__':
    string, k = input('Enter a string and an integer factor of string length:').split()
    merge_the_tools(string, int(k))