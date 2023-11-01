import multiprocessing
import os
from pathlib import Path
import requests
import time

urls = [
        'http://nakompe.ru/wp-content/uploads/2020/02/pp_image_58968_q5ncrmul4t12BD0BAD180D0B0D181D0B8D0B2D18BD0B52BD184D0BED182D0BE.jpg',
        'http://vsegda-pomnim.com/uploads/posts/2022-04/1650920851_26-vsegda-pomnim-com-p-gori-putorana-foto-26.jpg'
        ]

def get_url(url):
    start_time = time.time()
    image_path = Path('./picture')
    response = requests.get(url)
    response = requests.get(url, stream=True)
    filename = image_path.joinpath(os.path.basename(url))
    with open(filename, "wb") as f:
        for i in response.iter_content():
            f.write(i)
    end_time = time.time() - start_time
    print(f'Cкачано {filename} за {end_time:.2f} секунд')


if __name__ == "__main__":
    start_time = time.time()
    proces = []
    for url in urls:
        t = multiprocessing.Process(target=get_url, args=(url,))
        proces.append(t)
        t.start()

    for i in proces:
        i.join()
    end_time = time.time() - start_time
    print(f'Время работы программы: {end_time:.2f} секунд')
