from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = "https://www.newegg.com/global/be-en/Cell-Phones/Category/ID-450"

# opening up connection, grabbing the page
uClient = uReq(my_url)

# offload content into variable
page_html = uClient.read()

# close the file
uClient.close()

# html parsing
page_soup = soup(page_html, "html.parser")

# grabs each product
containers = page_soup.findAll("div", {"class": "item-container"})

filename = "products.csv"
f = open(filename, "w")

headers = "brand; product_name; old_price; current_price; total_ratings\n"

f.write(headers)

for container in containers:
    brand_container = container.findAll("a", {"class": "item-brand"})
    brand = brand_container[0].img["title"]

    title_container = container.findAll("a", {"class": "item-title"})
    product_name = title_container[0].text

    old_price_container = container.findAll("li", {"class": "price-was"})
    old_price = old_price_container[0].text[10:16]

    current_price_container = container.findAll(
        "li", {"class": "price-current"})
    current_price = current_price_container[0].text[3:8]

    total_ratings_container = container.findAll(
        "span", {"class": "item-rating-num"})
    total_ratings = total_ratings_container[0].text[1:3]

    print("brand: " + brand)
    print("product_name: " + product_name)
    print("old_price: €" + old_price)
    print("current_price: €" + current_price)
    print("total of ratings: " + total_ratings)

    f.write(brand + ";" + product_name.replace(",", "|") + ";" +
            old_price + ";" + current_price + ";" + total_ratings + "\n")

f.close()
