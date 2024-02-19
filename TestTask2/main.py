import json

def readJson(str_json):
    list = []
    if 'children' in str_json:
        body = str_json['children']
    else:
        body = str_json

    for item in body:
        list.append((item['title'], item['id']))
        if 'children' in item:
            temp = readJson(item['children'])
            list.extend(temp)
    return list

with open('./src/new_test_hw.json', 'r', encoding='utf-8') as file_json:
    file_data = json.load(file_json)

data = tuple(readJson(file_data))
print(len(data))
for i in range(0,10):
    print(data[i])