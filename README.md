## JobHunter
Short project for Data Engineering job interview where the challenge is to webscrape HR/job related data and make it available with Flask. <br><br>
1. Run `setup.py` for packages and libraries installation (open terminal on Linkedin_JobHunt folder, type in command `python setup.py build` followed by `python setup.py install`);
2. In Linkedin_Scraping folder run `scrape_and_clean.py`, input the information asked (job title, location, max number of results wanted).
3. In Linkedin_Scraping folder run `api.py` to creat local connection.
Result: You will have the information scraped, cleaned and available in your localhost (0.0.0.0:5000/), click the button on the home page to access it.<br>

### Scraping LinkedIn:
- **`scraping.py`** contains a function to scrape LinkedIn using Selenium. Asks for `job title` and `location`;
- The function takes care of the infinite scrolling, and acts as a user, using random `time.sleep()` to avoid beeing blocked from the website;
- Each kind of information is stored as a list in a dictionary for easy access later on:

```
jobs_info = {'id': list(range(len(job_title))), 'job title': job_title, 'company': company, 'location': location,
                 'applicants': applicants, 'days ago': days, 'body': body, 'seniority level': seniority,
                 'employment type': employment, 'function': function, 'industry': industry, 'links': links_scraped
                 }
```
- Finally, it is stored as a `csv` file, on a format that is possible to be transformed into a `pandas.DataFrame` for easier manipulation;
- The results used for the rest of the exercise are the ones stores in **`search_results.csv`**.
<br><br>
### Data Cleaning:
- Some data cleaning was made with string manipulation, through **`cleaning.py`**;
- The days since the job offers were posted got transformed into integers, weeks and months were turned into total amount of days;
- Added keywords for job and location, getting them lower cased and removing punctuation;
- The cleaned data is stored in **`clean_results.csv`**.
<br><br>
### Flask API:
- Connected the data building an API with Flask using `swagger`, creating the `read()`function to display data sorted by days since the job offer was posted post;
- The basic connections are in `api.py`, and the features' functions are in `api_functions.py`;
- Still missing ADD and DELETE, amongst other essencial API features.
