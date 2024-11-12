# pesudcode

# function handleURL(string url)
# 1. Read the google file
# 2. Return the desired text in string? 
#   - Look for a table?
#   - Look for the string "x-coordinate"?

# function printText(string url)
# 1. Call handleURL(url)
# 2. Store value into an array, array of SyntaxWarning
# 3. print it in reverse order

import requests
from bs4 import BeautifulSoup

url = "https://docs.google.com/document/d/e/2PACX-1vRMx5YQlZNa3ra8dYYxmv-QIQ3YJe8tbI3kqcuC7lQiZm-CSEznKfN_HYNSpoXcZIV3Y_O3YoUB1ecq/pub"
response = requests.get(url)
if response.status_code != 200:
    raise Exception(f"Failed to load page with status code {response.status_code}")

soup = BeautifulSoup(response.text, 'html.parser')

table_data = []
rows = soup.find_all('tr')[1:]  
dic = {}
maxX = 0
maxY = 0

for row in rows:
    cells = row.find_all('td')
    if len(cells) == 3:
        
        x = int(cells[0].text.strip())
        character = cells[1].text.strip()
        y = int(cells[2].text.strip())

        maxX = max(x,maxX)
        maxY = max(y,maxY)
        dic[(x,y)] = character

while maxY >= 0:
    tempStr = ""
    for x_cord in range(maxX + 1):
        tempStr += (dic.get((x_cord,maxY), ""))
    print(tempStr)
    maxY = maxY - 1

