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
# from app.table_element import elements_table_body

browser = Selenium()

pdf = PDF()

# List Name and Spanding Agencies from Start page
name_spending_agency = []

# List elements from table Agency
list_text_table = []

# List URL from table Agency
list_url_table = []



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

        # Function module for going to the agency page
            get_element(name_agency, url_agencies)

        else:
            print('Check the name or spelling of the agency')
            browser.close_browser()
            exit()

    print('DONE, open_page_agency')


# Block with all elements Agency
def block_data_table_agency():
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


# Getting block body table elements
def block_body_table(body_table):
    try:
        browser.find_element('xpath://div[@class="dataTables_scrollBody"]/table/tbody', body_table)
        
    except Exception as ex:
        print(ex)

    print('DONE, block_body_table')


# Getting table body text
def elements_table_body(elements):
    list_uii = []
    list_bureau = []
    list_investment = []
    list_spending = []
    list_type = []
    list_rating = []
    list_projects = []


    # UII
    try:
        uii_elements = browser.find_elements('xpath://tr/td[1][@class="left sorting_2"]', elements)

    except Exception as ex:
        print(ex)

    for url in uii_elements:
        finder_url = browser.find_elements('tag:a', url)

        for item in finder_url:
            if item ==  None:
                continue

            list_url_table.append(item)

    for text_uii in uii_elements:
        list_uii.append(browser.get_text(text_uii))


    # Bureau
    try:
        bureau_elements = browser.find_elements('xpath://tr/td[2][@class=" left select-filter"]', elements)

    except Exception as ex:
        print(ex)

    for text_bureau in bureau_elements:
        list_bureau.append(browser.get_text(text_bureau))


    # Investment Title
    try:
        investment_elements = browser.find_elements('xpath://tr/td[3][@class=" left"]', elements)

    except Exception as ex:
        print(ex)

    for text_investment in investment_elements:
        list_investment.append(browser.get_text(text_investment))


    # Total Spending
    try:
        spending_elements = browser.find_elements('xpath://tr/td[4][@class=" right"]', elements)

    except Exception as ex:
        print(ex)

    for text_spending in spending_elements:
        list_spending.append(browser.get_text(text_spending))


    # Type
    try:
        type_elements = browser.find_elements('xpath://tr/td[5][@class=" left select-filter"]', elements)

    except Exception as ex:
        print(ex)

    for text_type in type_elements:
        list_type.append(browser.get_text(text_type))


    # CIO Rating
    try:
        rating_elements = browser.find_elements('xpath://tr/td[6][@class=" center"]', elements)

    except Exception as ex:
        print(ex)

    for text_rating in rating_elements:
        list_rating.append(browser.get_text(text_rating))

    
    # Projects
    try:
        projects_elements = browser.find_elements('xpath://tr/td[7][@class=" center"]', elements)

    except Exception as ex:
        print(ex)

    for text_projects in projects_elements:
        list_projects.append(browser.get_text(text_projects))


    list_text_table.append(
        {
            'UII': list_uii,
            'Bureau': list_bureau,
            'Investment Title': list_investment,
            'Total Spending': list_spending,
            'Type': list_type,
            'CIO Rating': list_rating,
            'Projects': list_projects
        }
    )

    return list_text_table


# Open pages from table
def open_url_table(file_pdf):
    open_page = browser.click_element(list_url_table[0])
    browser.set_browser_implicit_wait(10)

    # Download Business Case PDF
    element_case = browser.find_element('id:business-case-pdf')

    browser.click_element(element_case)
    time.sleep(20)

    print('DONE, open_url_table')



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
        block_table_agency = block_data_table_agency()
        browser.set_browser_implicit_wait(10)

    # Form control (All)
        show_entery()
        time.sleep(10)

    # Getting block body table elements
        all_elements = block_body_table(body_table=block_table_agency)

    # Getting table body text
        elements_table_body(elements=all_elements)

    # Open pages from table
        open_url_table('new_robot/output')

        print('done')
        
    finally:
        browser.close_browser()


if __name__ == "__main__":
    main()
