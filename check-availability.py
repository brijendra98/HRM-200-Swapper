import requests
from bs4 import BeautifulSoup
import time

while True:
    # getting the page for enrollment data
    r = requests.get('http://www.adm.uwaterloo.ca/cgi-bin/cgiwrap/infocour/salook.pl?level=under&sess=1179&subject=HRM&cournum=200',timeout=5)

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


    if enrl_cap > enrl_tot:
        if enrl_cap_two > enrl_tot_two:
            #ENROLL
		    print ("ENROLLED")
        elif subs(enrl_cap_env,enrl_tot_env) + subs(enrl_cap_mat,enrl_tot_mat) + subs(enrl_cap_rec,enrl_tot_rec) + subs(enrl_cap_erg,enrl_tot_erg) < subs(enrl_cap,enrl_tot):
		    #ENROLL
		    print("ENROLLED")
        else:
            #Course full. Check again
            print("COURSE FULL")
    else:
        #Course full. Check again
        print("COURSE FULL")
    time.sleep(0.7)
