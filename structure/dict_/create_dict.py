my_dict: dict[str, str|int] = {'name': 'test', 'age':12}

def get_value_dict(dict_):
    name = dict_.get('name')
    age = dict_.get('age')

    assert name == 'test'
    assert age == 12

# get_value_dict(my_dict)