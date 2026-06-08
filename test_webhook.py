import requests
user_message = 'Cn you tell me about black holes in 3-4 lines?'

request_message = {'message':user_message}
url = "http://localhost:5678/webhook-test/07f60269-d048-4724-b45a-64d999af8f84"
response = requests.post(url,json=request_message)
print(response.status_code)
print(response.json()[0]['output'])

