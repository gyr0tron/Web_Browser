
import requests
import asyncio
import aiohttp

API_ENDPOINT = "http://localhost:5000/login"
# data = {'nm':"http://www.ndtv.com"}

# sending post request and saving response as response object
# r = requests.post(url = API_ENDPOINT, data = data)

# extracting response text 
# res = r.text
# print("The response is: " + res)

# async with session.post('http://localhost:5000/login', data = data) as resp:
#     print(resp.status)
#     print(await resp.text())

async def fetch(data):
  async with aiohttp.request('post', 'http://localhost:5000/login', data = data) as resp:
        print('--------------------Posted----------------------')
        assert resp.status == 200
        print(await resp.text())

if __name__=="__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(fetch())

# r = asyncio.wait_for(aiohttp.request('post', 'http://localhost:5000/login', data = data), 10)
# res = r
# print("The response is: " + res)

