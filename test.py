import requests

url = 'http://127.0.0.1:5000/predict'
headers = {'Content-Type': 'application/json; charset=utf-8'}

data = {
    'text':'يشير تقرير الهيئة الحكومية الدولية المعنية بتغير المناخ لعام 2021 بشأن العلوم الفيزيائية إلى أن تغير المناخ واسع النطاق وسريع ومكثف، ويؤكد على الضرورة الملحة لإجراء تخفيضات قوية ومستدامة في انبعاثات غازات الدفيئة.'
    }

response = requests.post(url, headers=headers, json=data)

# Process the response
response_data = response.json()
print(response_data)