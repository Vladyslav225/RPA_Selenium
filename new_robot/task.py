"""Template robot with Python."""


# def minimal_task():
#     print("Done.")


# if __name__ == "__main__":
#     minimal_task()

from re import search
from RPA.Browser.Selenium import Selenium
# from RPA.FileSystem import FileSystem
# from RPA.Excel.Application import Application
from RPA.PDF import PDF

import time
from openpyxl import Workbook

browser = Selenium()


list_name = []
list_money = []


# app = Application()


def open_the_website(url):
    browser.open_available_browser(url)

    
    # FileSystem().create_file("output/text.txt", text_1, overwrite=True)

    #TODO Save to exel

# Click element "DIVE IN"
def open_list_agencies():
    # pass
    
    browser.click_element("class:btn.btn-default.btn-lg-2x.trend_sans_oneregular")

#Search block with name and money Agencies
def search_block_agencies():
    

    # pass
    block_agency = browser.find_elements("id:agency-tiles-widget")
    # print(len(block_agency))


    for elements in block_agency:
        name_agencies = browser.find_elements('class:h4.w200', elements)
        # print(name_agencies)

        money_agencies = browser.find_elements('class:h1.w900', elements)
        
        for name in name_agencies:
            text_name = browser.get_text(name)
            # print(text_name)

            list_name.append(text_name)

        for money in money_agencies:
            text_money = browser.get_text(money)
            # print(text_money)

            list_money.append(text_money)

    return list_name, list_money



def save_to_xlsx(list_name_and_money):
    wb = Workbook()
    book = wb.active

    for item in list_name_and_money:

        for i in item:

            book['A1'] = i

            book.append([1, 2, 3])

            wb.save('output/file.xlsx')




def main():
    try:
        open_the_website("https://itdashboard.gov/")
        open_list_agencies()
        time.sleep(5)

        list_name_and_money = search_block_agencies()
        # print(list_name_and_money)

        time.sleep(5)

        # get_text_agencies(elements=list_name_and_money)

        save_to_xlsx(list_name_and_money)
        # print('done')
        
    finally:
        browser.close_browser()


if __name__ == "__main__":
    main()
