from requests import get, put, delete

url = 'http://127.0.0.1:5000/'

data = [{"username": 'mango','email': 'abcd@efg.com'},
		{"username": 'stan','email': 'sstsn@efg.com'},
		{"username": 'lan','email': 'lan@efg.com'},]

# First import data into the db, if exist will return "User id Taken."
print('Data Import...')
for i in range(len(data)):
	response = put(url + 'users/' + str(i+1), data[i])
	print(response.json())
print('----------------------------')

print('Data Delete...')
res = delete(url + 'users/2')
print(res.json())
print('----------------------------')

res = get(url + 'users')
print(res.json())