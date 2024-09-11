import pandas as pd

data = {
    "name": "Joao",
    "age": 30,
    "address": {
        "city": "São Paulo",
        "postal_code": "01234-567"
    },
    "phones": [
        {"type": "home", "number": "1234-5678"},
        {"type": "mobile", "number": "9876-5432"}
    ]
}

df = pd.json_normalize(data, 'phones', ['name', 'age', ['address', 'city'], ['address', 'postal_code']])
print(df)

