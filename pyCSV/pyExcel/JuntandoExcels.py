import pandas as pd

df1 = pd.read_excel('file3.xlsx', sheet_name='Pessoas')
df2 = pd.read_excel('file4.xlsx', sheet_name='Avaliações')

# Combinar na vertical

# combined_vertical = pd.concat([df1, df2], ignore_index=True)
# combined_vertical.to_excel('combined_vertical.xlsx', index=False)

# MERGE
""" 
merged_df = pd.merge(df1,df2, on='ID', how='inner')
merged_df.to_excel('merged.xlsx', index=False)
"""
# JOIN
""" 
df1 = df1.join(df2.set_index("ID"), on='ID', lsuffix='_left', rsuffix='_right')
df1.to_excel('joined.xlsx', index=False)
"""

# VERTICAL
""" 
combined_horizontal = pd.concat([df1, df2], axis=1)
combined_horizontal.to_excel('combined_horizontal.xlsx', index=False)
"""

