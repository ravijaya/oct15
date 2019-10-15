import requests

url = 'http://google.com'

response = requests.get(url)

print(response.status_code)
print()
print(response.headers)
print()
print(response.text)