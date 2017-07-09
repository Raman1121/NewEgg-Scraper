from urllib.request import urlopen
from bs4 import BeautifulSoup

my_url = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20cards'

uclient = urlopen(my_url)
page_html = uclient.read()
uclient.close()

page_soup = BeautifulSoup(page_html, "html.parser")
containers = page_soup.findAll("div", {"class":"item-container"})

filename = "products.csv"
f = open(filename, "w")

headers = "brand, product_name, shipping\n"
f.write(headers)

for container in containers:
	brand = container.div.div.a.img["title"]
	title_container = container.findAll("a", {"class": "item-title"})
	product_name = title_container[0].text
	shipping_container = container.findAll("li", {"class":"price-ship"})
	shipping = shipping_container[0].text.strip()

	print("brand" + brand)
	print("product_name" + product_name)
	print("shipping" + shipping)

	f.write(brand + "," + product_name.replace("," , "|") + "," + shipping + "\n")


f.close();