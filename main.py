import requests
import os
import argparse
from urllib.parse import urlparse
from dotenv import load_dotenv
load_dotenv()


def shorten_link(token, url):
    headers = {'Authorization': token}
    long_url = {"long_url": url}
    response = requests.post('https://api-ssl.bitly.com/v4/bitlinks',
                             headers=headers, json=long_url)
    response.raise_for_status()
    return response.json()['id']


def is_bitlink(token, url):
    headers = {'Authorization': token}
    response = requests.get(f'https://api-ssl.bitly.com/v4/bitlinks/{url}',
                            headers=headers)
    return response.ok


def count_clicks(token, link):
    headers = {'Authorization': token}
    params = {'unit': 'day', 'units': '-1'}
    response = requests.get(f'https://api-ssl.bitly.com/v4/bitlinks/{link}/clicks/summary',
                            headers=headers, params=params)
    response.raise_for_status()
    return response.json()['total_clicks']


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Сокращает url и выводит количество кликов по сокращенному url'
    )
    parser.add_argument('url', help='Ваш url')
    user_url = parser.parse_args().url
    token = os.environ['BITLY_TOKEN']
    parsed_url = urlparse(user_url)
    assembled_link = f"{parsed_url.netloc}{parsed_url.path}"

    try:
        if is_bitlink(token, assembled_link):
            print('По Вашей ссылке прошли:', count_clicks(token, assembled_link),
                  'раз(а)')
        else:
            print('Битлинк:', shorten_link(token, user_url))
    except requests.exceptions.HTTPError:
        print('Ошибка! Некорректная ссылка')