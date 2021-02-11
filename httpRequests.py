# References:
# https://realpython.com/python-requests/
# https://www.w3schools.com/tags/ref_httpmethods.asp
# https://www.geeksforgeeks.org/getpass-and-getuser-in-python-password-without-echo/
# https://docs.github.com/en/rest/reference/users#get-the-authenticated-user

# The Hypertext Transfer Protocol (HTTP) is designed to enable communications between clients and servers.
# HTTP works as a request-response protocol between a client and server.

from getpass import getpass
import requests
from requests.exceptions import HTTPError

##########################################################################
# GET request
##########################################################################
# request data from a specified resource
# can be cached
# remain in browser history
# can be bookmarked
# have length restrictions (URL length can be 2048 characters max, including GET request data)
# only ASCII characters permitted
# DO NOT USE when dealing with sensitive data
print("GET request: ", end='')
print(requests.get('https://api.github.com'))

# Loop over list of URLs with try-except
for url in ['https://api.github.com', 'https://api.github.com/invalid']:
    try:
        response = requests.get(url)

        # If the response was successful, no Exception will be raised (only for certain status codes)
        response.raise_for_status()
    except HTTPError as http_err:
        # https://realpython.com/python-f-strings/
        print(f'HTTP error occurred: {http_err}')  # Python 3.6
    except Exception as err:
        print(f'Other error occurred: {err}')  # Python 3.6
    else:
        print('Success!')

# Capture the response
response = requests.get('https://api.github.com')
print("Status Code: " + str(response.status_code))  # Status code

# If-else
if response.status_code == 200:
    print(response.url + ": Success!!!")
elif response.status_code == 404:
    print(response.url + ": Not Found")

print("URL: " + response.url)  # URL

# Response body/content
# Serialized JSON content
print("Response Content: " + str(response.content))  # Raw bytes of the response payload
# Requests will try to guess the encoding based on the response's headers if not specified
print("Response Text: " + str(response.text))  # Character-encoded response payload

response.encoding = 'utf-8'  # Optional, requests infers this internally
print("Response Text: " + str(response.text))  # UTF-8 character-encoded response payload

# De-serialize using json.loads() or simply response.json
print("Response JSON: ", end='')
print(response.json())

# List of keys in response body
print('##########################################################################')
print("Response body keys: ")
print('##########################################################################')
for key in response.json().keys():
    print(key)
print('##########################################################################')

# Response header
print("Response header: ", end='')
print(response.headers)

# List of keys in response header
print('##########################################################################')
print("Response header keys: ")
print('##########################################################################')
for key in response.headers.keys():
    print(key)
print('##########################################################################')

print("Response Content-Type: ", end='')
print(response.headers['Content-Type'])  # Response header content type
print("Response content-type: ", end='')
print(response.headers['content-type'])  # Headers are case insensitive

# Parameterized GET requests
# Query string parameters
# Search GitHub's repositories for requests
json_response = requests.get(
    'https://api.github.com/search/repositories',  # Github's search API
    params={'q': 'requests+language:python'},  # Modify the results returned by the search API (dictionary input)
).json()

repository = json_response['items'][0]
print(f'Repository name: {repository["name"]}')  # Python 3.6+
print(f'Repository description: {repository["description"]}')  # Python 3.6+

# params as a list of tuples
response = requests.get(
    'https://api.github.com/search/repositories',
    params=[('q', 'requests+language:python')],
)
print(response)

# params as bytes
response = requests.get(
    'https://api.github.com/search/repositories',
    params=b'q=requests+language:python',
)
print(response)

# Request headers
# Proprietary GitHub Accept header where the content is a special JSON format
# 'application/vnd.github.v3.text-match+json'
json_response = requests.get(
    'https://api.github.com/search/repositories',
    params={'q': 'requests+language:python'},
    headers={'Accept': 'application/vnd.github.v3.text-match+json'},  # text-match media type in Accept header
).json()

# Accept header tells the server what content types your application can handle
repository = json_response['items'][0]
print(f'Text matches: {repository["text_matches"]}')

##########################################################################
# Other HTTP methods
##########################################################################
# httpbin.org is a great resource created by the author of requests, Kenneth Reitz.
# It’s a service that accepts test requests and responds with data about the requests
# It has several great endpoints that can test pretty much everything you need in a HTTP library.
##########################################################################
# POST request
##########################################################################
# send data to a server to create/update a resource
# cannot be cached
# do not remain in browser history
# cannot be bookmarked
# no restrictions on data length or data type
print("POST request: ", end='')
print(requests.post('https://httpbin.org/post', data={'key': 'value'}))

##########################################################################
# PUT request
##########################################################################
# send data to a server to create/update a resource
# The difference between POST and PUT is that PUT requests are idempotent.
# That is, calling the same PUT request multiple times will always produce the same result.
# In contrast, calling a POST request repeatedly have side effects of creating the same resource multiple times.
print("PUT request: ", end='')
print(requests.put('https://httpbin.org/put', data={'key': 'value'}))

##########################################################################
# DELETE request
##########################################################################
# deletes the specified resource
print("DELETE request: ", end='')
print(requests.delete('https://httpbin.org/delete'))

##########################################################################
# HEAD request
##########################################################################
# almost identical to GET, but without the response body
# useful for checking what a GET request will return before actually making a GET request
print("HEAD request: ", end='')
print(requests.head('https://httpbin.org/get'))

##########################################################################
# PATCH request
##########################################################################
# https://www.baeldung.com/http-put-patch-difference-spring
# send data to a server to partially update a resource
# PUT requests are idempotent, PATCH requests need not be idempotent
print("PATCH request: ", end='')
print(requests.patch('https://httpbin.org/patch', data={'key': 'value'}))

##########################################################################
# OPTIONS request
##########################################################################
# describes the communication options for the target resource
print("OPTIONS request: ", end='')
print(requests.options('https://httpbin.org/get'))

##########################################################################
# Request message body/payload
##########################################################################
# POST, PUT, PATCH: data param accepts a dictionary, list of tuples, bytes, or a file-like object

# Content type: application/x-www-form-urlencoded
print(requests.post('https://httpbin.org/post', data={'key': 'value'}))  # Dictionary-format
print(requests.post('https://httpbin.org/post', data=[('key', 'value')]))  # Tuple-format

# JSON format
# When you pass JSON data via json, requests will serialize the data and add the correct Content-Type header
json_response = requests.post('https://httpbin.org/post', json={'key': 'value'}).json()
print(json_response['data'])
print(json_response['headers']['Content-Type'])

# PreparedRequest
# Request preparation includes actions like validating headers and serializing JSON content
response = requests.post('https://httpbin.org/post', json={'key': 'value'})
print(response.request.headers['Content-Type'])
print(response.request.url)
print(response.request.body)

# Authentication/authorization
# If the authenticated user is authenticated through basic authentication or OAuth with the user scope,
# then the response lists public and private profile information.
# If the authenticated user is authenticated through OAuth without the user scope,
# then the response lists only public profile information.
print(requests.get('https://api.github.com/user', auth=('username',
                                                        getpass(prompt='Password: ', stream=None))))
