import requests
import time
from datetime import datetime
from requests.exceptions import HTTPError
import xml.etree.ElementTree as ET
import json
import random


def set_request(IP, command):
    url = 'http://'+ IP + '/cmd.cgi?cmd=' + command
    try:
        r = requests.get(url)
    except HTTPError as http_err:
        print(http_err)
    print(datetime.now(), command, r.text)


def get_request(IP):
    url = 'http://'+ IP + '/state.xml'
    try:
        r = requests.get(url)
        return r.text
    except HTTPError as http_err:
        return http_err
    

def get_status(IP):
    json_string = 'Error'
    text = get_request(IP)
    if isinstance(text,str):
        tree = ET.fromstring(text)
        data = {}
        for e in  tree.getchildren():
            data[e.tag] = e.text
        json_string = json.dumps(data)
    return(json_string)



if name == "main":
    IP = "192.168.100.101"    
    
    com_dic = {'REL':4,'OUT':12}

    while True:
        com1 = random.choice(list(com_dic.keys()))
        com2 = str(random.choice(range(1,com_dic[com1]+1)))
        com3 = random.choice(['0','1'])

        command = ','.join([com1,com2,com3])
        
        set_request(IP,command)
        time.sleep(2)
        print(get_status(IP))
        time.sleep(2)
