import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Читаем файл
df = pd.read_csv('UkraineConflict.csv')

def date_to_time_sorted(date):
    return date.split("-")[1]+"-"+date.split("-")[2]

def month_number(date):
    dict = {
        'January-2022': 1,
        'February-2022': 2,
        'March-2022': 3,
        'April-2022': 4,
        'May-2022': 5,
        'June-2022': 6,
        'July-2022': 7,
        'August-2022': 8,
        'September-2022': 9,
        'October-2022': 10,
        'November-2022': 11,
        'December-2022': 12,
        'January-2023': 13,
        'February-2023': 14,
        'March-2023': 15
    }
    return dict[date]

# Диаграмма рассеивания
flg, ax = plt.subplots(figsize=(20, 12))

df['DATE'] = df['EVENT_DATE'].apply(date_to_time_sorted)
df_sorted = df[df['YEAR']>2021][['FATALITIES', 'DATE']].groupby('DATE').agg({'FATALITIES': ['sum']}).reset_index()
df_sorted.columns = ['date', 'deaths']
df_sorted['month'] = df_sorted['date'].apply(month_number)
df_sorted.sort_values(by=['month'])

ax.scatter(x=df_sorted['month'], y=df_sorted['deaths'])
plt.xlabel("Временная метка")
plt.ylabel("Смерти")
plt.show()

# Ящик с усами
plt.boxplot(x=df_sorted['deaths'])
plt.show()


# кореляционная матрица
corr_df = df[['FATALITIES', 'INTERACTION', 'YEAR']]
corr = corr_df.corr()
sns.heatmap(corr, annot=True)
print(corr)


