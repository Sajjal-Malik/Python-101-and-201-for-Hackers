import requests  # Import the requests library for making HTTP requests

# Make a GET request to httpbin.org/get endpoint
response = requests.get('http://httpbin.org/get')

# Headers contain metadata about the response (server info, content type, etc.)
# print(response.headers)  # Print all response headers
# print(response.headers['Server'])  # Print the server header specifically
# print(response.headers['Content-Type'])  # Print content type header

# Check if the request was successful (HTTP status code 200)
if response.status_code == 200:
    print("Successfully loaded the response")
else:
    print("Error loading Content")

# Cookies are small pieces of data stored by the browser
# print(response.cookies)  # Print any cookies sent back by the server

# URL shows the final URL after any redirects
# print(response.url)  # Print the final URL of the response

# Make a GET request with query parameters and custom headers
new_response = requests.get(
    'http://httpbin.org/get',  # Target URL
    params={'id': 1},  # Query parameters (appended as ?id=1)
    # Request header indicating we prefer JSON response
    headers={'Accept': 'application/json'}
)

print(new_response.text)  # Print the response body content
print(new_response.headers)  # Print the response headers
print(new_response.url)  # Print the complete URL with query parameters

# Example of a DELETE request (commented out)
# del_response = requests.delete('http://httpbin.org/get', params={'id':1}, headers={'Accept': 'application/json'})
# print(del_response)

# Example of a POST request (commented out)
# post_response = requests.post('http://httpbin.org/get', params={'id':1}, headers={'Accept': 'application/json'})
# print(post_response)

# Create a session to persist cookies across multiple requests
session_request = requests.session()  # Create a session object
# Add a custom cookie to the session
session_request.cookies.update({'username': 'dm'})

# Make a request using the session - cookies will be automatically included
print(session_request.get('http://httpbin.org/cookies').text)
# This will show the cookies we sent, as httpbin.org/cookies echoes back received cookies
