"""Template robot with Python."""


# def minimal_task():
#     print("Done.")


# if __name__ == "__main__":
#     minimal_task()

from re import search
from turtle import title
from RPA.Browser.Selenium import Selenium
# from RPA.FileSystem import FileSystem
# from RPA.Excel.Application import Application
from RPA.PDF import PDF

from openpyxl import Workbook
import time

browser = Selenium()

# app = Application()

list_name = []
list_money = []


def open_the_website(url):
    browser.open_available_browser(url)

    
    # FileSystem().create_file("output/text.txt", text_1, overwrite=True)

    #TODO Save to exel

# Click element "DIVE IN"
def open_list_agencies():
    browser.click_element("class:btn.btn-default.btn-lg-2x.trend_sans_oneregular")

#Get text name and money Agencies
def search_block_agencies():
    block_agency = browser.find_elements("id:agency-tiles-widget")


    for elements in block_agency:
        name_agencies = browser.find_elements('class:h4.w200', elements)

        money_agencies = browser.find_elements('class:h1.w900', elements)
        # print(money_agencies)

        for name in name_agencies:
            text_name = browser.get_text(name)
            list_name.append(text_name)

        for money in money_agencies:
            text_money = browser.get_text(money)
            list_money.append(text_money)

    return list_name, list_money



def save_to_xlsx():

    wb = Workbook()
    book = wb.active
    book.title= 'Agencies'
    
    book['A1'] = 'Name companies'
    book['B1'] = 'Money companies'

    r = 2
    for statN in list_name:
        book.cell(row=r, column=1).value = statN
        r += 1

    r = 2
    for statN in list_money:
        book.cell(row=r, column=2).value = statN
        r += 1

    print('done')

    wb.save('output/file.xlsx')
    wb.close()




def main():
    try:
        open_the_website("https://itdashboard.gov/")
        open_list_agencies()
        time.sleep(5)
        info = search_block_agencies()
        # print(info)
        time.sleep(5)
        save_to_xlsx()
        # print('done')
        
    finally:
        browser.close_browser()


if __name__ == "__main__":
    main()
