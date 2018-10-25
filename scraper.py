from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://treehouse-projects.github.io/horse-land/index.html')
soup = BeautifulSoup(html.read(), 'html.parser')

# div = soup.find('div', {'class': 'featured'})
# print(div)

featured_header = soup.find('div', {'class': 'featured'})
print(featured_header.get_text())
