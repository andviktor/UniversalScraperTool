from bs4 import BeautifulSoup
from lxml import etree

class Soup:
    """BeautifulSoup object operations
    """
    def __init__(self, response):
        """Create a new BeautifulSoup object
        """
        self._soup = BeautifulSoup(response.content, 'html.parser')

    def get_elements(self, xpath):
        """Gets a soup object and xpath param and returns a result
        """
        dom = etree.HTML(str(self._soup))
        return dom.xpath(xpath)