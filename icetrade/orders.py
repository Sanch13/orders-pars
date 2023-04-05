import json
from pathlib import Path
import requests
from bs4 import BeautifulSoup
from datetime import date
import re

from settings.filters import pattern_positive, pattern_negative
from settings.params import url_icetrade, headers

folder = f"{Path(__file__).resolve().parent.name}_{date.today()}"
Path(f"{folder}").mkdir(exist_ok=True)

response = requests.get(url_icetrade, headers=headers, verify=False)
src = response.text

count = 1
lst = []
for i in range(1, 2):
    soup = BeautifulSoup(src, "lxml")
    rows = soup.select("#auctions-list tr")[1:]
    for row in rows:
        if not float(row.select_one('td:nth-child(5)').text.strip()[:-3].replace(' ', '')) >= 500:
            continue
        if not re.search(pattern_positive, row.a.text):
            continue
        if re.search(pattern_negative, row.a.text):
            continue
        item = {'lot': count,
                'name': row.a.text.strip(),
                'link': row.a.get("href"),
                'deadline': row.select_one('td:nth-child(6)').text,
                'price': row.select_one('td:nth-child(5)').text.strip()}
        lst.append(item)
        count += 1

amount = {"Количество": f"На {date.today()} --> {len(lst)} предложений"}
lst.insert(0, amount)
with open(f"{folder}/products_icetrade_{date.today()}.json", "w", encoding="utf-8") as file:
    json.dump(lst, file, indent=4, ensure_ascii=False)
