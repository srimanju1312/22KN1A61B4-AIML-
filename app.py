import requests
def shorten_url(long_url):
    api_url = 'https://nokkufy.com/api/shorten'
    data = {
        'url': long_url
    }
    response = requests.post(api_url, json=data)
    if response.status_code == 200:
        result = response.json()
        return result.get('short_url')
    else:
        print("Failed to shorten URL:", response.text)
        return None
long_url = 'https://example.com/some/very/long/url'
short_url = short_url(long_url)
if short_url:
    print("Shortened URL:",short_url)
else:
    print("Could not shorten the URL:", long_url)