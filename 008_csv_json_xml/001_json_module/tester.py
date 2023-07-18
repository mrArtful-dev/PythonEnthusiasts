import json

with open('sample2.json', 'r', encoding='utf8') as file:
    data = json.load(file)


for person in data["people"]:
    if not person['emails']:
        person['reminder'] = 'Please update email!'


with open('sample2_copy.json', 'w', encoding='utf8') as file:
    json.dump(data, file, indent=2, sort_keys=True)