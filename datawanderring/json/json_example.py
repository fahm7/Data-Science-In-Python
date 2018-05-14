import json
import requests

url="http://musicbrainz.org/ws/2/artist/5b11f4ce-a62d-471e-81fc-a69a8278c7da?inc=aliases&fmt=json"
data= requests.get(url).text
print (type(data))
print (data)

data= json.loads(data)
print (type(data))
print (data)