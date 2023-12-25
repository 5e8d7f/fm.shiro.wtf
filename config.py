class Webserver:
    host: str = '0.0.0.0'
    port: int = 8080


class LastFM:
    api_keys: list[str] = [
        'b25b959554ed76058ac220b7b2e0a026',
        '58a7d4a1c6b5b4b0f6f2e6f5e8f5d1c4',
    ]
    api_url: str = 'http://ws.audioscrobbler.com/2.0/'
