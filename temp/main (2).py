import requests
from bs4 import BeautifulSoup

link = "https://www.ilmateenistus.ee/ilm/ilmavaatlused/vaatlusandmed/oopaevaandmed/"
page = requests.get(link)
soup = BeautifulSoup(page.content, "html.parser")
table = soup.find("table", class_="table")
tbody = table.find("tbody")
rows = tbody.find_all("tr")
table_headers = ["Jaam", "Õhutemperatuur (°C) keskmine", "Õhutemperatuur (°C) max", "Õhutemperatuur (°C) min",
                 "Maapinna minimaalne temperatuur (°C)", "Minimaalne temperatuur 2cm kõrgusel maapinnast (°C)",
                 "Suhteline õhuniiskus (%) keskmine", "Suhteline õhuniiskus (%) min", "Tuule kiirus (m/s) keskmine",
                 "Tuule kiirus (m/s) max", "Sademed (mm)", "Päikesepaiste kestus (h)"]
for row in rows:
    cells = row.find_all('td')
    info = ""
    for index, cell in enumerate(cells):
        text = cell.text
        if text != "":
            info += f"{table_headers[index]}: {text}\t\t"
    print(info)

