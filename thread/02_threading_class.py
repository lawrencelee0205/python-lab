from threading import Thread
import urllib.request

class HttpRequestThread(Thread):
    def __init__(self, url):
        super().__init__()
        self.url = url
        self.http_status_code = None
        self.reason = None

    def run(self) -> None:
        print(f'Checking {self.url} ...')
        try:
            response = urllib.request.urlopen(self.url)
            self.http_status_code = response.code
        except urllib.error.HTTPError as e:
            self.http_status_code = e.code
        except urllib.error.URLError as e:
            self.reason = e.reason        

def main() -> None:
    urls = [
        'https://httpstat.us/200',
        'https://httpstat.us/400'
    ]

    threads = [HttpRequestThread(url) for url in urls]

    [t.start() for t in threads]

    [t.join() for t in threads]

    [print(f'{t.url}: {t.http_status_code}') for t in threads]

if __name__ == '__main__':
    main()