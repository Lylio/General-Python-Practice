import requests

# This code snippet was generated by Postman
# Enter the URL https://jsonplaceholder.typicode.com/todos/1
# Choose Bearer token in Authorization type
# Click on code (next to cookies) and generate in Python

url = "https://jsonplaceholder.typicode.com/todos/1"

payload = ""
headers = {
    'cache-control': "no-cache",
    'Postman-Token': "7d31dbae-c175-43c5-a159-05e10b2a3452"
    }

response = requests.request("GET", url, data=payload, headers=headers)

print(response.text)
