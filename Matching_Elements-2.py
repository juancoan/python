from lxml import html, etree
import requests
from selenium import webdriver


def Interactions():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://learn.letskodeit.com/p/practice")

    Page_Source = driver.page_source
    print("Printing page source to a file.")
    with open("PageSource.txt",'w') as VariableName:  # start using 'with' keybord, variable object at the end 'as Variable name'
      print("Writing to file...")
      VariableName.write(Page_Source)  # same write function


    # Example html content
    html = Page_Source

    # Use etree to process html text and return an _Element object which is a dom object.
    dom = etree.HTML(html)

    # Get a tag's text. Please Note: The _Element's xpath method always return a list of html nodes.Because there is only one a tag's text, so we can do like below.
    a_tag_text = dom.xpath('//legend[contains(text(),"Example")]')

    print(a_tag_text)

Interactions()