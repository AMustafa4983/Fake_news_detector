import requests

url = 'http://127.0.0.1:5000/english'
headers = {'Content-Type': 'application/json; charset=utf-8'}

data = {
    'text': 'We have been cooling down for the past 4000 years”; the Earth has cooled since the ‘medieval warming’, “It’s all about when you start the measurements'
}

response = requests.post(url, headers=headers, json=data)

# Process the response
response_data = response.json()
print(response_data)