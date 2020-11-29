import pandas as pd

df3 = df_cash[df_cash['acct_num'] == '12345678']
df3.sort_values(['cal_date'], axis=0, ascending = True, inplace=True)
df3.iloc[0, df3.columns.get_loc('Running_Tot')] = df3.iloc[0, df3.columns.get_loc('free_cash')]
intaccr = 0

for index, row in df3.iterrows():
    runtot = row['free_cash'] + intaccr
    intaccr = row['Running_Tot'] * (row['bdp_rate'] / (365 * 100))
    df3.iloc[index, df3.columns.get_loc('Running_Tot')] = runtot #this line is throwing error
    df3.iloc[index, df3.columns.get_loc('Interest_accr')] = intaccr

df3