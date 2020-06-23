from Linkedin_Scraping.scraping_and_cleaning.cleaning import *
from Linkedin_Scraping.scraping_and_cleaning.scraping import *

single_job_search(max_result=1000)

CleanData('../data/search_results.csv').cleaning()
