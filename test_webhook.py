import requests


user_requests ="Hi, How Are You, all ok ?"

response_message = {"message":user_requests}

url ="http://localhost:5678/webhook-test/df442a97-fe2a-4d06-99bf-282768a4c3e6"

response = requests.post(url,json=user_requests)

print(response.status_code)