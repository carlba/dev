
import requests

r = requests.get(u'https://api.github.com/user', auth=('carlba', 'bajskorv9510'))




print r.status_code
print r.headers['content-type']
print r.encoding
print r.text



print r.json()
print r.json()
print r.json()["login"]

