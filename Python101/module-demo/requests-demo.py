import requests

x = requests.get('http://httpbin.org/get')

print(x)
print(x.headers)
print(x.headers['Server'])

if x.status_code == 200:
    print("Success!")
elif x.status_code == 404:
    print("Not found!")

print(x.elapsed)
print(x.cookies)

print(x.content)
print(x.text)

x = requests.get('http://httpbin.org/get', params={'id':'1'})
print(x.url)

x = requests.get('http://httpbin.org/get?id2')
print(x.url)


x = requests.get('http://httpbin.org/get', params={'id':'3'}, headers={'Accept':'application/json', 'test_header':'test'})
print(x.text)


x = requests.delete('http://httpbin.org/delete')
print(x.text)

x = requests.post('http://httpbin.org/post', data={'a':'b'})
print(x.text)

# ----------------------------------------------

x = requests.get('http://github.com', allow_redirects=False)
print(x.headers)

#x = requests.get('http://httpbin.org/get', timeout=0.01)
#print(x.content)

x = requests.get('http://httpbin.org/cookies', cookies={'a':'b'})
print(x.content)

x = requests.session()
x.cookies.update({'a':'b'})
print(x.get('http://httpbin.org/cookies').text)

x = requests.get('https://api.github.com/events')
print(x.json())