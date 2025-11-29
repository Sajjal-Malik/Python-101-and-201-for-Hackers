import requests

response = requests.get('http://httpbin.org/get')

# print(response.headers)
# print(response.headers['Server'])
# print(response.headers['Content-Type'])

if response.status_code == 200:
    print("Successfully loaded the response")
else:
    print("Error loading Content")


# print(response.cookies)
# print(response.url)


new_response = requests.get(
    'http://httpbin.org/get', params={'id': 1}, headers={'Accept': 'application/json'})

print(new_response.text)
print(new_response.headers)
print(new_response.url)


# del_response = requests.delete('http://httpbin.org/get', params={'id':1}, headers={'Accept': 'application/json'})
# print(del_response)

# post_response = requests.post('http://httpbin.org/get', params={'id':1}, headers={'Accept': 'application/json'})
# print(post_response)


session_request = requests.session()
session_request.cookies.update({'username': 'dm'})
print(session_request.get('http://httpbin.org/cookies').text)
