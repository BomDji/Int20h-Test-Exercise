import requests
import time
import schedule

from datetime import datetime

from bs4 import BeautifulSoup

from mongoengine import Q

from ..db_models.shop import Shop
from ..db_models.product import Product


class ParserManager:
    URL_TEMPLATE = 'https://price.ua/{category}/page{page}.html?sort_direction=asc&sort_by=price_asc'
    CEREALS_TAG = 'catc12388t1'

    def parse_item(self, soup):
        products = soup.findAll('div', {'class': 'product-block'})

        for product in products:
            shop_name = product.find('div', {'class': 'firmname'}).text

            shop = Shop.objects(name=shop_name).first()
            if not shop:
                shop = Shop()
                shop.name = shop_name
                shop.save()

            name = product.find('span', {'class': 'ga_model_name'}).text.strip()
            description = product.find('div', {'class': 'description'}).text

            price, currency = product.find('span', {'class': 'price'}).text.split()
            price = float(price.replace(',', '.'))

            link = 'https://price.ua' + product.find('a', {'data-otc': 'price_button'}).get('href')
            img_link = product.find('span', {'class': 'photo-wrap'}).find('img').get('src')[2:]

            product = Product.objects(Q(name=name) & Q(description=description) & Q(img_link=img_link)).first()
            if not product:
                product = Product()

                product.name = name
                product.description = description
                product.price = price
                product.currency = currency
                product.img_link = img_link
                product.link = link
                product.category_tag = self.CEREALS_TAG
                product.price_history = [(datetime.utcnow(), price)]

                product.save()
            else:
                product.price = price
                product.price_history.append((datetime.utcnow(), price))
                product.save()

    def parse_worker(self):
        page = 1

        while True:
            url = self.URL_TEMPLATE.format(category=self.CEREALS_TAG, page=page)
            r = requests.get(url)

            soup = BeautifulSoup(r.text, 'lxml')

            if page != 1:
                meta_url = soup.find('meta', attrs={'property': 'og:url'}).get('content')
                current_page = int(meta_url.split('.html')[0].split('page')[1])

                if current_page < page:
                    break

            self.parse_item(soup)
            page += 1

            time.sleep(1)

    def run(self):
        self.parse_worker()

        schedule.every(2).minutes.do(self.parse_worker)

        while True:
            schedule.run_pending()
            time.sleep(1)
