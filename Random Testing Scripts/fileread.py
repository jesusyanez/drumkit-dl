import requests
from bs4 import BeautifulSoup

def main():
    r = requests.get('https://drive.google.com/file/d/10SRO70nAtaLKu7ehMJ8yy4zK811H3ubR/view?usp=sharing')
    soup = BeautifulSoup(r.content, features="lxml")

    title = soup.title.string
    title = title[:-15]
    print (title)


if __name__ == '__main__':
    main()