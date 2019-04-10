#!/bin/python3
import base64
import requests
from bs4 import BeautifulSoup
link = 'https://brisim.bri.co.id/'

for i in range(1,201):
    html = requests.get(link, verify=False).text
    htmlsoup = BeautifulSoup(html, features='lxml')
    html_jpeg = htmlsoup.findAll('img', {'id':'imgCaptId'})
    imgstring = html_jpeg[0]['src'].replace('data:image/jpg;base64,','')
    imgdata = base64.b64decode(imgstring)
    filename = 'captcha_images/file'+str(i)+'.jpg'
    with open(filename, 'wb') as f:
        f.write(imgdata)
    f.close()
