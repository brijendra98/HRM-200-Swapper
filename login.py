import requests
from lxml import html
from bs4 import BeautifulSoup
import config

USERNAME = config.credentials['userid']
PASSWORD = config.credentials['password']

LOGIN_URL = "https://quest.pecs.uwaterloo.ca/psp/SS/"
URL = "https://quest.pecs.uwaterloo.ca/psc/SS/ACADEMIC/SA/c/SA_LEARNER_SERVICES.SSS_STUDENT_CENTER.GBL?Page=SSS_STUDENT_CENTER&Action=U&TargetFrameName=None"

def main():
    session_requests = requests.session()

    # Get login csrf token
    result = session_requests.get(LOGIN_URL)

    # Create payload
    payload = {
        "userid": USERNAME,
        "pwd": PASSWORD,
    }

    # Perform login
    result = session_requests.post(LOGIN_URL, data = payload, headers = dict(referer = LOGIN_URL))

    # Scrape url
    result = session_requests.get(URL)
    webpage = result.text
    soup = BeautifulSoup(webpage, 'html.parser')
    print(soup.prettify())

if __name__ == '__main__':
    main()
