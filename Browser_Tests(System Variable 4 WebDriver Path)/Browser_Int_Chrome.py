from selenium import webdriver

class BrowserInteractions():
    def Interactions(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://learn.letskodeit.com/p/practice")

        titulo = driver.title
        print("Page title is: ", titulo)

        Actual_Page = driver.current_url
        print("Current URL is: ", Actual_Page)

        driver.refresh()
        print("Page has been refreshed...")

        driver.get(driver.current_url)
        print("Page has been refreshed...a SECOND time.")

        driver.get("https://learn.letskodeit.com/")
        New_Page = driver.current_url
        print("A new page has been opened. ")
        print("Current URL is: ", New_Page)

        driver.back()
        print("Going back.")

        driver.forward()
        print("Going forward.")

        Page_Source = driver.page_source
        print("Printing page source to a file.")
        with open("PageSource.txt",'w') as VariableName:  # start using 'with' keybord, variable object at the end 'as Variable name'
            print("Writing to file...")
            VariableName.write(Page_Source)  # same write function

Chr = BrowserInteractions()
Chr.Interactions()