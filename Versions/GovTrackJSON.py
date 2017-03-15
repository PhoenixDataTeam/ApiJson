#need to pip install requests in your virtual envrionment 

import json
import csv
import requests

url = 'https://www.govtrack.us/api/v2/bill?congress=114&order_by=-current_status_date'

r = requests.get(url)

data = r.json()

objects = data['objects']

# change code to the location on your computer
with open('../json35/bills.csv', 'w') as o:

    writer = csv.writer(o)

    writer.writerow([
            'title',
            'label',
            'number',
            'current_status'
        ])
    
    for bill in objects:
        writer.writerow([
            bill['title_without_number'],
            bill['bill_type_label'],
            bill['number'],
            bill['current_status']
        ])
