import pandas as pd
df = pd.read_csv('events.csv')
print(df.info())
def get_day(data):
    return data[0:2]
df['day'] = df['visit_date'].apply(get_day)
print('\n---- Новый столбец "day" -------------')
print(df['day'].head(5))
