import requests
from bs4 import BeautifulSoup

r = requests.get(
    'http://www.adm.uwaterloo.ca/cgi-bin/cgiwrap/infocour/salook.pl?level=under&sess=1179&subject=HRM&cournum=200',
    timeout=5
)

webpage = r.text
soup = BeautifulSoup(webpage, 'html.parser')
element = soup.findAll('td')
print(element)
