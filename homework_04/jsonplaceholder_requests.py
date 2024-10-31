import aiohttp
from typing import List, Dict

USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"


async def fetch_json(session: aiohttp.ClientSession, url: str) -> List[Dict]:
    async with session.get(url) as resp:
        resp.raise_for_status()
        data = await resp.json()
        return data


async def fetch_users(session: aiohttp.ClientSession) -> List[Dict]:
    users = await fetch_json(session, USERS_DATA_URL)
    print(f"Загружено {len(users)} пользователей.")
    return users


async def fetch_posts(session: aiohttp.ClientSession) -> List[Dict]:
    posts = await fetch_json(session, POSTS_DATA_URL)
    print(f"Загружено {len(posts)} постов.")
    return posts