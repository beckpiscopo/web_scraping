from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.ontheissues.org/states/AR.htm')
soup = BeautifulSoup(html.read(), 'html.parser')

# div = soup.find('div', {'class': 'featured'})
# print(div)

# featured_header = soup.find('div', {'class': 'featured'})
# print(featured_header.get_text())

#for button in soup.find(attrs={'class': 'button button--primary'}): 
#   print(button)

for link in soup.find_all('a'): 
    print(link.get('href'))
