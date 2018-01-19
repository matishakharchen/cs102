import requests
import config


def get_page(group, week=''):
    if week:
        week = str(week) + '/'
    url = 'http://www.ifmo.ru/ru/schedule/0/K3140/raspisanie_zanyatiy_K3140.htm'.format(
        domain=config.domain, 
        week=week, 
        group=group)
    response = requests.get(url)
    web_page = response.text
    return web_page
