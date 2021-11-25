import requests

url = 'http://127.0.0.1:5000/'

# res = requests.get(url + 'employees/4')
# print(res.json())
# res = requests.get(url + 'employees')
# print(res.json())

# res = requests.post(url + 'employees', 
# 					data={
# 						'userId': '4',
# 						'jobTitle':'Program Manager',
# 						"firstName": "Paul",
# 						"lastName": "Lennon",
# 					})
# print(res.json())


# del_res = requests.delete(url + 'employees/3')
# print(del_res.json())

# res = requests.get(url + 'employees')
# print(res.json())

res = requests.put(url + 'employees/2', data={'firstName': 'Ken'})
print(res.json())