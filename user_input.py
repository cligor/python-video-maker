def run():
	content = {}
	content['searchTerm'] = askSearchTerm()

	print(content)
	
def askSearchTerm():
	return input('Type what you want search: ')
