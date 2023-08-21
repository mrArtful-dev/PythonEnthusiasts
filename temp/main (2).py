import csv

print('Overall rank,', 'Country or region,', 'Score,', 'Freedom to make life choices')


with open('../008_csv_json_xml/002_csv_module/csv_files/2019.csv', 'r', encoding='UTF8') as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row['Overall rank'], row['Country or region'], row['Score'], row['Freedom to make life choices'])

    top10 = sorted(reader, key=lambda x: list(x['Freedom to make life choices']), reverse=True)[:10]
    for row in top10:
        print(row['Overall rank'], row['Country or region'], row['Score'], row['Freedom to make life choices'])