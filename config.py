redirect: str = 'https://www.shiro.wtf'

class Webserver:
    host: str = '0.0.0.0'
    port: int = 8080


class LastFM:
    api_keys: list[str] = [
        '48033c63480ced8435e6655de38639c7',
    ]
    api_url: str = 'http://ws.audioscrobbler.com/2.0/'
