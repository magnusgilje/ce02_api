import requests
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self,url:str):
        self.url = url

    def scrape_site(self):
        page = requests.get(self.url)
        if page.status_code == 200:
            soup = BeautifulSoup(page.content, 'html.parser')
            for script_or_style in soup(["script", "style"]):
                script_or_style.extract()
            text = soup.get_text()
            return {' '.join(text.split())}
    if __name__ == "__main__":
        scrape_site()