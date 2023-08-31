from html.parser import HTMLParser
import urllib.request


def get_html_from_url(url: str) -> str:
    req = urllib.request.Request(url)

    with urllib.request.urlopen(req) as response:
        page = response.read()

        decoded_page = page.decode('utf-8').replace("\n", "")

        return decoded_page


class CustomHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.big_text = ''
        self.title = ''

    def handle_data(self, data):
        self.big_text += data

    def parse_title(self, data: str):
        if '<title>' in data:
            title = data.split('<title>')[1]
            title = title.split('</title>')[0]
            self.title = title
        elif '<h1>' in data:
            h1 = data.split('<h>')[1]
            h1 = h1.split('</h1>')[0]
            self.title = h1

    def feed(self, data: str) -> None:
        super().feed(data)
        self.parse_title(data)
