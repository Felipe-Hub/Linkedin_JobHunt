from searchers import *
from flask import jsonify

df = pd.read_csv('clean_results.csv').drop('Unnamed: 0', axis=1)
data = df.to_dict(orient='records')


def read():
    """
    This function responds to a request for /api/people
    with the complete lists of people

    :return:        sorted by days list of job offers
    """
    return sorted(data, key=lambda x: x['days ago'])
