from user_input import *

content_to_search = {}

content_to_search['search_term'] = get_content_search_term()
content_to_search['search_prefix'] = get_content_search_prefix()

print(content_to_search)
