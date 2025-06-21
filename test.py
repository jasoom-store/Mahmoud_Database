
data = [
    ('mena', 29, 'mena@m.m'),
    ('mahmoud', 34, 'mahmoud@m.m')
]

columes = [
    ('usernema', 0, 0, 0, 0, 0),
    ('age', 0, 0, 0, 0, 0),
    ('email', 0, 0, 0, 0, 0)
]

for value in data:
    print("{")
    for ind, col in enumerate(value):
        print(columes[ind][0] +": "+ str(col))
    print("}")
