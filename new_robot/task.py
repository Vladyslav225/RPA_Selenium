"""Template robot with Python."""


from RPA.Browser.Selenium import Selenium
from RPA.PDF import PDF

# I use openpyxl, because library "RPA.Excel.Application" work with Windows.
# I use Ubuntu.
from openpyxl import Workbook
import openpyxl
from openpyxl.writer.excel import save_workbook
import time

# app
from app.finder_agency import get_element

browser = Selenium()


# List Name and Spanding Agencies from Start page
name_spending_agency = []




# Open the start page of the web-site
def open_website(url):
    try:
        browser.open_available_browser(url)

    except Exception as ex:
        print(ex)


# Open all agency, click element 'DIVE IN'
def open_agency():
    try:
        browser.click_element('class:btn.btn-default.btn-lg-2x.trend_sans_oneregular')

    except Exception as ex:
        print(ex)


# General block Name and Spending Agencies
def general_block_agencies():
    try:
        return browser.find_element('id:agency-tiles-widget')

    except Exception as ex:
        print(ex)


# Name and Spending Agencies
def informatin_agencies(get_text):
    name_agency = []
    spending_agency = []

    # Name Agencies
    try:
        element_name_agency = browser.find_elements('class:h4.w200', get_text)
    except Exception as ex:
        print(ex)

    for text_name in element_name_agency:
        name_agency.append(browser.get_text(text_name))

    # Spanding Agencies
    try:
        element_spending_agency = browser.find_elements('class:h1.w900', get_text)
    except Exception as ex:
        print(ex)

    for text_spending in element_spending_agency:
        spending_agency.append(browser.get_text(text_spending))

    name_spending_agency.append(
        {
            'Name Agency':name_agency,
            'Spending Agency':spending_agency,
        }
    )

    print('DONE, informatin_agencies')


# Select one Agency
def open_page_agency(url_agencies):
    name_agency = 'National Science Foundation'

    for element in name_spending_agency:
        find_element = element['Name Agency']

        if name_agency in find_element:
            get_element(name_agency, url_agencies)

        else:
            print('Check the name or spelling of the agency')
            browser.close_browser()
            exit()

    print('DONE, open_page_agency')


# Block with all elements Agency
def block_table_agency():
    try:
        return browser.find_element('id:investments-table-object_wrapper')

    except Exception as ex:
        print(ex)


# Form control (All)
def show_entery():
    try:
        browser.click_element('xpath://select[@class="form-control c-select"]/option[4]')

    except Exception as ex:
        print(ex)

    print('DONE, table_afgency')

def main():
    try:

    # Open the start page of the web-site
        open_website("https://itdashboard.gov/")
        browser.set_browser_implicit_wait(10)

    # Open all agency, click element 'DIVE IN'
        open_agency()
        browser.set_browser_implicit_wait(10)
        time.sleep(5)

    # General block Name and Spending Agencies
        block_agencies = general_block_agencies()
        browser.set_browser_implicit_wait(10)

    # Name and Spending Agencies
        informatin_agencies(get_text=block_agencies)
        browser.set_browser_implicit_wait(10)

    # Select one Agency
        open_page_agency(url_agencies=block_agencies)
        browser.set_browser_implicit_wait(10)

    # Block with all elements Agency
        block_agency = block_table_agency()
        browser.set_browser_implicit_wait(10)

    # Form control (All)
        show_entery()
        time.sleep(7)

        

        print('done')
        
    finally:
        browser.close_browser()


if __name__ == "__main__":
    main()
