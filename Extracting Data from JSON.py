# Extracting Data from JSON
import json
import urllib.request

count = 0

# Prompting the user for a URL
url = input("Enter location: ")

print("Retrieving", url)
# Opening the URL and reading the data
with urllib.request.urlopen(url) as response:
    data = response.read().decode()

print("Retrieved", len(data), "characters")

# Parsing the JSON data
info = json.loads(data)

# Extracting comment counts and computing the sum
for item in info["comments"]:
    count += int(item["count"])

print("Count:", len(info["comments"]))
print("Sum:", count)
