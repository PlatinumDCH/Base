import re
from loop_structure.get_len_str.utils.time_decor import time_it


@time_it
async def get_len_for_loop(sentense: str):
    """
    Count the number if char excluding spaces.
    """
    len_ = 0
    for x in sentense:
        if x != ' ':
            len_ += 1
    
    return len_

@time_it
async def get_len_replace_method(sentense: str):
    """
    Return copy, when all char-spaces replaceed.
    """
    return len(sentense.replace(' ',''))

@time_it
async def get_len_use_sum(sentense: str):
    """
    Not create new string in memory
    efective vork in long sentense
    """
    return sum(1 for char in sentense if char != ' ')

@time_it
async def get_len_use_filter(sentense):
    """ Create temporary list"""
    return len(list(filter(lambda x: x!= ' ', sentense)))

@time_it
async def get_len_use_re(sentense):
    """Delete all space symvol"""
    return len(re.sub(r'\s', '', sentense))