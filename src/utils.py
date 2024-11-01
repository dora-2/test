import json


with open('operations.json') as f:
    data = json.load(f)

if type(data) == list:
    print(data)  # data - словарь, тип dict
else:
    print([])


