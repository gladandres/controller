import requests
from datetime import datetime
from requests.exceptions import HTTPError
import xml.etree.ElementTree as ET


def set_request(IP, command):
    url = 'http://'+ IP + '/cmd.cgi?cmd=' + command
    return exicute_request(url)


def get_request(IP):
    url = 'http://'+ IP + '/state.xml'
    return exicute_request(url)


def exicute_request(url):
    try:
        r = requests.get(url)
        return r.text
    except HTTPError as http_err:
        return http_err    


def get_status(IP):
    text = get_request(IP)
    if isinstance(text,str):
        tree = ET.fromstring(text)
        data = {}
        for e in  tree.getchildren():
            data[e.tag] = e.text
        return data
    return text