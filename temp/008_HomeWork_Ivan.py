import csv
# Написать программу которая из фала "2019.csv" возьмёт топ 10 стран по любому из пунктов (не первые три)

with open('../008_csv_json_xml/002_csv_module/csv_files/2019.csv', 'r', encoding='utf8') as csv_file:
    csv_reader = list(csv.DictReader(csv_file))

while True:
    user_choise = input('1.TOP 10 GDP per capita\n'
                        '2.TOP 10 Social support\n'
                        '3.TOP 10 Healthy life expectancy\n'
                        '4.TOP 10 Freedom to make life choices\n'
                        '5.TOP 10 Generosity\n'
                        '6.TOP 10 Perceptions of corruption\n'
                        '0.Exit\n'
                        '-->')
    if user_choise == '1':
        column_name = 'GDP per capita'
    elif user_choise == '2':
        column_name = 'Social support'
    elif user_choise == '3':
        column_name = 'Healthy life expectancy'
    elif user_choise == '4':
        column_name = 'Freedom to make life choices'
    elif user_choise == '5':
        column_name = 'Generosity'
    elif user_choise == '6':
        column_name = 'Perceptions of corruption'
    elif user_choise == '0':
        print('Good bye!')
        break
    else:
        print('Choise is out of range')
    countries_data = {}
    for line in csv_reader:
        country = line['Country or region']
        value = float(line[column_name])
        countries_data[country] = value
    top_10_countries = dict(sorted(countries_data.items(), key=lambda x: x[1], reverse=True)[:10])
    for country, value in top_10_countries.items():
        print(f"{country}: {value}")




# 008230717/2019.csv/