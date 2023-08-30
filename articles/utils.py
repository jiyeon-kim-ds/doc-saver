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

    def handle_data(self, data: str):
        self.big_text += data
