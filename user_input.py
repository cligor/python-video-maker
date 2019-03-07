def get_content_search_term():
	return input('What do you want make a video? ')

def get_content_search_prefix():
	prefixes = ['Who is ', 'What is ', 'The history of ']


	print('\nChoose a prefix: ')

	index = 1
	for prefix in prefixes:
		print('{}: {}' .format(index, prefix))
		index += 1

	choice = int(input())

	return prefixes[choice - 1]
