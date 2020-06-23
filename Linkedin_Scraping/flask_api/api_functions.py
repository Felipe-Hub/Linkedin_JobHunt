import pandas as pd


# Data
df = pd.read_csv('data/clean_results.csv').drop('Unnamed: 0', axis=1)
data = df.to_dict(orient='records')


class JobHunt:

    def read():
        """
        This method responds to a request with the complete list
        of job offers.

        :return: list of job offers sorted by days
        """
        return sorted(data, key=lambda x: x['days ago'])
