import asyncio
import time

from loop_structure.get_len_str.utils.logger import logger
from loop_structure.get_len_str.utils.time_decor import time_it


@time_it
async def foo():
    time.sleep(3)

async def main():
    await foo()

asyncio.run(main())