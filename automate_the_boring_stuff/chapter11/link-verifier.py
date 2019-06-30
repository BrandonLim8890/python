#!python3
# link-verifier.py - Verifies all links on a webpage

import requests, bs4

def linkVerifier(url):
    res = requests.get(url)
    try:
        res.raise_for_status()

        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        link_elem = soup.select('a')

        good_counter = 0
        bad_counter = 0

        links_to_test = []

        for elem in link_elem:
            if elem.get('href') and elem.get('href').startswith('http'):
                links_to_test.append(elem.get('href'))
        
        for link in links_to_test:
            res2 = requests.get(link)
            try:
                res.raise_for_status()
                print(f'Good link: {link}')
                good_counter += 1
            except Exception:
                print(f'Bad link: {link}')
                bad_counter += 1
        print(f'Good links: {good_counter}\nBad links: {bad_counter}\nTotal #: {len(links_to_test)}')

    except Exception:
        print(f'Something went wrong: {Exception}')


linkVerifier('https://automatetheboringstuff.com/chapter11/')