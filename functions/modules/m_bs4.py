from bs4 import BeautifulSoup
from lxml import etree

def set_soup(response):
    """Returns a new BeautifulSoup object
    """
    return BeautifulSoup(response.content, 'html.parser')

def get_elements(soup, xpath):
    """Gets a soup object and xpath param and returns a result
    """
    dom = etree.HTML(str(soup))
    return dom.xpath(xpath)
