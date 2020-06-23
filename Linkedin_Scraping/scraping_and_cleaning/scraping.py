from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Firefox
from random import uniform
import pandas as pd
import time
import csv


def single_job_search(max_result=''):
    """
    Ask user to input job title (or company) and location to look for and scrape job offers in LinkedIn.
    If there is no input it will perform a general/global job search to scrape from.

    :param: max_result: maximum number of job offers you want to scrape.
    :return: a tuple with job offers information in a dictionary, and the list of errors (dict, errors).
    """

    job = input('Input job title you wish to search: ')
    location = input('Input location (city and/or country) you wish to search: ')

    # starts driver on LinkedIn job search page
    url = 'https://www.linkedin.com/jobs'
    driver = Firefox()
    time.sleep(1)
    driver.get(url)
    time.sleep(3)

    # inputs search words on respective bars in Linkedin and click search button
    # job title or company input
    job_bar = driver.find_elements_by_xpath("//input[@aria-label='Search job titles or companies']")
    job_bar[1].send_keys(job)
    time.sleep(1)
    job_bar[1].click()
    # location input
    loc_bar = driver.find_elements_by_xpath('//input[@aria-controls="job-search-bar-location-typeahead-list"]')
    loc_bar[1].clear()
    # sometime the dropdown menu obscures the search button, to solve it:
    # only write location if it is specified
    if location != '':
        loc_bar[1].send_keys(location)
        time.sleep(1)
        # sometimes the location does not have a drop down menu, so we have to click the search button
        if len(driver.find_elements_by_id('location-1')) > 0:
            driver.find_elements_by_id('location-1')[0].click()
            time.sleep(1)
        else:
            driver.find_elements_by_xpath('//button[@class="search__button pill pill--blue etta-pill"]')[1].click()
            time.sleep(1)
    # click search button if no location is specified
    else:
        driver.find_elements_by_xpath('//button[@class="search__button pill pill--blue etta-pill"]')[1].click()
        time.sleep(1)

    elements = list()

    # searches all results until maximum allowed by LinkedIn
    if max_result == '':
        breaker = True
        while breaker is True:
            breaker = len(elements)
            # store each job offer card element
            elements = driver.find_elements_by_class_name('result-card__full-card-link')
            elements[-1].send_keys(Keys.NULL)
            time.sleep(uniform(1, 1.5))
            # this if statement will break the while loop if there are no more job offers available:
            if len(elements) == breaker:
                breaker = False
            else:
                breaker = True
            # in case infinite scroll ends click "show more" button
            show_more = driver.find_elements_by_xpath('//button[@class="infinite-scroller__show-more-button '
                                                      'infinite-scroller__show-more-button--visible"]')
            if len(show_more) > 0:
                show_more[0].click()
    # searches until maximum results required is reached
    else:
        while len(elements) < int(max_result):
            breaker = len(elements)
            # store each job offer card element
            elements = driver.find_elements_by_class_name('result-card__full-card-link')
            elements[-1].send_keys(Keys.NULL)
            time.sleep(uniform(1, 1.5))
            # this if statement will break the while loop if there are no more job offers available:
            if len(elements) == breaker:
                break
            # in case infinite scroll ends click "show more" button
            show_more = driver.find_elements_by_xpath('//button[@class="infinite-scroller__show-more-button '
                                                      'infinite-scroller__show-more-button--visible"]')
            if len(show_more) > 0:
                show_more[0].click()

    # create data structures to store scraped info
    job_title = list()
    location = list()
    company = list()
    applicants = list()
    days = list()
    body = list()
    seniority = list()
    employment = list()
    function = list()
    industry = list()

    # get links for job offers
    links_scraped = [element.get_attribute('href') for element in elements]
    # empty list to store possible errors
    errors = list()
    for element in elements:
        # the try and excepts are import:
        # the first one will check availability of link to job description, if not available appends as an error
        # the other tries and excepts will check if info is available, it is not available, it will append None
        # that way we keep the lists with same length for the dict, making it possible to build a pandas.DataFrame
        try:
            element.click()
            time.sleep(uniform(0.5, 1))
        except:
            errors.append(element.get_attribute('href'))  # stores links of failed job offer click
        try:
            job_title.append(driver.find_element_by_class_name(
                'topcard__title').text)
        except:
            job_title.append('Not informed.')
        try:
            location.append(driver.find_element_by_xpath(
                '//span[@class="topcard__flavor topcard__flavor--bullet"]').text)
        except:
            location.append('Not informed.')
        try:
            company.append(driver.find_element_by_xpath(
                '//a[@class="topcard__org-name-link topcard__flavor--black-link"]').text)
        except:
            company.append('Not informed.')
        try:
            applicants.append(driver.find_element_by_xpath(
                '//figcaption[@class="num-applicants__caption"]').text)
        except:
            applicants.append('Not informed.')
        try:
            days.append(driver.find_element_by_xpath(
                '//span[@class="topcard__flavor--metadata posted-time-ago__text"]').text)
        except:
            days.append('Not informed.')
        try:
            body.append(driver.find_element_by_xpath(
                '//div[@class="show-more-less-html__markup show-more-less-html__markup--clamp-after-5"]').text)
        except:
            body.append('Not informed.')
        try:
            seniority.append(driver.find_elements_by_xpath(
                '//span[@class="job-criteria__text job-criteria__text--criteria"]')[0].text)
        except:
            seniority.append('Not informed.')
        try:
            employment.append(driver.find_elements_by_xpath(
                '//span[@class="job-criteria__text job-criteria__text--criteria"]')[1].text)
        except:
            employment.append('Not informed.')
        try:
            function.append(driver.find_elements_by_xpath(
                '//span[@class="job-criteria__text job-criteria__text--criteria"]')[2].text)
        except:
            function.append('Not informed.')
        try:
            industry.append(driver.find_elements_by_xpath(
                '//span[@class="job-criteria__text job-criteria__text--criteria"]')[3].text)
        except:
            industry.append('Not informed.')

        time.sleep(uniform(0.5, 1))

    jobs_info = {'id': list(range(len(job_title))), 'job title': job_title, 'company': company, 'location': location,
                 'applicants': applicants, 'days ago': days, 'body': body, 'seniority level': seniority,
                 'employment type': employment, 'function': function, 'industry': industry, 'links': links_scraped
                 }

    print("You have successfully scraped {} job offers".format(len(jobs_info['id'])))
    print("Saving results to file!")
    df = pd.DataFrame.from_dict(jobs_info)
    df.to_csv('search_results.csv')

    if len(errors) > 0:
        print("Failed scraping {} job offers".format(len(errors)))
        print("Saving errors to file!")
        with open('search_errors.csv', 'w', newline='') as outfile:
            writer = csv.writer(outfile)
            writer.writerow(errors)

    driver.quit()

    return jobs_info, errors


"""
TO DO:


def job_search(job=None, location=None, max_results=100):
    
    Choose job title(s) (or companies) and location(s) to look for and scrape job offers in Linkedin.
    If no parameters is passed it will perform a general/global job search to scrape from.

    :param: job: takes a string or list of strings to input in Linkedin job search bar.
    :param: location: takes a string or list of strings to input in Linkedin location search bar.
    :param: max_results: maximum number of job offer you want to scrape.
    :return: pandas.DataFrame
   


    # verifies type of input
    if type(job) == str:
        if type(location) == str:

        elif type(location) == list:

    elif type(job) == list:
        if type(location) == str:

        elif type(location) == list:

    else:
        raise TypeError("The parameters must be string or list of strings.")



    return

"""
