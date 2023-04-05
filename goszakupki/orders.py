import json
from pathlib import Path
from time import sleep
import requests
from bs4 import BeautifulSoup
from datetime import date
import re
from settings.filters import pattern_positive, pattern_negative
from settings.params import url_goszakupki, headers

folder = f"{Path(__file__).resolve().parent.name}_{date.today()}"
Path(f"{folder}").mkdir(exist_ok=True)

response = requests.get(url_goszakupki, headers=headers, verify=False)
src = response.text

last_page = int(BeautifulSoup(src, "lxml").find(class_="last").text)  # номер последней страницы
sleep(0.5)

lst = []
count = 1
for i in range(1, last_page + 1):  # проход по всем страницам и выборка нужных объявлений по
    # фильтрам (положительные и отрицательные)
    response = requests.get(url_goszakupki + "&page=" + str(i), headers=headers, verify=False)
    soup = BeautifulSoup(response.text, "lxml")
    rows = soup.select("tbody tr")
    for row in rows:
        if row.select_one('td:nth-child(4)').text == "Подача предложений":
            if not float(row.select_one('td:nth-child(6)').text[:-3].replace(' ', '')) >= 500:
                continue
            if not re.search(pattern_positive, row.a.text):
                continue
            if re.search(pattern_negative, row.a.text):
                continue
            item = {'lot': count,
                    'name': row.a.text,
                    'link': "https://goszakupki.by" + row.a.get('href'),
                    'deadline': row.select_one('td:nth-child(5)').text,
                    'price': row.select_one('td:nth-child(6)').text}
            lst.append(item)
            count += 1

amount = {"Количество": f"На {date.today()} --> {len(lst)} предложений"}
lst.insert(0, amount)
with open(f"{folder}/products_goszakupki_{date.today()}.json", "w", encoding="utf-8") as file:
    json.dump(lst, file, indent=4, ensure_ascii=False)
