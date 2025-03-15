from create_list import languages

languages.insert(2, 'C++')

assert languages == ['Python', 'Java', 'C++','JavaScript']


test_value = 'TestLenguage'
languages.append(test_value)

assert languages == ['Python', 'Java', 'C++','JavaScript', 'TestLenguage']