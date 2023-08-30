import requests


def search_gif(search_term):
    
    api_key = 'gOoqPUNQINVpuioUVdzWyCesJWPeV4fk'

    url = f'https://api.giphy.com/v1/gifs/search?q={search_term}&api_key={api_key}&limit=5'

    resp = requests.get(url)
    data = resp.json()
    gifs = data['data']
    if not gifs:
            print("There are no GIFs for this request")
    else:
        for gif in gifs:
            print(gif['url'])
search_term = input("Enter a word to search for GIF images:")
search_gif(search_term)