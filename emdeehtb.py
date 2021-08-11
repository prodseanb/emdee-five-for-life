from bs4 import BeautifulSoup
import requests
import hashlib

URL = "http://142.93.35.92:31149"
request = requests.session()
page = request.get(URL)

soup = BeautifulSoup(page.text, "html.parser")

for i in soup.findAll('h3'):
	md5 = (i.get_text())
	#print(md5)

hash_object = hashlib.md5(md5.encode())
md5_hash = hash_object.hexdigest()
#print(md5_hash)

data = {'hash': md5_hash}
output = request.post(url = URL, data = data)

print(output.text)
