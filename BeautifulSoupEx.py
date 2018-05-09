import requests
verify='/etc/ssl/certs/cacert.org.pem'

url = "https://www.wikipedia.org/"

r = requests.get(url, verify=False)

# one line return html as string
html_doc = r.text
print("\n\n______________DATA WITH RESUESTS___________\n")
# print(html_doc)

#----------------- BEAUTIFUL SOUP -----------------------------

from bs4 import BeautifulSoup

soup= BeautifulSoup(html_doc)
print(soup.title)
#print(soup.get_text())

for link in soup.find_all('a'):
            print(link.get('href'))
