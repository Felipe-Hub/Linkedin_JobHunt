import pandas as pd


def total_days(x):
    """
    Turns weeks and months into total days.
    :param x: string
    :return: total of days as int
    """
    x = x.split()

    if x[1] == 'week':
        days = int(x[0]) * 7

    elif x[1] == 'month':
        days = int(x[0]) * 30

    else:
        days = int(x[0])

    return days


df = pd.read_csv('search_results_test.csv')

df['keywords_job'] = df['job title'].apply(lambda x: x.lower().replace('/', ' ').replace('.', ''))
df['keywords_loc'] = df['location'].apply(lambda x: x.lower().replace('/', ' ').replace('.', ''))

df['days ago'] = df['days ago'].apply(lambda x: total_days(x) if x != 'Not informed.' else x)

df.to_csv('clean_results.csv')