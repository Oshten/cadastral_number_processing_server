import time
import random
import asyncio


async def imitation_send_query(data: dict) -> dict:
    """Имитирует асинхронный запос к внешнему серверу посредствам библиотеки aiohttp"""
    timeout = random.randint(10, 60)
    print(timeout)
    result = await asyncio.sleep(timeout, result={'calculated': True, 'timeout': timeout, 'id': data.get('id')})
    print(result)
    return result

