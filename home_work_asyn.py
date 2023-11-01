import os
from pathlib import Path
import time
import aiohttp
import asyncio
 
async def download_image(session, url):
    start_time = time.time()
    image_path = Path('./picture')
    filename = image_path.joinpath(os.path.basename(url))
    async with session.get(url) as response:
        data = await response.read()
        with open(filename, "wb") as file:
            file.write(data)
        end_time = time.time() - start_time
        print(f'Cкачано {filename} за {end_time:.2f} секунд')
 
async def main():
    async with aiohttp.ClientSession() as session:
        urls = [
        'http://nakompe.ru/wp-content/uploads/2020/02/pp_image_58968_q5ncrmul4t12BD0BAD180D0B0D181D0B8D0B2D18BD0B52BD184D0BED182D0BE.jpg',
        'http://vsegda-pomnim.com/uploads/posts/2022-04/1650920851_26-vsegda-pomnim-com-p-gori-putorana-foto-26.jpg'
        ]
 
        tasks = []
        for url in urls:
            task = asyncio.create_task(download_image(session, url))
            tasks.append(task)
        await asyncio.gather(*tasks)

if __name__ == '__main__':
    start_time = time.time()
    asyncio.run(main())
    end_time = time.time() - start_time
    print(f'Программа работала {end_time:.2f} секунд')