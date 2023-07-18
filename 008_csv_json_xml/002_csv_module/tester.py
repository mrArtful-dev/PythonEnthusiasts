import csv

with open('csv_files/test.csv', 'r', encoding='utf8') as file:
    data = list(csv.DictReader(file))
    headers = data[0].keys()
    data = iter(data)

    with open('csv_files/new_test.csv', 'w', encoding='utf8') as output:

        writer = csv.DictWriter(output, fieldnames=headers, lineterminator='\n')

        writer.writeheader()

        writer.writerows(data)
        # for line in data:
        #     writer.writerow(line)