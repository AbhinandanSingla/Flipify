from product import Product
from scrapper import (search_products,
                      dataframe_to_object
                      )

searched_products = []
df = search_products("Red kurta with pant")
for _, row in df.iterrows():
    searched_products.append(dataframe_to_object(Product, row))

print(searched_products[0].name, searched_products[0].price, searched_products[0].image,
      searched_products[0].detail_url)
