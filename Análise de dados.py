import pandas as pd
df= pd.read_csv('telecom_users.csv')
df =df.drop(['Unnamed: 0'], axis=1)
print(df)
df['TotalGasto'] = pd.to_numeric(df['TotalGasto'], errors ='coerce')
df = df.dropna(how='all', axis=1)
df = df.dropna(how='any', axis=0)
print(df.info())
print(df['Churn'].value_counts(normalize = True).map('{:.1%}'.format))

import plotly.express as px

for coluna in df:
    if coluna != "IDCliente":
        fig = px.histogram(df, x=coluna, color='Churn')
        fig.show()
        print(df.pivot_table(index='Churn', columns=coluna, aggfunc='count')['IDCliente']) 

