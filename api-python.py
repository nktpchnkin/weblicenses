import os
import requests
import json

domain = requests.get('https://api.ipify.org').text #получаем IP адрес (Его указывать при создании лицензии! Узнать можно свой IP На сайте 2ip.ru)
license = 26 #Номер лицензии
sign = input("Введите ваш лицензионный ключ: ") #Лицензионный ключ (Например: U2B6-5BTO-VCEP-JNRG)
str_params = {'domain': domain, 'license': license, 'sign': str(sign)}
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36'}
response = requests.get("https://instaplanet.online/api", params = str_params, headers = headers).json()
if response['status'] != 200:
	print(response['message'])
else:
	print("Лицензионный ключ верный! Приятной работы =)")
