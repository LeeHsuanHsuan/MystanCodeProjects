"""
File: anagram.py
Name: Lee Hsuan Hsuan
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop
dict_list = []


def main():
    """
    TODO:
    """
    ####################
    # read all words to dict_list
    read_dictionary()
    while True:
        print('Welcome to stanCode "Anagram Generator" (or -1 to quit)')
        s = input('Find anagrams for: ')
        # while s equals EXIT break the loop
        if s == EXIT:
            break
        else:
            start = time.time()
            find_anagrams(s)
            end = time.time()
    ####################
    print('----------------------------------')
    print(f'The speed of your anagram algorithm: {end-start} seconds.')


def read_dictionary():
    """
    :return: read the words to the global value dict_list
    """
    with open(FILE, 'r') as f:
        for line in f:
            # split all the space and \n
            line = line.split('\n')[0]
            # append the word to the list
            dict_list.append(line)


def find_anagrams(s):
    """
    :param s:str, user want to search for anagram
    :return:the result of the anagram and print all of them
    """
    # call the helper function with empty string and empty lst
    lst = find_anagrams_helper(s, "", [])
    ana_num = len(lst)
    print(f'{ana_num} anagrams: {lst}')


def find_anagrams_helper(s, cur_s, lst):
    # if the length of current string equals the string means the BaseCase.
    if len(s) == len(cur_s):
        # if the current string in the dict_list print it out
        if cur_s in dict_list and cur_s not in lst:
            print(f'Found: {cur_s}')
            print('Searching...')
            lst.append(cur_s)
    else:
        # i means the character in the string, and append it to the current string
        for i in s:
            # if i already in the current string no need to add
            if s.count(i) == cur_s.count(i):
                pass
            # if not current string add i
            else:
                # Choose
                cur_s += i
                # Explore
                if has_prefix(cur_s) is True:
                    find_anagrams_helper(s, cur_s, lst)
                # Un-choose
                cur_s = cur_s[:len(cur_s)-1]
    return lst


def has_prefix(sub_s):
    """
    :param sub_s:the string have to find in the dictionary
    :return: bool, if it start with the sub_s, return True
    """
    for s in dict_list:
        if s.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()
