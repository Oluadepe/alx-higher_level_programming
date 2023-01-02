#!/usr/bin/python3
"""
takes:
    - a URL 
    - Sends a request to the URL 
    - Displays the body of the response
"""

import sys
from urllib.request import urlopen

def main(url):
    try:
        with urlopen(url) as response:
            body = response.read().decode('utf-8')
            print(body)
    except urllib.error.HTTPError as e:
    print(f'Error code: {e.code}')

if __name__ == '__main__':
  main(sys.argv[1])
