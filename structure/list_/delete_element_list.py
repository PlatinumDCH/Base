from insert_value_in_list import languages, test_value


languages.remove(test_value)

assert languages == ['Python', 'Java', 'C++','JavaScript']