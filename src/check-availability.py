import requests
import time
from bs4 import BeautifulSoup
#from twilio.rest import Client
import sys
sys.path.insert(0, '../config')
import config

#account_sid = config.twilio['account_sid']
#auth_token = config.twilio['auth_token']
#client = Client(account_sid, auth_token)

while True:
    # getting the page for enrollment data
    try:
        r = requests.get('http://www.adm.uwaterloo.ca/cgi-bin/cgiwrap/infocour/salook.pl?level=under&sess=1179&subject=HRM&cournum=200',timeout=5)
    except requests.exceptions.RequestException as e:
        print e
        time.sleep(120)
	continue
    webpage = r.text
    soup = BeautifulSoup(webpage, 'html.parser')
    element = soup.findAll('td')

    # defining required values
    enrl_cap = int(element[12].text)
    enrl_tot = int(element[13].text)
    enrl_cap_env = int(element[20].text)
    enrl_tot_env = int(element[21].text)
    enrl_cap_mat = int(element[27].text)
    enrl_tot_mat = int(element[28].text)
    enrl_cap_rec = int(element[34].text)
    enrl_tot_rec = int(element[35].text)
    enrl_cap_erg = int(element[41].text)
    enrl_tot_erg = int(element[42].text)
    enrl_cap_two = int(element[48].text)
    enrl_tot_two = int(element[49].text)

    def subs(x,y):
        if x - y > 0:
            return x - y
        else:
            return 0

    def available(criteria):
         #message = client.messages.create(
        #             to = config.twilio['to'],
            #         from_ = config.twilio['from_'],
            #         body  = "Spot Empty in HRM 200 through "+criteria+" Criteria. ENROLL FAST!"
            #        )
         print ("SPOT AVAILABLE. MESSAGE SENT")


    if enrl_cap > enrl_tot:
        if enrl_cap_two > enrl_tot_two:
             available("2nd Year Reserve")
             break
        elif subs(enrl_cap_env,enrl_tot_env) + subs(enrl_cap_mat,enrl_tot_mat) + subs(enrl_cap_rec,enrl_tot_rec) + subs(enrl_cap_erg,enrl_tot_erg) < subs(enrl_cap,enrl_tot):
             available("General")
             break

    #Course full. Check again
    print("COURSE FULL")
    time.sleep(10)
