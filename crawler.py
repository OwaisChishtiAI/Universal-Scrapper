import requests
from bs4 import BeautifulSoup
 
class Crawler:
    def __init__(self):
        self.strings = []

    def scrap_text(self, doc):
        print("Fetching...")
        # getting response object
        res = requests.get(doc)
        
        # Initialize the object with the document
        soup = BeautifulSoup(res.content, "html.parser")
        
        # Get the whole body tag
        tag = soup.body
        
        # Print each string recursively
        for string in tag.strings:
            self.strings.append(string)
        print("Fetching Completed.")
        return self.strings