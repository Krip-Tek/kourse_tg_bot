import requests

url = 'https://opentdb.com/api.php?amount=10'

response = requests.get(url)

if response.status_code == 200:
    print(response.text)
else:
    print(response.status_code)

