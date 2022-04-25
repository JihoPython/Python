import requests


r = requests.get('https://www.naver.com')

print(r.text)