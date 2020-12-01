import requests
from lxml.html import fromstring
from cachetools import cached, TTLCache

TTL_7HRS = TTLCache(maxsize=2, ttl=25200)


class Auth:
    def __init__(self, api_key):
        self._api_key = api_key

    @cached(TTL_7HRS)
    def get_single_use_service_ticket(self):
        url = 'https://utslogin.nlm.nih.gov/cas/v1/api-key'
        headers = {
            'Content-type': 'application/x-www-form-urlencoded',
            'Accept': 'text/plain',
            'User-Agent': 'python'
        }
        resp = requests.post(
            url, data={'apikey': self._api_key}, headers=headers
        )
        resp.raise_for_status()
        html = fromstring(resp.text)
        ticket_granting_ticket_url = html.xpath('//form/@action')[0]

        resp = requests.post(
            ticket_granting_ticket_url,
            data={'service': 'http://umlsks.nlm.nih.gov'},
            headers=headers
        )
        resp.raise_for_status()
        single_use_service_ticket = resp.text
        return single_use_service_ticket


class API:
    BASE_URL = 'https://uts-ws.nlm.nih.gov/rest'

    def __init__(self, *, api_key, version='current'):
        self._auth = Auth(api_key=api_key)
        self._version = version

    def get_cui(self, cui):
        url = f'{self.BASE_URL}/content/{self._version}/CUI/{cui}'
        return self._get(url=url)

    def get_tui(self, tui):
        url = (f'{self.BASE_URL}/semantic-network/{self._version}/TUI/{tui}')
        return self._get(url=url)

    def _get(self, url):
        ticket = self._auth.get_single_use_service_ticket()
        resp = requests.get(url, params={'ticket': ticket})
        resp.raise_for_status()
        return resp.json()
