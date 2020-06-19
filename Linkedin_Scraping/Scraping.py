from searchers import *

job = input('Input job title you wish to search: ')
location = input('Input location (city and/or country) you wish to search: ')
max_result = input('Input maximum number of results desired: ')

search = single_job_search(job, location, max_result=max_result)

