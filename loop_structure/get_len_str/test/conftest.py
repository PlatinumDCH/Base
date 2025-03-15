import json
import aiofiles
import pytest_asyncio


from loop_structure.get_len_str.settings import config


@pytest_asyncio.fixture(scope="session")
async def read_metadata():
    """
    Read metadata file onse
    """
    print('Call {}'.format(read_metadata.__name__))

    async with aiofiles.open(config.META_FILE, 'r') as metadate_file:
        metadata = json.loads(await metadate_file.read())
    return metadata['len_text_without_space']


@pytest_asyncio.fixture(scope="session")
async def read_text():
    """
    Read content file onse
    """
    print('Call {}'.format(read_text.__name__))

    async with aiofiles.open(config.FILE_NAME, 'r', encoding='utf-8') as file:
        return await file.read()

