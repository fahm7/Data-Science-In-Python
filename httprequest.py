from urllib.request import urlopen, Request
import ssl
context = ssl._create_unverified_context()

url = "https://www.wikipedia.org/"

request = Request(url)
response = urlopen(request,context=context)
html = response.read()
print("______________DATA WITH URLLIB___________")
print (html)

response.close()

import requests
verify='/etc/ssl/certs/cacert.org.pem'
r = requests.get(url, verify=False)

#r= requests.get(url)

# one line return html as string
text= r.text
print("\n\n______________DATA WITH RESUESTS___________\n")
print(text)

