#! python3
# image-site-downlaoder.py - Goes to a Imgur, searches for a category of photos
# and downloads the specified number of photos.

import requests, bs4, os

url = 'https://imgur.com/'

def imageDownloader(query, number_of_photos):
    # Create searched url
    search_url = url + '?q=' + query

    # Create output folder
    os.makedirs(query, exist_ok=True)
    abs_path = os.path.abspath(query)

    # Download and soup the website
    res1 = requests.get(search_url)
    try:
        res1.raise_for_status()
        soup = bs4.BeautifulSoup(res1.text, 'html.parser')

        # Create list of image links
        images = soup.select('.image-list-link img')

        # Max number of images to choose
        num_of_images = min(number_of_photos, len(images))
        img_src = []

        # List of image files from src
        for link in images[:num_of_images]:
            img_src.append(link.get('src'))

        # Download each image
        for image in img_src:
            # Downloads each image src link
            res2 = requests.get(image)
            try:
                res2.raise_for_status()
                image_file = open(os.path.join(query, os.path.basename(image)), 'wb')
                for chunk in res2.iter(100000):
                    image_file.write(chunk)
                image_file.close()
            except Exception:
                print(f'There was a problem {Exception}')

    except Exception:
        print(f'There was a problem {Exception}')


print('Enter a query for images on imgur:')
search = input()
print('Enter a max number of results: ')
num = int(input())

imageDownloader(search, num)
