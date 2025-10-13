import requests

response = requests.get("https://www.microsoft.com")
print(response.content)
