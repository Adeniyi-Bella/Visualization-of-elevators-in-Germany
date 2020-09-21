import requests
import json

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


print(data)
