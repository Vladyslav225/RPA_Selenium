# Function module 'open_page_agency' for going to the agency page


from RPA.Browser.Selenium import Selenium

browser = Selenium()

def get_element(name_agency, url_agencies):
    if name_agency == 'Department of Agriculture':
        element = browser.find_element('xpath://div/div[1]/div[1]/div/div/div[@class="col-sm-12"]/a', url_agencies)
        browser.click_element(element)

    elif name_agency == 'Department of Commerce':
        element = browser.find_element('xpath://div/div[1]/div[2]/div/div/div[@class="col-sm-12"]/a', url_agencies)
        browser.click_element(element)

    elif name_agency == 'Department of Defense':
        element = browser.find_element('xpath://div/div[1]/div[3]/div/div/div[@class="col-sm-12"]/a', url_agencies)
        browser.click_element(element)

    elif name_agency == 'Department of Health and Human Services':
        element = browser.find_element('xpath://div/div[2]/div[1]/div/div/div[@class="col-sm-12"]/a', url_agencies)
        browser.click_element(element)

    elif name_agency == 'Department of the Interior':
        element = browser.find_element('xpath://div/div[2]/div[2]/div/div/div[@class="col-sm-12"]/a', url_agencies)
        browser.click_element(element)

    elif name_agency == 'Department of Justice':
        element = browser.find_element('xpath://div/div[2]/div[3]/div/div/div[@class="col-sm-12"]/a', url_agencies)
        browser.click_element(element)

    elif name_agency == 'Department of Labor':
        element = browser.find_element('xpath://div/div[3]/div[1]/div/div/div[@class="col-sm-12"]/a', url_agencies)
        browser.click_element(element)

    elif name_agency == 'Department of State':
        element = browser.find_element('xpath://div/div[3]/div[2]/div/div/div[@class="col-sm-12"]/a', url_agencies)
        browser.click_element(element)

    elif name_agency == 'Department of the Treasury':
        element = browser.find_element('xpath://div/div[3]/div[3]/div/div/div[@class="col-sm-12"]/a', url_agencies)
        browser.click_element(element)

    elif name_agency == 'Social Security Administration':
        element = browser.find_element('xpath://div/div[4]/div[1]/div/div/div[@class="col-sm-12"]/a', url_agencies)
        browser.click_element(element)

    elif name_agency == 'Department of Education':
        element = browser.find_element('xpath://div/div[4]/div[2]/div/div/div[@class="col-sm-12"]/a', url_agencies)
        browser.click_element(element)

    elif name_agency == 'Department of Energy':
        element = browser.find_element('xpath://div/div[4]/div[3]/div/div/div[@class="col-sm-12"]/a', url_agencies)
        browser.click_element(element)

    elif name_agency == 'Environmental Protection Agency':
        element = browser.find_element('xpath://div/div[5]/div[1]/div/div/div[@class="col-sm-12"]/a', url_agencies)
        browser.click_element(element)

    elif name_agency == 'Department of Transportation':
        element = browser.find_element('xpath://div/div[5]/div[2]/div/div/div[@class="col-sm-12"]/a', url_agencies)
        browser.click_element(element)

    elif name_agency == 'General Services Administration':
        element = browser.find_element('xpath://div/div[5]/div[3]/div/div/div[@class="col-sm-12"]/a', url_agencies)
        browser.click_element(element)

    elif name_agency == 'Department of Homeland Security':
        element = browser.find_element('xpath://div/div[6]/div[1]/div/div/div[@class="col-sm-12"]/a', url_agencies)
        browser.click_element(element)

    elif name_agency == 'Department of Housing and Urban Development':
        element = browser.find_element('xpath://div/div[6]/div[2]/div/div/div[@class="col-sm-12"]/a', url_agencies)
        browser.click_element(element)

    elif name_agency == 'National Aeronautics and Space Administration':
        element = browser.find_element('xpath://div/div[6]/div[3]/div/div/div[@class="col-sm-12"]/a', url_agencies)
        browser.click_element(element)

    elif name_agency == 'Office of Personnel Management':
        element = browser.find_element('xpath://div/div[7]/div[1]/div/div/div[@class="col-sm-12"]/a', url_agencies)
        browser.click_element(element)

    elif name_agency == 'Small Business Administration':
        element = browser.find_element('xpath://div/div[7]/div[2]/div/div/div[@class="col-sm-12"]/a', url_agencies)
        browser.click_element(element)

    elif name_agency == 'Department of Veterans Affairs':
        element = browser.find_element('xpath://div/div[7]/div[3]/div/div/div[@class="col-sm-12"]/a', url_agencies)
        browser.click_element(element)

    elif name_agency == 'U.S. Agency for International Development':
        element = browser.find_element('xpath://div/div[8]/div[1]/div/div/div[@class="col-sm-12"]/a', url_agencies)
        browser.click_element(element)

    elif name_agency == 'U.S. Army Corps of Engineers':
        element = browser.find_element('xpath://div/div[8]/div[2]/div/div/div[@class="col-sm-12"]/a', url_agencies)
        browser.click_element(element)

    elif name_agency == 'National Archives and Records Administration':
        element = browser.find_element('xpath://div/div[8]/div[3]/div/div/div[@class="col-sm-12"]/a', url_agencies)
        browser.click_element(element)

    elif name_agency == 'National Science Foundation':
        element = browser.find_element('xpath://div/div[9]/div[1]/div/div/div[@class="col-sm-12"]/a', url_agencies)
        browser.click_element(element)

    elif name_agency == 'Nuclear Regulatory Commission':
        element = browser.find_element('xpath://div/div[9]/div[2]/div/div/div[@class="col-sm-12"]/a', url_agencies)
        browser.click_element(element)
    

    print('DONE, get_element')