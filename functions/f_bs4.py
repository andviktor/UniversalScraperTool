from bs4 import BeautifulSoup
from lxml import etree

def set_soup(response):
    return BeautifulSoup(response.content, 'html.parser')

def get_elements(soup, xpath):
    dom = etree.HTML(str(soup))
    return dom.xpath(xpath)
