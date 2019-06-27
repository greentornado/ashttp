import json

from ashttp import *


def test_ashttp():
    import asyncio

    async def main():
        r = await get('https://httpbin.org/get')
        assert await r.json()
        r = await post('https://httpbin.org/post', data=json.dumps({"a": 1}))
        assert await r.json()
        r = await put('https://httpbin.org/put', data=json.dumps({"a": 1}))
        assert await r.json()
        r = await patch('https://httpbin.org/patch', data=json.dumps({"a": 1}))
        assert await r.json()
        r = await delete('https://httpbin.org/delete')
        assert await r.json()
        r = await option('https://httpbin.org/option')
        assert await r.json()

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
