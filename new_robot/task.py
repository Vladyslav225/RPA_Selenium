"""Template robot with Python."""


from RPA.Browser.Selenium import Selenium
from RPA.PDF import PDF

# I use openpyxl, because library "RPA.Excel.Application" work with Windows.
# I use Ubuntu.
from openpyxl import Workbook
import openpyxl
from openpyxl.writer.excel import save_workbook
import time

browser = Selenium()


# Basic page
# Create list with name and spending agencies
list_name_agency = []
list_spending_agency = []
list_link_agency = []


# Elements table of one of the agancies 'class:odd'
# Create a general list
list_uii_odd = []
list_bureau_odd = []
list_investment_title_odd = []
list_total_spending_odd = []
list_type_odd = []
list_rating_odd = []
list_project_odd = []


# Elements table of one of the agancies 'class:even'
# Create a general list
list_uii_even = []
list_bureau_even = []
list_investment_title_even = []
list_total_spending_even = []
list_type_even = []
list_rating_even = []
list_project_even = []



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


# #Get text Name, Spending Agencies
def information_agencies():
    try:
        block_agency = browser.find_elements("id:agency-tiles-widget")

    except Exception as ex:
        print(ex)

    for elements in block_agency:

    # Name Agency
        name_agencies = browser.find_elements('class:h4.w200', elements)
        for name in name_agencies:
            text_name = browser.get_text(name)
            list_name_agency.append(text_name)

    # Spending Agency
        spending_agencies = browser.find_elements('class:h1.w900', elements)
        for money in spending_agencies:
            text_spending = browser.get_text(money)
            list_spending_agency.append(text_spending)

    # URL Agency
        list_link_agency.append(browser.find_elements('class:btn.btn-default.btn-sm', elements))            


# Saving to Exel information about Agencies
# def save_to_xlsx(filename):

#     wb = Workbook()
#     book = wb.active
#     book.title = 'Agencies'
    
#     book['A1'] = 'Name Agencies'
#     book['B1'] = 'Spending Agencies'

#     r = 2
#     for name in list_name_agency:
#         book.cell(row=r, column=1).value = name
#         r += 1

#     r = 2
#     for money in list_spending_agency:
#         book.cell(row=r, column=2).value = money
#         r += 1

#     wb.save(filename=filename)
#     wb.close()


# Go to the page of one of the agencies
def go_to_agency():
    
    browser.click_element(list_link_agency[0][24])


# Form control (All)
def show_entery():
    browser.click_element('xpath://select[@class="form-control c-select"]/option[@value="-1"]')


# Name table
# def name_table():
#     # Name table
#     element_name_table = browser.find_element('class:h1.w200.martop-0.marbottom-0')
#     text_name_table = browser.get_text(element_name_table)

#     return text_name_table


# Data table Head
def head_table():
    pass


# Element Table Body
def table_body():
    get_table_body = browser.find_element('xpath://div[@class="dataTables_scrollBody"]//tbody')

    return get_table_body


# Elements 'class:odd'
def class_odd(odd):
    class_odd_elements = browser.find_elements('class:odd', odd)

    # UII elements
    for uii in class_odd_elements:
        element_uii = browser.find_elements('class:left.sorting_2', uii)

        for text_uii in element_uii:
            get_text_uii = browser.get_text(text_uii)
            list_uii_odd.append(get_text_uii)

    # Bureau
    for bureau in class_odd_elements:
        element_bureau = browser.find_elements('class:left.select-filter', bureau)

        for text_bureau in element_bureau:
            get_text_bureau = browser.get_text(text_bureau)
            list_bureau_odd.append(get_text_bureau)


    # Investment Title
    for investment_title in class_odd_elements:
        element_investment_title = browser.find_elements('class:left', investment_title)

        for text_investment_title in element_investment_title:
            get_text_investment_title = browser.get_text(text_investment_title)
            list_investment_title_odd.append(get_text_investment_title)


    # Total FY2021 Spending ($M)
    for total_spending in class_odd_elements:
        element_total_spending = browser.find_elements('class:right', total_spending)

        for text_total_spending in element_total_spending:
            get_text_total_spending = browser.get_text(text_total_spending)
            list_total_spending_odd.append(get_text_total_spending)


    # Type
    for _type in class_odd_elements:
        element_type = browser.find_elements('class:left.select-filter',_type)

        for text_type in element_type:
            get_text_type = browser.get_text(text_type)
            list_type_odd.append(get_text_type)


    # CIO Rating and Projects
    for rating_and_project in class_odd_elements:

        # CIO Rating
        element_rating = browser.find_elements('class:center', rating_and_project)[0]

        get_text_rating = browser.get_text(element_rating)
        list_rating_odd.append(get_text_rating)

        # Projects
        element_projects = browser.find_elements('class:center', rating_and_project)[1]

        get_text_projects = browser.get_text(element_projects)
        list_project_odd.append(get_text_projects)


# Elements 'class:even'
def class_even(even):
    class_even_elements = browser.find_elements('class:even', even)

    # UII elements
    for uii in class_even_elements:
        element_uii = browser.find_elements('class:left.sorting_2', uii)

        for text_uii in element_uii:
            get_text_uii = browser.get_text(text_uii)
            list_uii_even.append(get_text_uii)

    # Bureau
    for bureau in class_even_elements:
        element_bureau = browser.find_elements('class:left.select-filter', bureau)

        for text_bureau in element_bureau:
            get_text_bureau = browser.get_text(text_bureau)
            list_bureau_even.append(get_text_bureau)


    # Investment Title
    for investment_title in class_even_elements:
        element_investment_title = browser.find_elements('class:left', investment_title)

        for text_investment_title in element_investment_title:
            get_text_investment_title = browser.get_text(text_investment_title)
            list_investment_title_even.append(get_text_investment_title)


    # Total FY2021 Spending ($M)
    for total_spending in class_even_elements:
        element_total_spending = browser.find_elements('class:right', total_spending)

        for text_total_spending in element_total_spending:
            get_text_total_spending = browser.get_text(text_total_spending)
            list_total_spending_even.append(get_text_total_spending)


    # Type
    for type_ in class_even_elements:
        element_type = browser.find_elements('class:left.select-filter',type_)

        for text_type in element_type:
            get_text_type = browser.get_text(text_type)
            list_type_even.append(get_text_type)


    # CIO Rating and Projects
    for rating_and_project in class_even_elements:

        # CIO Rating
        element_rating = browser.find_elements('class:center', rating_and_project)[0]

        get_text_rating = browser.get_text(element_rating)
        list_rating_even.append(get_text_rating)

        # Projects
        element_projects = browser.find_elements('class:center', rating_and_project)[1]

        get_text_projects = browser.get_text(element_projects)
        list_project_even.append(get_text_projects)


def save_table_to_xlsx(FILENAME):

    try:
        wb = openpyxl.load_workbook(FILENAME)

    except:
        wb = Workbook()

    sheet_1 = wb.create_sheet('Agencies')
    sheet_2 = wb.create_sheet('Individual Investments')

    # for i, value in enumerate(columns, 1):
    #     sheet_1.cell(row=1, column=i).value = value

    for i, row in enumerate(list_uii_odd, 2):
        for j, value in enumerate(row, 1):
            sheet_1.cell(row=i, column=j).value = value


    for i, row in enumerate(list_uii_even, 2):
        for j, value in enumerate(row, 1):
            sheet_2.cell(row=i, column=j).value = value

    save_workbook(wb, FILENAME)
    wb.close()


# Get link in UII from Table
def url_from_table(url):
    link_table = browser.find_elements('tag:a', url)
    # print(link_table)

    # return link_table



def main():
    try:
        open_the_website("https://itdashboard.gov/")
        browser.set_browser_implicit_wait(10)

        open_list_agencies()
        browser.set_browser_implicit_wait(10)

        information_agencies()
        browser.set_browser_implicit_wait(10)
        
        # save_to_xlsx('output/file.xlsx')
        # browser.set_browser_implicit_wait(10)

        go_to_agency()
        browser.set_browser_implicit_wait(10)

        show_entery()
        time.sleep(10)

        # name_table()

        table = table_body()

        class_odd(odd=table)

        class_even(even=table)

        save_table_to_xlsx('output/file.xlsx')

        url_from_table(url=table)

        print('done')
        
    finally:
        browser.close_browser()


if __name__ == "__main__":
    main()
