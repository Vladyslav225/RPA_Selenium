"""Template robot with Python."""


from RPA.Browser.Selenium import Selenium

from RPA.PDF import PDF

# I use openpyxl, because library "RPA.Excel.Application" work with Windows.
# I use Ubuntu.
from openpyxl import Workbook
import time

browser = Selenium()



list_name = []
list_money = []


def open_the_website(url):
    try:
        browser.open_available_browser(url)

    except:
        print('Check the correctness of the input URL')

# Click element "DIVE IN"
def open_list_agencies():
    try:
        browser.click_element("class:btn.btn-default.btn-lg-2x.trend_sans_oneregular")

    except Exception as ex:
        print(ex)

#Get text name and money Agencies
def search_block_agencies():
    try:
        block_agency = browser.find_elements("id:agency-tiles-widget")

    except Exception as ex:
        print(ex)

    for elements in block_agency:
        name_agencies = browser.find_elements('class:h4.w200', elements)

        money_agencies = browser.find_elements('class:h1.w900', elements)

        for name in name_agencies:
            text_name = browser.get_text(name)
            list_name.append(text_name)

        for money in money_agencies:
            text_money = browser.get_text(money)
            list_money.append(text_money)

    return list_name, list_money

# Saving to Exel information about Agencies
def save_to_xlsx(filename):

    wb = Workbook()
    book = wb.active
    book.title= 'Agencies'
    
    book['A1'] = 'Name companies'
    book['B1'] = 'Money companies'

    r = 2
    for name in list_name:
        book.cell(row=r, column=1).value = name
        r += 1

    r = 2
    for money in list_money:
        book.cell(row=r, column=2).value = money
        r += 1

    wb.save(filename=filename)
    wb.close()




def main():
    try:
        open_the_website("https://itdashboard.gov/")
        open_list_agencies()
        time.sleep(5)
        search_block_agencies()
        time.sleep(5)
        save_to_xlsx('output/file.xlsx')
        
    finally:
        browser.close_browser()


if __name__ == "__main__":
    main()
