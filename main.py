from bs4 import BeautifulSoup
import requests
from datetime import datetime
import time
import json
import re
from fake_useragent import FakeUserAgent

desc_title_video_cards_bot = []
desc_price_video_cards_bot = []
desc_data_video_cards_bot = []
desc_url_video_cards_bot = []


def get_first_desc_video_cards():
    url = "https://www.avito.ru/ulyanovsk/tovary_dlya_kompyutera/komplektuyuschie/videokarty-ASgBAgICAkTGB~pm7gmmZw?cd=1&p=1"

    headers = {
        "accept": "*/*",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 YaBrowser/21.8.3.607 Yowser/2.5 Safari/537.36 "
    }
    r = requests.get(url=url, headers=headers, timeout=5)

    soup = BeautifulSoup(r.text, "lxml")
    avito_desc = soup.find_all("div", class_="iva-item-root-Nj_hb")

    desc_dict_video_cards = {}
    
    for avito in avito_desc:
        desc_title = avito.find("h3", class_="title-root-j7cja").text.strip()
        desc_price = avito.find("span", class_="price-text-E1Y7h").text.strip()
        desc_data = avito.find("div", class_="date-text-VwmJG").text.strip()

        desc_get_url = avito.find("a", class_="link-link-MbQDP")
        desc_url = f"https://www.avito.ru{desc_get_url['href']}"

        split_id = desc_url.split("/")[-1]
        desc_id_str = str(split_id.split("_")[-1])
        desc_id = str(desc_id_str.split('?')[:1])

        desc_title_video_cards_bot.append(desc_title)
        desc_price_video_cards_bot.append(desc_price)
        desc_data_video_cards_bot.append(desc_data)
        desc_url_video_cards_bot.append(desc_url)

        desc_dict_video_cards[desc_id] = {
            "title": desc_title,
            "price": desc_price,
            "data": desc_data,
            "url": desc_url
        }
        with open('db/video_cards.json', 'w', encoding='utf-8') as file:
            json.dump(desc_dict_video_cards, file, indent=5, ensure_ascii=False)


def check_video_cards_desc_update():
    with open('db/video_cards.json', 'r', encoding='utf-8') as file:
        desc_list = json.load(file)

    url = "https://www.avito.ru/ulyanovsk/tovary_dlya_kompyutera/komplektuyuschie/videokarty-ASgBAgICAkTGB~pm7gmmZw?cd=1&p=1"

    headers = {
        "accept": "*/*",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 YaBrowser/21.8.3.607 Yowser/2.5 Safari/537.36 "
    }
    r = requests.get(url=url, headers=headers)

    soup = BeautifulSoup(r.text, "lxml")
    avito_desc = soup.find_all("div", class_="iva-item-root-Nj_hb")

    desc_dict_video_cards = {}

    for avito in avito_desc:
        desc_get_url = avito.find("a", class_="link-link-MbQDP")
        desc_url = f"https://www.avito.ru{desc_get_url['href']}"

        split_id = desc_url.split("/")[-1]
        desc_id_str = str(split_id.split("_")[-1])
        desc_id = str(desc_id_str.split('?')[:1])

        if desc_id in desc_list:
            continue
        else:
            desc_title = avito.find("h3", class_="title-root-j7cja").text.strip()
            desc_price = avito.find("span", class_="price-text-E1Y7h").text.strip()
            desc_data = avito.find("div", class_="date-text-VwmJG").text.strip()

            desc_get_url = avito.find("a", class_="link-link-MbQDP")
            desc_url = f"https://www.avito.ru{desc_get_url['href']}"

            split_id = desc_url.split("/")[-1]
            desc_id_str = str(split_id.split("_")[-1])
            desc_id = str(desc_id_str.split('?')[:1])

            desc_dict_video_cards[desc_id] = {
                "title": desc_title,
                "price": desc_price,
                "data": desc_data,
                "url": desc_url
            }

            desc_title_video_cards_bot .append(desc_title)
            desc_price_video_cards_bot.append(desc_price)
            desc_data_video_cards_bot.append(desc_data)
            desc_url_video_cards_bot.append(desc_url)

    with open('db/video_cards.json', 'w', encoding='utf-8') as file:
        (json.dump(desc_dict_video_cards, file, indent=5, ensure_ascii=False))

    return desc_list


desc_title_cpu_bot = []
desc_price_cpu_bot = []
desc_data_cpu_bot = []
desc_url_cpu_bot = []


def get_first_desc_cpu():

    url = "https://www.avito.ru/ulyanovsk/tovary_dlya_kompyutera/komplektuyuschie/protsessory-ASgBAgICAkTGB~pm7gniZw?cd=1&p=1"

    headers = {
        "accept": "*/*",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 YaBrowser/21.8.3.607 Yowser/2.5 Safari/537.36 "
    }
    r = requests.get(url=url, headers=headers, timeout=5)

    soup = BeautifulSoup(r.text, "lxml")
    avito_desc = soup.find_all("div", class_="iva-item-root-Nj_hb")

    desc_dict_cpu = {}

    for avito in avito_desc:
        desc_title = avito.find("h3", class_="title-root-j7cja").text.strip()
        desc_price = avito.find("span", class_="price-text-E1Y7h").text.strip()
        desc_data = avito.find("div", class_="date-text-VwmJG").text.strip()

        desc_get_url = avito.find("a", class_="link-link-MbQDP")
        desc_url = f"https://www.avito.ru{desc_get_url['href']}"

        split_id = desc_url.split("/")[-1]
        desc_id_str = str(split_id.split("_")[-1])
        desc_id = str(desc_id_str.split('?')[:1])

        desc_title_cpu_bot.append(desc_title)
        desc_price_cpu_bot.append(desc_price)
        desc_data_cpu_bot.append(desc_data)
        desc_url_cpu_bot.append(desc_url)

        desc_dict_cpu[desc_id] = {
            "title": desc_title,
            "price": desc_price,
            "data": desc_data,
            "url": desc_url
        }
        with open('db/cpu.json', 'w', encoding='utf-8') as file:
            (json.dump(desc_dict_cpu, file, indent=5, ensure_ascii=False))


def check_cpu_desc_update():
    with open('db/cpu.json', 'r', encoding='utf-8') as file:
        desc_list = json.load(file)

    url = "https://www.avito.ru/ulyanovsk/tovary_dlya_kompyutera/komplektuyuschie/protsessory-ASgBAgICAkTGB~pm7gniZw?cd=1&p=1"

    headers = {
        "accept": "*/*",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 YaBrowser/21.8.3.607 Yowser/2.5 Safari/537.36 "
    }
    r = requests.get(url=url, headers=headers)

    soup = BeautifulSoup(r.text, "lxml")
    avito_desc = soup.find_all("div", class_="iva-item-root-Nj_hb")

    desc_dict_cpu = {}

    for avito in avito_desc:
        desc_get_url = avito.find("a", class_="link-link-MbQDP")
        desc_url = f"https://www.avito.ru{desc_get_url['href']}"

        split_id = desc_url.split("/")[-1]
        desc_id_str = str(split_id.split("_")[-1])
        desc_id = str(desc_id_str.split('?')[:1])

        if desc_id in desc_list:
            continue
        else:
            desc_title = avito.find("h3", class_="title-root-j7cja").text.strip()
            desc_price = avito.find("span", class_="price-text-E1Y7h").text.strip()
            desc_data = avito.find("div", class_="date-text-VwmJG").text.strip()

            desc_get_url = avito.find("a", class_="link-link-MbQDP")
            desc_url = f"https://www.avito.ru{desc_get_url['href']}"

            split_id = desc_url.split("/")[-1]
            desc_id_str = str(split_id.split("_")[-1])
            desc_id = str(desc_id_str.split('?')[:1])

            desc_dict_cpu[desc_id] = {
                "title": desc_title,
                "price": desc_price,
                "data": desc_data,
                "url": desc_url
            }

            desc_title_cpu_bot.append(desc_title)
            desc_price_cpu_bot.append(desc_price)
            desc_data_cpu_bot.append(desc_data)
            desc_url_cpu_bot.append(desc_url)

    with open('db/cpu.json', 'w', encoding='utf-8') as file:
        (json.dump(desc_dict_cpu, file, indent=5, ensure_ascii=False))

    return desc_list


desc_title_motherboard_bot = []
desc_price_motherboard_bot = []
desc_data_motherboard_bot = []
desc_url_motherboard_bot = []


def get_first_desc_motherboard():

    url = "https://www.avito.ru/ulyanovsk/tovary_dlya_kompyutera/komplektuyuschie/materinskie_platy-ASgBAgICAkTGB~pm7gnOZw?cd=1&p=1"

    headers = {
        "accept": "*/*",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 YaBrowser/21.8.3.607 Yowser/2.5 Safari/537.36 "
    }
    r = requests.get(url=url, headers=headers, timeout=5)

    soup = BeautifulSoup(r.text, "lxml")
    avito_desc = soup.find_all("div", class_="iva-item-root-Nj_hb")

    desc_dict_cpu = {}

    for avito in avito_desc:
        desc_title = avito.find("h3", class_="title-root-j7cja").text.strip()
        desc_price = avito.find("span", class_="price-text-E1Y7h").text.strip()
        desc_data = avito.find("div", class_="date-text-VwmJG").text.strip()

        desc_get_url = avito.find("a", class_="link-link-MbQDP")
        desc_url = f"https://www.avito.ru{desc_get_url['href']}"

        split_id = desc_url.split("/")[-1]
        desc_id_str = str(split_id.split("_")[-1])
        desc_id = str(desc_id_str.split('?')[:1])

        desc_title_motherboard_bot.append(desc_title)
        desc_price_motherboard_bot.append(desc_price)
        desc_data_motherboard_bot.append(desc_data)
        desc_url_motherboard_bot.append(desc_url)

        desc_dict_cpu[desc_id] = {
            "title": desc_title,
            "price": desc_price,
            "data": desc_data,
            "url": desc_url
        }
        with open('db/motherboard.json', 'w', encoding='utf-8') as file:
            json.dump(desc_dict_cpu, file, indent=5, ensure_ascii=False)


def check_motherboard_desc_update():
    with open('db/motherboard.json', 'r', encoding='utf-8') as file:
        desc_list = json.load(file)

    url = "https://www.avito.ru/ulyanovsk/tovary_dlya_kompyutera/komplektuyuschie/materinskie_platy-ASgBAgICAkTGB~pm7gnOZw?cd=1&p=1"

    headers = {
        "accept": "*/*",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 YaBrowser/21.8.3.607 Yowser/2.5 Safari/537.36 "
    }
    r = requests.get(url=url, headers=headers)

    soup = BeautifulSoup(r.text, "lxml")
    avito_desc = soup.find_all("div", class_="iva-item-root-Nj_hb")

    desc_dict_motherboard = {}

    for avito in avito_desc:
        desc_get_url = avito.find("a", class_="link-link-MbQDP")
        desc_url = f"https://www.avito.ru{desc_get_url['href']}"

        split_id = desc_url.split("/")[-1]
        desc_id_str = str(split_id.split("_")[-1])
        desc_id = str(desc_id_str.split('?')[:1])

        if desc_id in desc_list:
            continue
        else:
            desc_title = avito.find("h3", class_="title-root-j7cja").text.strip()
            desc_price = avito.find("span", class_="price-text-E1Y7h").text.strip()
            desc_data = avito.find("div", class_="date-text-VwmJG").text.strip()

            desc_get_url = avito.find("a", class_="link-link-MbQDP")
            desc_url = f"https://www.avito.ru{desc_get_url['href']}"

            split_id = desc_url.split("/")[-1]
            desc_id_str = str(split_id.split("_")[-1])
            desc_id = str(desc_id_str.split('?')[:1])

            desc_dict_motherboard[desc_id] = {
                "title": desc_title,
                "price": desc_price,
                "data": desc_data,
                "url": desc_url
            }

            desc_title_motherboard_bot.append(desc_title)
            desc_price_motherboard_bot.append(desc_price)
            desc_data_motherboard_bot.append(desc_data)
            desc_url_motherboard_bot.append(desc_url)

            with open('db/motherboard.json', 'w', encoding='utf-8') as file:
                json.dump(desc_dict_motherboard, file, indent=5, ensure_ascii=False)

    return desc_list

desc_title_ram_bot = []
desc_price_ram_bot = []
desc_data_ram_bot = []
desc_url_ram_bot = []


def get_first_desc_ram():

    url = "https://www.avito.ru/ulyanovsk/tovary_dlya_kompyutera/komplektuyuschie/operativnaya_pamyat-ASgBAgICAkTGB~pm7gnYZw?cd=1&p=1"

    headers = {
        "accept": "*/*",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 YaBrowser/21.8.3.607 Yowser/2.5 Safari/537.36 "
    }
    r = requests.get(url=url, headers=headers, timeout=5)

    soup = BeautifulSoup(r.text, "lxml")
    avito_desc = soup.find_all("div", class_="iva-item-root-Nj_hb")

    desc_dict_ram = {}

    for avito in avito_desc:
        desc_title = avito.find("h3", class_="title-root-j7cja").text.strip()
        desc_price = avito.find("span", class_="price-text-E1Y7h").text.strip()
        desc_data = avito.find("div", class_="date-text-VwmJG").text.strip()

        desc_get_url = avito.find("a", class_="link-link-MbQDP")
        desc_url = f"https://www.avito.ru{desc_get_url['href']}"

        split_id = desc_url.split("/")[-1]
        desc_id_str = str(split_id.split("_")[-1])
        desc_id = str(desc_id_str.split('?')[:1])

        desc_title_ram_bot.append(desc_title)
        desc_price_ram_bot.append(desc_price)
        desc_data_ram_bot.append(desc_data)
        desc_url_ram_bot.append(desc_url)

        desc_dict_ram[desc_id] = {
            "title": desc_title,
            "price": desc_price,
            "data": desc_data,
            "url": desc_url
        }
        with open('db/ram.json', 'w', encoding='utf-8') as file:
            json.dump(desc_dict_ram, file, indent=5, ensure_ascii=False)


def check_ram_desc_update():
    with open('db/ram.json', 'r', encoding='utf-8') as file:
        desc_list = json.load(file)

    url = "https://www.avito.ru/ulyanovsk/tovary_dlya_kompyutera/komplektuyuschie/operativnaya_pamyat-ASgBAgICAkTGB~pm7gnYZw?cd=1&p=1"

    headers = {
        "accept": "*/*",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 YaBrowser/21.8.3.607 Yowser/2.5 Safari/537.36 "
    }
    r = requests.get(url=url, headers=headers)

    soup = BeautifulSoup(r.text, "lxml")
    avito_desc = soup.find_all("div", class_="iva-item-root-Nj_hb")

    desc_dict_ram = {}

    for avito in avito_desc:
        desc_get_url = avito.find("a", class_="link-link-MbQDP")
        desc_url = f"https://www.avito.ru{desc_get_url['href']}"

        split_id = desc_url.split("/")[-1]
        desc_id_str = str(split_id.split("_")[-1])
        desc_id = str(desc_id_str.split('?')[:1])

        if desc_id in desc_list:
            continue
        else:
            desc_title = avito.find("h3", class_="title-root-j7cja").text.strip()
            desc_price = avito.find("span", class_="price-text-E1Y7h").text.strip()
            desc_data = avito.find("div", class_="date-text-VwmJG").text.strip()

            desc_get_url = avito.find("a", class_="link-link-MbQDP")
            desc_url = f"https://www.avito.ru{desc_get_url['href']}"

            split_id = desc_url.split("/")[-1]
            desc_id_str = str(split_id.split("_")[-1])
            desc_id = str(desc_id_str.split('?')[:1])

            desc_dict_ram[desc_id] = {
                "title": desc_title,
                "price": desc_price,
                "data": desc_data,
                "url": desc_url
            }

            desc_title_ram_bot.append(desc_title)
            desc_price_ram_bot.append(desc_price)
            desc_data_ram_bot.append(desc_data)
            desc_url_ram_bot.append(desc_url)

            with open('db/ram.json', 'w', encoding='utf-8') as file:
                json.dump(desc_dict_ram, file, indent=5, ensure_ascii=False)

    return desc_list

def main():
    get_first_desc_video_cards()
    check_video_cards_desc_update()
    get_first_desc_cpu()
    check_cpu_desc_update()
    get_first_desc_motherboard()
    check_motherboard_desc_update()
    get_first_desc_ram()
    check_ram_desc_update()


if __name__ == "__main__":
    main()
