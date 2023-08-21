BASE_URL = "https://www.flipkart.com"


class Product:
    def __init__(self, **kwargs):
        self.name = kwargs.get('name')
        self.image = kwargs.get('image')
        self.price = kwargs.get('price')
        # self.spcification = kwargs.get('spcification')
        self.rating = kwargs.get('rating')
        self.detail_url = f"{BASE_URL}{kwargs.get('detail_url')}"


class DefaultProduct:
    def __init__(self, **kwargs):
        self.name = kwargs.get('name')
        self.subtitle = kwargs.get('subtitle')
        self.image = kwargs.get('image')
        self.offer_info = kwargs.get('offer_info')
        self.detail_url = f"{BASE_URL}{kwargs.get('detail_url')}"
