from requests import get
from bs4 import BeautifulSoup

result = []
#address = input()
def get_urls(address='https://habrahabr.ru'):
	r = get(address)
	domain = r.url.split("/")[2]
	soup = BeautifulSoup(r.content, 'lxml')
	links = soup.find_all("a", href=True)
	for i in links:
		if not domain in i["href"] and not i["href"].startswith("/"):
			result.append(i["href"])
	print(result)

get_urls()
