import aiofiles

from loop_structure.get_len_str.settings import config



async def read_file():
    async with aiofiles.open(config.FILE_NAME, mode='r') as f:
        content = await f.read()
    
    return content
