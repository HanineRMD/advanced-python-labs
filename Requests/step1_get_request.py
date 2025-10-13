#import requests

#url = "https://www.microsoft.com"
#response = requests.get(url)

#print(response)
import requests

url = "https://www.microsoft.com"
response = requests.get(url)

print("Status code:", response.status_code)
