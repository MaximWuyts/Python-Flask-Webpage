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

for container in containers:
    try:
        Name = container.img["alt"]
        print(Name)
    except TypeError:
        pass

    title_container = container.findAll("a", {"class": "item-title"})
    product_name = title_container[0].text

    old_price_container = container.findAll(
        "span", {"class": "price-was-data"})
    old_price = old_price_container[0].text

    current_price_container = container.findAll(
        "li", {"class": "price-current"})
    current_price = current_price_container[0].text[2:8]

    total_ratings = container.div.span[0].text

    print("brand: " + brand)
    print("product_name: " + product_name)
    print("old_price: " + old_price)
    print("current_price: " + current_price)
