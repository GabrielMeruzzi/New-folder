import json
import pandas as pd
from datetime import datetime

df = pd.read_json('exerc1.json')
print(df)


df['date_of_sale'] = pd.to_datetime(df['date_of_sale'])

df2024 = df[df['date_of_sale'].dt.year == 2024]
print(df2024)

df2024['total_revenue'] = df2024['sale_price'] * df2024['quantity_sold']

print(df2024)







