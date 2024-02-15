import urllib.request
import xml.etree.ElementTree as ET

url = input('Enter URL: ')
print('Retrieving', url)

total = 0

uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved', len(data), 'characters')

tree = ET.fromstring(data)
counts = tree.findall('.//count')

for count in counts:
    total += int(count.text)

print('Sum:', total)
