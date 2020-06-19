from random import uniform
from selenium.webdriver import Firefox
import pandas as pd
import selenium
import time


def single_job_search(job=None, location=None, max_results=100):
    """
    Choose job title (or company) and location to look for and scrape job offers in Linkedin.
    If no parameters is passed it will perform a general/global job search to scrape from.

    :param: job: takes a string to input in Linkedin job search bar.
    :param: location: takes a string to input in Linkedin location search bar.
    :param: max_results: maximum number of job offers you want to scrape.
    :return: pandas.DataFrame with job offer information
    """

    # starts driver on Linkedin job search page
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
    loc_bar[1].send_keys(location)
    time.sleep(1)
    loc_bar[1].click()
    # clicke search button
    driver.find_elements_by_xpath('//button[@class="search__button pill pill--blue etta-pill"]')[1].click()
    time.sleep(1)

    jobs_info = {'links': links_scraped = list(), }
    while len(links_scraped) < max_results:
        elements = driver.find_elements_by_class_name('result-card__full-card-link')
        links = [element.get_attribute('href') for element in elements]
        links_scraped += links
        elements[-1].send_keys(Keys.NULL)
        time.sleep(uniform(1, 2))


    df = pd.DataFrame.from_dict()

    return df


def job_search(job=None, location=None, max_results=100):
    """
    Choose job title(s) (or companies) and location(s) to look for and scrape job offers in Linkedin.
    If no parameters is passed it will perform a general/global job search to scrape from.

    :param: job: takes a string or list of strings to input in Linkedin job search bar.
    :param: location: takes a string or list of strings to input in Linkedin location search bar.
    :param: max_results: maximum number of job offer you want to scrape.
    :return: pandas.DataFrame
    """


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

test
