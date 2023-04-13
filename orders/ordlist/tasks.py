from datetime import date, timedelta
import requests
from bs4 import BeautifulSoup
import re
import logging

from celery import shared_task

from ordlist.utils import pattern_positive, pattern_negative, url_goszakupki, url_icetrade, headers
from ordlist.models import DataIcetrade, DataGoszakupki


logger = logging.getLogger(__name__)


@shared_task
def get_data_from_icetrade():
    logger.info("Выполняю задачу get_data_from_icetrade")
    response = requests.get(url_icetrade, headers=headers, verify=False)
    src = response.text
    for i in range(1, 2):
        soup = BeautifulSoup(src, "lxml")
        rows = soup.select("#auctions-list tr")[1:]
        for row in rows:
            if not re.search(pattern_positive, row.a.text):
                continue
            if re.search(pattern_negative, row.a.text):
                continue
            if DataIcetrade.objects.filter(link=row.a.get("href"), date=date.today()):
                continue
            logger.info("Save in BD")
            DataIcetrade.objects.create(name=row.a.text.strip(),
                                        link=row.a.get("href"),
                                        deadline=row.select_one('td:nth-child(6)').text,
                                        price=float(row.select_one('td:nth-child(5)').text.strip()[:-3].replace(' ', '')),
                                        abbreviation=row.select_one('td:nth-child(5)').text.strip()[-3:],
                                        date=date.today())


@shared_task()
def get_data_from_goszakupki():
    logger.info("Выполняю задачу get_data_from_goszakupki")
    response = requests.get(url_goszakupki, headers=headers, verify=False)
    src = response.text
    last_page = int(BeautifulSoup(src, "lxml").find(class_="last").text)
    for i in range(1, last_page + 1):
        response = requests.get(url_goszakupki + "&page=" + str(i), headers=headers, verify=False)
        soup = BeautifulSoup(response.text, "lxml")
        rows = soup.select("tbody tr")
        for row in rows:
            if row.select_one('td:nth-child(4)').text == "Подача предложений":
                if not re.search(pattern_positive, row.a.text):
                    continue
                if re.search(pattern_negative, row.a.text):
                    continue
                if DataGoszakupki.objects.filter(link="https://goszakupki.by" + row.a.get('href'),
                                                 date=date.today()):
                    continue
                logger.info("Save in BD")
                DataGoszakupki.objects.create(name=row.a.text.strip(),
                                              link="https://goszakupki.by" + row.a.get('href'),
                                              deadline=row.select_one('td:nth-child(5)').text,
                                              price=float(row.select_one('td:nth-child(6)').text.strip()[:-3].replace(' ', '')),
                                              abbreviation=row.select_one('td:nth-child(6)').text.strip()[-3:],
                                              date=date.today())


@shared_task()
def delete_records_ice():
    logger.info("Delete form DataIcetrade records")
    DataIcetrade.objects.filter(date__lt=date.today()-timedelta(days=1)).delete()


@shared_task()
def delete_records_gos():
    logger.info("Delete form DataGoszakupki records")
    DataGoszakupki.objects.filter(date__lt=date.today()-timedelta(days=1)).delete()
