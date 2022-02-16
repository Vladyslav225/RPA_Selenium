"""Template robot with Python."""


from turtle import title
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
list_name_agency = []
list_spending_agency = []
list_link_agency = []


# Head Table
list_head = []


# Lists elements table of one of the agancies 'class:odd'
list_uii_odd = []
list_bureau_odd = []
list_investment_title_odd = []
list_total_spending_odd = []
list_type_odd = []
list_rating_odd = []
list_project_odd = []

# Lists elements table of one of the agancies 'class:even'
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


# Go to the page of one of the agencies
def go_to_agency():
    
    browser.click_element(list_link_agency[0][24])


# Form control (All)
def show_entery():
    browser.click_element('xpath://select[@class="form-control c-select"]/option[4]')


# Data table Head
def head_table():
    block_head = browser.find_element('class:dataTables_scrollHeadInner')

    # elements_class_left = browser.find_elements('class:left', block_head)
    # for text_left in elements_class_left:
    #     list_head.append(browser.get_text(text_left))

    # elements_class_right = browser.find_elements('class:right.sorting', block_head)
    # for text_right in elements_class_right:
    #     list_head.append(browser.get_text(text_right))

    # elements_class_center = browser.find_elements('class:center.sorting', block_head)
    # for text_center in elements_class_center:
    #     list_head.append(browser.get_text(text_center))

    elements = browser.find_elements('xpath:/table[@class="datasource-table usa-table-borderless dataTable no-footer"]/thead/tr[2]/th', block_head)
    for text_elements in elements:
        list_head.append(browser.get_text(text_elements))

    print(list_head)


# Element Table Body
def table_body():
    get_table_body = browser.find_element('xpath://div[@class="dataTables_scrollBody"]//tbody')

    return get_table_body


# Elements 'class:odd'
def class_odd(odd):
    class_odd_elements = browser.find_elements('class:odd', odd)

    # Elements with general class "left..."
    for class_left in class_odd_elements:

        # UII elements
        element_uii = browser.find_elements('class:left', class_left)[0]

        get_text_uii = browser.get_text(element_uii)
        list_uii_odd.append(get_text_uii)

        # Bureau and Type
        element_bureau = browser.find_elements('class:left', class_left)[1]
        get_text_bureau = browser.get_text(element_bureau)
        list_bureau_odd.append(get_text_bureau)

        # Investment Title
        element_investment_title = browser.find_elements('class:left', class_left)[2]
        get_text_investment_title = browser.get_text(element_investment_title)
        list_investment_title_odd.append(get_text_investment_title)

        # Type
        element_type = browser.find_elements('class:left', class_left)[3]
        get_text_type = browser.get_text(element_type)
        list_type_odd.append(get_text_type)

    # Total FY2021 Spending ($M)
    for total_spending in class_odd_elements:
        element_total_spending = browser.find_elements('class:right', total_spending)

        for text_total_spending in element_total_spending:
            get_text_total_spending = browser.get_text(text_total_spending)
            list_total_spending_odd.append(get_text_total_spending)

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

    # Elements with general class "left..."
    for class_left in class_even_elements:

        # UII elements
        element_uii = browser.find_elements('class:left', class_left)[0]

        get_text_uii = browser.get_text(element_uii)
        list_uii_even.append(get_text_uii)

        # Bureau and Type
        element_bureau = browser.find_elements('class:left', class_left)[1]
        get_text_bureau = browser.get_text(element_bureau)
        list_bureau_even.append(get_text_bureau)

        # Investment Title
        element_investment_title = browser.find_elements('class:left', class_left)[2]
        get_text_investment_title = browser.get_text(element_investment_title)
        list_investment_title_even.append(get_text_investment_title)

        # Type
        element_type = browser.find_elements('class:left', class_left)[3]
        get_text_type = browser.get_text(element_type)
        list_type_even.append(get_text_type)

    # Total FY2021 Spending ($M)
    for total_spending in class_even_elements:
        element_total_spending = browser.find_elements('class:right', total_spending)

        for text_total_spending in element_total_spending:
            get_text_total_spending = browser.get_text(text_total_spending)
            list_total_spending_even.append(get_text_total_spending)

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


# Create and save exel
def save_table_to_xlsx(FILENAME):
    wb = Workbook()

    # Sheet-1
    sheet_1 = wb.active
    sheet_1.title='Agencies'

    sheet_1['A1'] = 'Name Agencies'
    sheet_1['B1'] = 'Spending Agencies'

    r = 2
    for name in list_name_agency:
        sheet_1.cell(row=r, column=1).value = name
        r += 1

    r = 2
    for money in list_spending_agency:
        sheet_1.cell(row=r, column=2).value = money
        r += 1
    

    # Sheet-2
    sheet_2 = wb.create_sheet(index=1, title='Individual Investments')

    c=1
    for head in list_head:
        sheet_2.cell(row=1, column=c).value = head
        c+=1

    r = 2
    for uii_odd in list_uii_odd:
        sheet_2.cell(row=r, column=1).value = uii_odd
        r += 1

    r = 2
    for bureau_odd in list_bureau_odd:
        sheet_2.cell(row=r, column=2).value = bureau_odd
        r += 1

    r = 2
    for investment_title_odd in list_investment_title_odd:
        sheet_2.cell(row=r, column=3).value = investment_title_odd
        r += 1

    r = 2
    for total_spending_odd in list_total_spending_odd:
        sheet_2.cell(row=r, column=4).value = total_spending_odd
        r += 1

    r = 2
    for _type_odd in list_type_odd:
        sheet_2.cell(row=r, column=5).value = _type_odd
        r += 1

    r = 2
    for rating_odd in list_rating_odd:
        sheet_2.cell(row=r, column=6).value = rating_odd
        r += 1

    r = 2
    for project_odd in list_project_odd:
        sheet_2.cell(row=r, column=7).value = project_odd
        r += 1



    r = 13
    for uii_even in list_uii_even:
        sheet_2.cell(row=r, column=1).value = uii_even
        r += 1

    r = 13
    for bureau_even in list_bureau_even:
        sheet_2.cell(row=r, column=2).value = bureau_even
        r += 1

    r = 13
    for investment_title_even in list_investment_title_even:
        sheet_2.cell(row=r, column=3).value = investment_title_even
        r += 1

    r = 13
    for total_spending_even in list_total_spending_even:
        sheet_2.cell(row=r, column=4).value = total_spending_even
        r += 1

    r = 13
    for _type_even in list_type_even:
        sheet_2.cell(row=r, column=5).value = _type_even
        r += 1

    r = 13
    for rating_even in list_rating_even:
        sheet_2.cell(row=r, column=6).value = rating_even
        r += 1

    r = 13
    for project_even in list_project_even:
        sheet_2.cell(row=r, column=7).value = project_even
        r += 1



    wb.save(filename=FILENAME)
    wb.close()




# Get link in UII from Table
def url_from_table(url):
    link_table = browser.find_elements('tag:a', url)
    # print(link_table)

    for text_url in link_table:
        get_text_url = browser.get_text(text_url)
        print(get_text_url)

    # return link_table



def main():
    try:
        open_the_website("https://itdashboard.gov/")
        browser.set_browser_implicit_wait(10)

        open_list_agencies()
        browser.set_browser_implicit_wait(10)

        information_agencies()
        browser.set_browser_implicit_wait(10)

        go_to_agency()
        time.sleep(10)

        show_entery()
        time.sleep(10)

        head_table()

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
