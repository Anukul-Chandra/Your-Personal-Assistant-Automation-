import requests


user_requests ="Can You Hear me ?"

response_message = {"message":user_requests}

url ="http://localhost:5678/webhook-test/df442a97-fe2a-4d06-99bf-282768a4c3e6"

response = requests.post(url,json=response_message)

print(response.status_code)
#print(response.json())
#print(response.text)
print(response.json()[0]['output'])