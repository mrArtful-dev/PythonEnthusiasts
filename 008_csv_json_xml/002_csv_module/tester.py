import csv

with open('csv_files/2019.csv', 'r', encoding='utf8') as file:
    # data = csv.reader(file)
    # next(data)
    # data = list(data)

    data = csv.DictReader(file)

    analysis_data = []
    for line in data:
        analysis_data.append([line['Social support'], line['Country or region']])

    analysis_data.sort(reverse=True)

    result = []
    for line in analysis_data:
        if len(result) > 9:
            break
        result.append(line)

    for line in result:
        print(line[1], line[0])