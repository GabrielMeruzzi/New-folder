import pandas as pd
import json

json_data = '''
[
    {"name": "Joao", "age": 30, "city": "Sao Paulo"},
    {"name": "Maria", "age": 25, "city": "Rio de Janeiro"}
]
'''

# data = json.loads(json_data)
# df = pd.DataFrame(data)

# Lendo o JSON com Pandas (ARQUIVO)
df = pd.read_json('data.json')

# Filtra a idade >= 27
filtered_df = df[df['age'] >= 27]

# Cria um uma nova coluna todos as linhas ACTIVE
df['status'] = 'active'

# Localiza city e altera
df.loc[df['city'] == 'Sao Paulo', 'city'] = 'Paulo Sao'

df.to_json('output_records.json', orient='records', lines=True)
df.to_json('output_split.json', orient='split')
df.to_json('output_index.json', orient='index')