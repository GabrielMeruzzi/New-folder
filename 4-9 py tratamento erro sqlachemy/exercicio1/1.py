c1 = {1, 2, 3}
c2 = {3, 4, 'a'}

try:
    c3 = c1.union(c2)
    for i in c3:
        if not isinstance(i, int):
            raise TypeError(f"O valor '{i}' não é um inteiro.")
except TypeError as e:
    print(e)
