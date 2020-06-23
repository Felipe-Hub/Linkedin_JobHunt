{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## JobHunter\n",
    "Short project for Data Engineering job interview where the challenge is to webscrape HR/job related data and make it available with Flask. <br><br>\n",
    "### Scraping LinkedIn:\n",
    "- **`searchers.py`** contains a function to scrape LinkedIn using Selenium. Asks for `job title` and `location`;\n",
    "- The function takes care of the infinite scrolling, and acts as a user, using random `time.sleep()` to avoid beeing blocked from the website;\n",
    "- Each kind of information is stored as a list in a dictionary for easy access later on:\n",
    "\n",
    "```\n",
    "jobs_info = {'id': list(range(len(job_title))), 'job title': job_title, 'company': company, 'location': location,\n",
    "                 'applicants': applicants, 'days ago': days, 'body': body, 'seniority level': seniority,\n",
    "                 'employment type': employment, 'function': function, 'industry': industry, 'links': links_scraped\n",
    "                 }\n",
    "```\n",
    "- Finally, it is stored as a `csv` file, on a format that is possible to be transformed into a `pandas.DataFrame` for easier manipulation;\n",
    "- The results used for the rest of the exercise are the ones stores in **`search_results_test.csv`**.\n",
    "<br><br>\n",
    "### Data Cleaning:\n",
    "- Some data cleaning was made with string manipulation, through **`Data_Cleaning.py`**;\n",
    "- The days since the job offers were posted got transformed into integers, weeks and months were turned into total amount of days;\n",
    "- Added keywords for job and location, getting them lower cased and removing punctuation;\n",
    "- The cleaned data is stored in **`clean_results.csv`**.\n",
    "<br><br>\n",
    "### Flask API:\n",
    "- Connected the data building an API with Flask using `swagger`, creating the `read()`function to display data sorted by days since the job offer was posted post;\n",
    "- The basic connections are in `frontend.py`, and the features' functions are in `backend.py`;\n",
    "- Still missing ADD and DELETE, amongst other essencial API features.\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
