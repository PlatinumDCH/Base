condition = True


def foo():
    if condition:
        return True
    else:
        return False


def bar():
    my_dict = {'age':1}

    if my_dict['age'] >=1:
        return True
    else:
        return False

def baz():
    stable_value = 3
    if stable_value == 3:
        return 'stable value is'.format(stable_value)
    elif stable_value == 2:
        return 'stable value is'.format(stable_value)
    else:
        return 'stable value is'.format(stable_value)