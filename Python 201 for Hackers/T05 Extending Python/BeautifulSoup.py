import requests
from bs4 import BeautifulSoup

page = requests.get("https://247ctf.com/scoreboard")
print(page.text)


soup = BeautifulSoup(page.content, 'html.parser')

# print("------------- Sample Test Web Scraping Results -----------------")
# print(soup.text)
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# print(soup.find('a'))

# for link in soup.find_all('a'):
#     print(link)
#     print(link.get('href'))

# print(soup.find(id="fetch-error"))
# print(soup.find(class_="nav-link"))
# print(soup.find('a', class_="nav-link"))


# print("------------- Actual Content Web Scraping Results -----------------")
table = soup.find('table')
table_body = table.find('tbody')
rows = table_body.find_all('tr')

for row in rows:
    print("----")
    cols = [x.text.strip() for x in row.find_all('td')]
    print(f"{cols[2]} in place {cols[0]} with {cols[-2]}")
