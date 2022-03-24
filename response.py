import requests
import re

url1 = input()
url2 = input()
response = requests.get(url1)


regex = r"(https?://[\w\./]+)"
url_lst = re.findall(regex, response.text)
for urls in url_lst:
    responseCheck = requests.get(urls)
    url_check = re.findall(regex, responseCheck.text)
    if url2 in url_check:
        print("Yes")
        break
else:
    print('No')
