import time
import requests

site_url = 'https://products.markit.com/indices/'
auth_url = 'https://products.markit.com/home/signOn'
file_url = 'https://products.markit.com/indices/data/DataOutputExcel.xls?queryID=DWmembers&isd_index=I12100042&family=ib%5FEUR' \
      '&app=excel&date=07%2E09%2E2018&fixing=EU%5FEOD&Level0=EUR&return=TRi&key=ISIN&bondtype=1'

username = '*'
password = '*'
data={'username': username, 'password': password}

s = requests.Session()
r = s.post(auth_url, data=data)
time.sleep(10)
r.raise_for_status()
print(r.url)
print(r.status_code)
# print(r.content)
# print(r.headers)
for cookie in s.cookies:
    print (cookie.name, cookie.value)

# r = s.get(site_url)
# time.sleep(10)
# r.raise_for_status()
# print(r.url)
# print(r.status_code)
# for cookie in s.cookies:
#     print (cookie.name, cookie.value)

r = s.get(file_url, allow_redirects=True)
r.raise_for_status()
print(r.url)
print(r.status_code)
for cookie in s.cookies:
    print (cookie.name, cookie.value)
file = open('file.txt', 'wb')
file.write(r.content)
print(r.text)