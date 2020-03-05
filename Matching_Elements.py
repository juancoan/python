from lxml import html
import requests

def MatchingElements(MyUrl):
    page = requests.get(MyUrl)
    tree = html.fromstring(page.content)

    #This will create a list of buyers:
    buyers = tree.xpath('//div[@title="buyer-name"]/text()')
    #This will create a list of prices
    prices = tree.xpath('//span[@class="item-price"]/text()')

    print ('Buyers: ', buyers)
    print ('Prices: ', prices)

    String2Look = "Moe"
    Count = 0
    for strings in buyers:

        Splitted= strings.split()
        # print(Splitted)
        for lines in Splitted:
            NewSplit = lines.split(",")
            #print(NewSplit)
            if String2Look in NewSplit:
                 Count +=1
    print("String ", String2Look, " was found ", Count, " times.")

MatchingElements(MyUrl='http://econpy.pythonanywhere.com/ex/001.html')

