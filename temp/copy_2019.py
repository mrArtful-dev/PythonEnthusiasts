import csv

print('Overall rank,', 'Country or region,', 'Score,', 'Freedom to make life choices')

with open('../Lessons_Python/homework/homework_006.csv', 'r', encoding='UTF8') as file:
    reader = csv.DictReader(file)
    for row in reader:

        top10 = sorted(reader, key=lambda x: list(x['Freedom to make life choices']), reverse=True)[:10]
        for row in top10:
            print(row['Country or region'], row['Score'], row['Freedom to make life choices'])



