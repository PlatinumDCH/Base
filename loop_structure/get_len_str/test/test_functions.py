import pytest

from  loop_structure.get_len_str.exeple_method import (
    get_len_for_loop,
    get_len_replace_method,
    get_len_use_sum,
    get_len_use_filter,
    get_len_use_re,
)

@pytest.mark.asyncio
async def test_get_len_for_loop(read_metadata, read_text):

    text = read_text
    expected_len = read_metadata

    result = await get_len_for_loop(text)
    assert result == expected_len

@pytest.mark.asyncio
async def test_get_len_raplace_metod(read_metadata, read_text):
    text = read_text
    expected_len = read_metadata

    result = await get_len_replace_method(text)
    assert result == expected_len

@pytest.mark.asyncio
async def test_get_len_use_sum(read_metadata, read_text):
    text = read_text
    expected_len = read_metadata

    result = await get_len_use_sum(text)
    assert result == expected_len

@pytest.mark.asyncio
async def test_get_len_use_filter(read_metadata, read_text):
    text = read_text
    expected_len = read_metadata

    result = await get_len_use_filter(text)
    assert result == expected_len

@pytest.mark.asyncio
async def test_get_len_use_re(read_metadata, read_text):
    text = read_text
    expected_len = read_metadata

    result = await get_len_use_re(text)
    assert result == expected_len