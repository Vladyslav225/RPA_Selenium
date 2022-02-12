"""Template robot with Python."""


from RPA.Browser.Selenium import Selenium
from RPA.PDF import PDF

# I use openpyxl, because library "RPA.Excel.Application" work with Windows.
# I use Ubuntu.
from openpyxl import Workbook
import time

browser = Selenium()

# TODO Затем бот должен выбрать одно из агентств, например National Science Foundation (это должно быть настроено в файле или на Robocloud)

list_name = []
list_spending = []
list_link = []

list_ = []


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

    # print(link)

    for elements in block_agency:

    # Name
        # name_agencies = browser.find_elements('class:h4.w200', elements)
        # for name in name_agencies:
        #     text_name = browser.get_text(name)
        #     list_name.append(text_name)

    # Spending
        # spending_agencies = browser.find_elements('class:h1.w900', elements)
        # for money in spending_agencies:
        #     text_spending = browser.get_text(money)
        #     list_spending.append(text_spending)

    # URL
        list_link.append(browser.find_elements('class:btn.btn-default.btn-sm', elements))            


# Saving to Exel information about Agencies
# def save_to_xlsx(filename):

    # wb = Workbook()
    # book = wb.active
    # book.title = 'Agencies'
    
    # book['A1'] = 'Name Agencies'
    # book['B1'] = 'Spending Agencies'

    # r = 2
    # for name in list_name:
    #     book.cell(row=r, column=1).value = name
    #     r += 1

    # r = 2
    # for money in list_spending:
    #     book.cell(row=r, column=2).value = money
    #     r += 1

    # wb.save(filename=filename)
    # wb.close()


# Go to the page of one of the agencies
def go_to_agency():
    
    browser.click_element(list_link[0][24])


# Get investments table
def investments_table(filename):
    # n = browser.find_element('class:h1.w200.martop-0.marbottom-0')
    # b = browser.get_text(n)
    # print(b)

    # Form control (All)
    browser.click_element('xpath://select[@class="form-control c-select"]/option[@value="-1"]')
    time.sleep(10)

    # Data table Head
    # table_head = browser.find_elements('xpath://div[@class="dataTables_wrapper no-footer"]//div[@class="dataTables_scrollHead"]')
    # text_table_head = browser.get_text(table_head)
    # split_ = text_table_head.split()
    # print(split_)
    # print(type(text_table_head))
    
    # Data tables Body
    table_body = browser.find_element('xpath://div[@class="dataTables_scrollBody"]//tbody')

    # Elements 'class:odd'
    table_odd_elements = browser.find_elements('class:odd', table_body)
    # print(body_elements)

    # Get link in UII
    tag_a = browser.find_elements('tag:a', table_body)
    # print(tag_a)

    # UII elements
    for id in table_odd_elements:
        element_id = browser.find_elements('class:left.sorting_2', id)

        for text_id in element_id:
            get_text_id = browser.get_text(text_id)
            print(get_text_id)

    # Bureau
    for bureau in table_odd_elements:
        element_bureau = browser.find_elements('class:left.select-filter', bureau)

        for text_bureau in element_bureau:
            get_text_bureau = browser.get_text(text_bureau)
            print(get_text_bureau)


    # Investment Title
    for investment_title in table_odd_elements:
        element_investment_title = browser.find_elements('class:left', investment_title)

        for text_investment_title in element_investment_title:
            get_text_investment_title = browser.get_text(text_investment_title)
            print(get_text_investment_title)


    # Total FY2021 Spending ($M)
    for total_spending in table_odd_elements:
        element_total_spending = browser.find_elements('class:right', total_spending)

        for text_total_spending in element_total_spending:
            get_text_total_spending = browser.get_text(text_total_spending)
            print(get_text_total_spending)


    # Type
    for type_ in table_odd_elements:
        element_type = browser.find_elements('class:left.select-filter',type_)

        for text_type in element_type:
            get_text_type = browser.get_text(text_type)
            print(get_text_type)



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

        investments_table('output/file.xlsx')
        browser.set_browser_implicit_wait(10)

        print('done')
        
    finally:
        browser.close_browser()


if __name__ == "__main__":
    main()
