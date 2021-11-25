import requests

url = "http://localhost:5000/"

# response = requests.get(url + 'employees/1')

# print(response.json())

res = requests.post(url + 'employees/', json={'jobTitle': 'musician', 'firstName': 'Tom', 'lastName': 'John'})
print(res.json())

res = requests.get(url + 'employees/')

print(res.json())