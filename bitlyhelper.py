import json
from urllib.request import urlopen
from config import TOKEN

ROOT_URL = "https://api-ssl.bitly.com"
SHORTEN = "/v4/shorten?access_token={}&longUrl={}"
DOMAIN = "bit.ly"


class BitlyHelper:

    def shorten_url(self, longurl):
        try:
            url = ROOT_URL + SHORTEN.format(TOKEN, longurl)
            response = urlopen(url).read()
            jr = json.loads(response)
            return jr['data']['url']
        except Exception as e:
            print(e)
