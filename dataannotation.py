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

# Step 2: Parse the HTML
soup = BeautifulSoup(response.text, 'html.parser')

# Step 3: Locate the table and extract data
# Assuming the table rows are identifiable in the HTML structure. Adjust tags based on actual structure.
table_data = []
rows = soup.find_all('tr')  # This might vary based on the table structure

for row in rows:
    cells = row.find_all('td')
    if len(cells) == 3:  # Assuming 3 columns: x-coordinate, y-coordinate, character
        x_coordinate = cells[0].text.strip()
        y_coordinate = cells[1].text.strip()
        character = cells[2].text.strip()
        table_data.append({
            "x-coordinate": x_coordinate,
            "y-coordinate": y_coordinate,
            "character": character
        })

# Step 4: Display the extracted data
for entry in table_data:
    print(entry)
