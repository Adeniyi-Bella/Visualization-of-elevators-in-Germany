import requests
import json
import csv

#For example, querying the url of active escalators 

url = "https://api.deutschebahn.com/fasta/v2/facilities?type=ESCALATOR&state=ACTIVE"

payload = {}

#Bearer token obtained from requesting
headers = {
  'Authorization': 'Bearer 738fbe1a7a7953c1ac9fec9105daa28a'
}

response = requests.request("GET", url, headers=headers, data = payload)

#converting to json format
json_convert=response.json()
data= json.dumps(json_convert, indent=2)

#saving to csv file format
file = open('Active_elv.csv', 'wb')
writer = csv.writer(file)


print(data)
writer

#closing the file after opening
file.close()