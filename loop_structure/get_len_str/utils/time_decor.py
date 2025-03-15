import time
from pathlib import Path


path_to_log_file = Path(__file__).parent.parent / 'time.log'


def time_it(func):
    """Decorator to time chacker executed function"""
    async def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = await func(*args, **kwargs)
        end_time = time.perf_counter()


       #TODO: if use async with aiofiles, not record to time.log
       #TODO: if use logger, dont recoed to time.log
        with open(path_to_log_file, 'a') as f:
            f.write(f"{func.__name__} executed: {end_time - start_time:.6f} sec\n"
                    )
        return result
    
    return wrapper