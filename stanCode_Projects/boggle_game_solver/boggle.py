"""
File: boggle.py
Name: Lee Hsuan Hsuan
----------------------------------------
TODO:
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'
dict_list = []
find_list = []


def main():
	"""
	Boggle Game - print out the words in sequences of adjacent letters.
	"""
	start = time.time()
	####################
	boggle_dict = {}
	# User input 4 rows of letters 4*4
	row_1 = input('1 row of letters: ')
	if len(row_1) > 7:
		print("Illegal Input.")
	else:
		row_1 = row_1.lower()
		boggle_dict['0'] = row_1.split()
		row_2 = input('2 row of letters: ')
		if len(row_2) > 7:
			print("Illegal Input.")
		else:
			row_2 = row_2.lower()
			boggle_dict['1'] = row_2.split()
			row_3 = input('3 row of letters: ')
			if len(row_3) > 7:
				print("Illegal Input.")
			else:
				row_3 = row_3.lower()
				boggle_dict['2'] = row_3.split()
				row_4 = input('4 row of letters: ')
				if len(row_4) > 7:
					print("Illegal Input.")
				else:
					row_4 = row_4.lower()
					boggle_dict['3'] = row_4.split()
					read_dictionary()
					find_anagram(boggle_dict)
	print(f'There are {len(find_list)} words in total.')

	####################
	end = time.time()
	print('----------------------------------')
	print(f'The speed of your boggle algorithm: {end - start} seconds.')


def find_anagram(boggle_dict):
	"""
	:param boggle_dict: boogle_dict is the letters user input
	:return: None
	"""
	# append the (row, col , letter) as a tuple to a list
	lst = []
	# key is the row of the letter
	for key in boggle_dict.keys():
		count = 0
		# count is the column of the letter
		for value in boggle_dict[key]:
			char = (int(key), count, value)
			lst.append(char)
			count += 1
	# add the first character to the string
	for first_tuple in lst:
		string = ''
		string += first_tuple[2]
		insert_index = lst.index(first_tuple)
		# remove the first character from the list
		lst.remove(first_tuple)
		find_anagram_helper(boggle_dict, string, lst, first_tuple)
		lst.insert(insert_index, first_tuple)


def find_anagram_helper(boggle_dict, cur_s, lst, i):
	"""
	:param boggle_dict: boogle_dict is the letters user input
	:param cur_s: current string which would be start at least one character
	:param lst: the list with the tuple(row, col, letter) have to add
	:param i: tuple with (row, col, letter)
	:return: None
	"""
	# if current string is in the dictionary then print it out
	if cur_s in dict_list and cur_s not in find_list:
		find_list.append(cur_s)
		print(f'Found "{cur_s}"')
	# Base Case
	if lst is None:
		pass
	else:
		min_row = i[0] - 1
		max_row = i[0] + 1
		min_col = i[1] - 1
		max_col = i[1] + 1
		# Choose the neighbor
		for new_i in lst:
			if min_row <= new_i[0] <= max_row and min_col <= new_i[1] <= max_col:
				cur_s += new_i[2]
				if has_prefix(cur_s):
					new_i_index = lst.index(new_i)
					lst.remove(new_i)
					# explore
					find_anagram_helper(boggle_dict, cur_s, lst, new_i)
					# Un-Choose
					lst.insert(new_i_index, new_i)
					cur_s = cur_s[:len(cur_s)-1]
				else:
					# Un-Choose
					cur_s = cur_s[:len(cur_s)-1]


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	# only read the words at least with 4 letters.
	with open(FILE, 'r') as f:
		for line in f:
			line = line.split('\n')[0]
			if len(line) >= 4:
				dict_list.append(line)


def has_prefix(sub_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for s in dict_list:
		if s.startswith(sub_s):
			return True
	return False


if __name__ == '__main__':
	main()
