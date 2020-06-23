import pandas as pd


def total_days(string):
    """
    Turns weeks and months into total days.
    :param string: string to be manipulated
    :return: total of days as int
    """
    list_words = string.split()

    if list_words[1] == 'week':
        days = int(list_words[0]) * 7

    elif list_words[1] == 'month':
        days = int(list_words[0]) * 30

    else:
        days = int(list_words[0])

    return days


class CleanData:

    def __init__(self, file):
        self.file = file

    def cleaning(self):
        df = pd.read_csv(self.file)

        df['keywords_job'] = df['job title'].apply(lambda x: x.lower().replace('/', ' ').replace('.', ''))
        df['keywords_loc'] = df['location'].apply(lambda x: x.lower().replace('/', ' ').replace('.', ''))

        df['days ago'] = df['days ago'].apply(lambda x: total_days(x) if x != 'Not informed.' else x)

        df.to_csv('../data/clean_results.csv')
        print("Data cleaned and saved in: '../data/clean_results.csv'")
