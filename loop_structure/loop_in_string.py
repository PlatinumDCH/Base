from base import names


exstract_name: str = names[0]


for index, value in enumerate(exstract_name, start=1):
    if index == 1:
        print('start brudfors is {}'.format(exstract_name))

    print('{} - place, {}'.format(index, value))


def get_len_str_without_space(sentense: str):
    len_ = 0
    for x in sentense:
        if x != ' ':
            len_ += 1

def get_len_str(sentense: str):
    return len(sentense.replace(' ',''))

def get_len_str_use_sum(sentense: str):
    """
    not create new string in memory
    efective vork in long sentense
    """
    return sum(1 for char in sentense if char != ' ')

def get_len_str_use_filter(sentense):
    """ Create temporary list"""
    return len(list(filter(lambda x: x!= ' ', sentense)))

def get_len_str_use_re(sentense):
    """Delete all space symvol"""
    import re
    return len(re.suv(r'\s', '', sentense))