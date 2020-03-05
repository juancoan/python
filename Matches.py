# 1st parameter is url string
# 2nd parameter xpath (search parameter)
# 3nd parameter string
# make selenium driver with url
# loop through all values in 2nd parameter, add entire html statement to list,
# so we have a list of all html statements matching the 2nd parameter
# loop through this list and return html statements that match the 3rd parameter string
# return list of html statements matching xpath and string, 2 levels of filtering



from lxml import etree #library to parse info from html using xpath
import requests

def MatchingElementsOther():
    URL = "http://www.dlib.org/dlib/november14/beel/11beel.html"
    page = requests.get(URL)
    tree = etree.HTML(page.text) #Setting up element tree, returning HTML content or the element
    element = tree.xpath('./body/form/table[3]/tr/td/table[5]') #list of selected elements, 1.
    content = etree.tostring(element[0]) #accesing the 1st element to obtaing the HTML content
    print(content)

    #creating a variable to look for the param specified inside the html content variable
    BitsFound = content.find(b'td') #since it is a byte obj, the param I am looking for is a b type as well
    if BitsFound:
        print("found")
MatchingElementsOther()