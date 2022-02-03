"""Template robot with Python."""


# def minimal_task():
#     print("Done.")


# if __name__ == "__main__":
#     minimal_task()

from re import search
from RPA.Browser.Selenium import Selenium
# from RPA.FileSystem import FileSystem
# from RPA.Excel.Application import Application

import time

browser = Selenium()

# app = Application()


def open_the_website(url):
    browser.open_available_browser(url)

    
    # FileSystem().create_file("output/text.txt", text_1, overwrite=True)

    #TODO find text all elements (name company, money company) and save to exel

# Click element "DIVE IN"
def open_list_agencies():
    # pass
    
    browser.click_element("class:btn.btn-default.btn-lg-2x.trend_sans_oneregular")

list_anme_money = []
#Search block with name and money Agencies
def search_block_agencies():
    dict_name_money = {}

    # pass
    block_agency = browser.find_elements("id:agency-tiles-widget")
    # print(len(block_agency))

    # for item in block_agency:

    #     item = block_agency

    for elements in block_agency:
        name_agencies = browser.find_elements('class:h4.w200', elements)
        # print(name_agencies)

        money_agencies = browser.find_elements('class:h1.w900', elements)
        
        for text1 in name_agencies:
            text_name = browser.get_text(text1)
            print(text_name)
            # dict_name_money['Name agency'] = text_name

        for text2 in money_agencies:
            text_money = browser.get_text(text2)
            print(text_money)
            # dict_name_money['Money agency'] = text_money


        #     print(dict_name_money)

        

            



        

    # list_anme_money.append(dict_name_money)

    # print(dict_name_money)

    # return list_anme_money


# Get element with name agencies
def get_text_agencies(elements):
    pass



def save_to_xlsx():
    pass
    # app.open_application()
    # app.open_workbook('workbook.xlsx')
    # app.set_active_worksheet(sheetname='new stuff')
    # app.write_to_cells(row=1, column=1, value='new data')
    # app.save_excel()
    # app.quit_application()



def main():
    try:
        open_the_website("https://itdashboard.gov/")
        open_list_agencies()
        time.sleep(5)

        search_block_agencies()
        time.sleep(5)
        print('done')


        # get_text_agencies(elements=search)

        save_to_xlsx()
    finally:
        browser.close_browser()


if __name__ == "__main__":
    main()
