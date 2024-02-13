from urllib import request
from bs4 import BeautifulSoup

# URL for the actual data
url = 'http://py4e-data.dr-chuck.net/comments_1854503.html'

# Open the URL and read the HTML content
html = request.urlopen(url).read()

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Find all span tags
tags = soup('span')

# Initialize sum variable
total_sum = 0

# Loop through span tags and sum up the numbers
for tag in tags:
    total_sum += int(tag.contents[0])

# Check if the sum ends with 74
if total_sum % 100 == 74:
    print("Sum ends with 74!")
else:
    print("Sum does not end with 74!")

# Print the total sum
print("Total sum:", total_sum)
