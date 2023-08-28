import re

import pandas as pd
import requests
from bs4 import BeautifulSoup

RUPEE_AMOUNT_REGEX = r"(?:₹\d+.\d+)"

def get_search_url(search_term):
    '''Generates url for search term'''
    search_term = search_term.replace(' ', '+')
    url_template = f"https://www.flipkart.com/search?q={search_term}&sort=popularity"
    return url_template


def filterProductName(item):
    product_name = ''
    a_title = [x.get('title')
               for x in item.find_all('a') if x.get('title') is not None]
    if item.find(class_='_4rR01T'):
        product_name = item.find(class_='_4rR01T').text
    elif any(a_title):
        product_name = a_title[0]
    return product_name


def search_products(search_term):
    '''Scrapes Searched Data From Given URL'''

    url = get_search_url(search_term)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    product_containers = soup.find_all(class_="_13oc-S")

    product_names = []
    product_images = []
    product_prices = []
    product_ratings = []
    # product_specifications = []
    product_detail_urls = []

    for item in product_containers:
        # Adding Product Name In List
        product_names.append(filterProductName(item))

        # Adding Product Image In List
        product_images.append(item.find('img')['src'])

        # Adding Product Price In List
        product_prices.append(
            re.search(RUPEE_AMOUNT_REGEX, str(item.find_all('div'))).group(0))

        # Adding Product Rating In List
        product_ratings.append(item.find(class_="_3LWZlK").text if item.find(
            class_="_3LWZlK") else 'No Rating')

        # Adding Product Specification In List
        # product_specifications.append(item.find(class_="_1xgFaf"))

        # Adding Product Detail URL
        product_detail_urls.append(item.find('a')['href'])

    # Creating Dataframe

    df_dict = {
        'name': product_names,
        'image': product_images,
        'price': product_prices,
        # 'specifications': product_specifications,
        'rating': product_ratings,
        'detail_url': product_detail_urls
    }

    df = pd.DataFrame.from_dict(df_dict)

    return df


def get_default_products():

    response = requests.get("https://www.flipkart.com/offers-store")
    soup = BeautifulSoup(response.text, "html.parser")
    products_template = soup.find_all(class_="_3YgSsQ")

    title = []
    images = []
    subtitle = []
    offer_info = []
    detail_url = []

    for product in products_template:
        title.append(product.find(class_="_3LU4EM").text)
        subtitle.append(product.find(class_="_3khuHA").text)
        images.append(product.find("img")["src"])
        offer_info.append(product.find(class_="_2tDhp2").text)
        detail_url.append(product.find(class_="_6WQwDJ")["href"])

    df_dict = {
        'name': title,
        'image': images,
        'subtitle': subtitle,
        'offer_info': offer_info,
        'detail_url': detail_url
    }

    df = pd.DataFrame.from_dict(df_dict)

    return df


def dataframe_to_object(obj, values):
    '''Converts Dataframe To Python Class'''
    return obj(**values)
