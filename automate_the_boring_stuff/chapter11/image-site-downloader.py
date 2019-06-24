#! python3
# image-site-downlaoder.py - Goes to a Imgur, searches for a category of photos
# and downloads the specified number of photos.

import requests, bs4, os

url = 'https://imgur.com/'

def imageDownloader(keyword, number_of_photos):
    