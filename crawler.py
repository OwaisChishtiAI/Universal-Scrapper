import bs4 as bs
import sys
import urllib.request
from PyQt5.QtWebEngineWidgets import QWebEnginePage
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl
import pandas as pd
 
app = QApplication(sys.argv)

class VirtualBrowser(QWebEnginePage):
    def __init__(self, url):
        self.app = app
        QWebEnginePage.__init__(self)
        self.html = ''
        self.loadFinished.connect(self._on_load_finished)
        self.load(QUrl(url))
        self.app.exec_()

    def _on_load_finished(self):
        self.html = self.toHtml(self.Callable)
        print('[INFO] Scrape Finish.')

    def Callable(self, html_str):
        self.html = html_str
        self.app.quit()


class Crawler:
    def __init__(self):
        self.strings = []
        self.doc = None
        self.soup = None
        self.tables = None

    def set_url(self, doc):
        self.doc = doc

    def clean_text(self, data):
        li = []
        data = data.split("\n")
        for e in data:
            if e:
                e = e.encode('ascii',errors='ignore').decode().replace("\t", "").strip()
                if e:
                    li.append(e)
        return li

    def scrape_text(self):
        print("[INFO] Fetching...")
        try:
            page = VirtualBrowser(self.doc)
            soup = bs.BeautifulSoup(page.html, 'html.parser')
            self.soup = soup
            body = soup.body
            return self.clean_text(body.text)
        except Exception as e:
            print("[scrap_text EXCEPTION] ", str(e))
        

    def scrape_tables(self):
        print("[INFO] Fetching Tables...")
        try:
            tbs = self.soup.find_all('table')
            df = pd.read_html(str(tbs))
            print("[INFO] Fetching Completed.")
            if df:
                return df
        except Exception as e:
            print("[scrap_tables EXCEPTION] ", str(e))

    def scrape_media(self):
        print("[INFO] Fetching Media.")
        try:
            images = []
            videos = []
            img_tags = self.soup.find_all('img')
            video_tags = self.soup.find_all('video')
            for each in img_tags:
                images.append(each["src"])
            for each in video_tags:
                videos.append(each["src"])
            return images, videos
        except Exception as e:
            print("[scrape_media EXCEPTION] ", str(e))


#https://pythonprogramming.net/parsememcparseface/
#https://finance.yahoo.com/quote/%5EGSPC/history?p=%5EGSPC