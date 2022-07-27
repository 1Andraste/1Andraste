# -*- coding: utf-8 -*-
import json

import requests
from bs4 import BeautifulSoup
from data_base import sqlite3_dp
import time

# from bit import param

info = {
    'id': '',
    'nameItem': '',
    'photo': '',
    'nameSeller': '',
    'linkToPost': '',
    'linkToSeller': '',
    'brand': '',
    'price': '',
    "currency": "",
    'size': '',
    'likes': '',
    'description': '',
    'country': '',
    'views': '',
    'data': '',
    'countPost': '',
    'rate': '',
    "givenItemCount": '',
    "takenItemCount": '',
    "registration": '',
}

headers = {
    'accept': 'application/json, text/plain, */*',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36',
}


def get_page(url):
    global script2, script3, views, posted, posted3, response, response2
    try:
        response = requests.get(url, headers=headers)
    except requests.exceptions.Timeout:
        print('KILLLLLLL')
    except requests.exceptions.TooManyRedirects:
        print("NNNNNNNNNNNN")
    except requests.exceptions.RequestException:
        print('IIIIIIIIIIIIIGER')
    soup = BeautifulSoup(response.content, "html.parser")
    script = soup.find_all('script')[-2].text.strip()
    data = json.loads(script)
    ids = data['items']['catalogItems']['ids']
    for i in range(24):
        try:
            response2 = requests.get(data['items']['catalogItems']['byId'][f"{ids[i]}"]['url'], headers=headers)
        except requests.exceptions.Timeout:
            print('2KILLLLLLL')
        except requests.exceptions.TooManyRedirects:
            print("2NNNNNNNNNNNN")
        except requests.exceptions.RequestException:
            print('2IIIIIIIIIIIIIGER')
        soup2 = BeautifulSoup(response2.content, "html.parser")
        div = soup2.find_all('div')
        for k in div:
            try:
                script2 = k.find('div', class_='details-list details-list--info').find('script').text.strip()
                print("----------")
                print(type(script2))
                print("----------")
                break
            except AttributeError:
                continue
        for k in div:
            try:
                script3 = k.find('aside', class_='sidebar-container u-float-right').find('script', {
                    "data-component-name": "ItemUserInfo"}).text.strip()
                if script3 is not None:
                    print("PASSED")
                    break
            except AttributeError:
                continue
        for k in div:
            try:
                views = k.find('div', class_='details-list__item-title')
                views2 = views.findNext().text
                if views.text == "Views":
                    info['views'] = views2
                    print("PASSED")
                    break
            except AttributeError:
                continue
        for k in div:
            try:
                posted = k.find('div', class_='details-list__item-title')
                posted2 = posted.findNext().find('time').attrs['datetime']
                hours = ((-1) * (int(posted2[19:22]) - 3))
                fullData = str(f'{int(posted2[11:13]) + hours}:{posted2[14:16]} - {posted2[0:10]} ')
                info['data'] = fullData
                print("PASSED3")
            except AttributeError:
                continue
        print(i)
        print(response2)
        script2 = json.loads(script2)
        print(script2)
        script3 = json.loads(script3)
        info['country'] = script3['user']['country_title']
        info['registration'] = script3['user']['created_at']
        info['givenItemCount'] = script3['user']['given_item_count']
        info['takenItemCount'] = script3['user']['taken_item_count']
        info['description'] = script2['content']['description']
        info['countPost'] = script3['user']['item_count']
        info['rate'] = script3['user']['positive_feedback_count']
        info['id'] = data['items']['catalogItems']['byId'][f"{ids[i]}"]["id"]
        info['nameItem'] = data['items']['catalogItems']['byId'][f"{ids[i]}"]['title']
        info['photo'] = data['items']['catalogItems']['byId'][f"{ids[i]}"]['photo']['url']
        info['nameSeller'] = data['items']['catalogItems']['byId'][f"{ids[i]}"]['user']['login']
        info['linkToPost'] = data['items']['catalogItems']['byId'][f"{ids[i]}"]['url']
        info['linkToSeller'] = data['items']['catalogItems']['byId'][f"{ids[i]}"]['user']['profile_url']
        info['brand'] = data['items']['catalogItems']['byId'][f"{ids[i]}"]['brand_title']
        info['price'] = data['items']['catalogItems']['byId'][f"{ids[i]}"]['price']
        info['currency'] = data['items']['catalogItems']['byId'][f"{ids[i]}"]['currency']
        info['size'] = data['items']['catalogItems']['byId'][f"{ids[i]}"]['size_title']
        info['likes'] = data['items']['catalogItems']['byId'][f"{ids[i]}"]['favourite_count']
        with open('post.html', 'w', encoding="utf-8") as out:
            out.write(str(soup2))
        time.sleep(1)
        # sqlite3_dp.sql_add_page(info)


    # with open('post.json', 'w') as outfile:
    #     json.dump(script3, outfile, indent=4)
    # with open('data.json', 'w') as outfile:
    #     json.dump(data['items']['catalogItems'], outfile, indent=4)


def get_post(url):
    pass


def main():
    sqlite3_dp.sql_start()
    # for i in range(25):
    #     get_page(url=f"https://www.vinted.co.uk/vetements?catalog[]=1904&page={i}")
    get_page(url=f"https://www.vinted.com/vetements?catalog[]=4&order=newest_first")


if __name__ == "__main__":
    main()
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
