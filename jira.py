import requests
import json

response = requests.request('get', 'http://192.168.56.102:9093/api/v1/alerts')
alerts_dict = json.loads(response.content)
# print alerts_dict

url = "http://localhost:8090/rest/api/2/issue/"
spec = {
    "fields": {
        "project":
       {
           "key": "SP"
       },
        "summary": " alert for CPU High Usage.",
        "description": " alert for CPU High Usage.",
        "issuetype": {
           "name": "Bug"
       }
    }
}

if alerts_dict["data"][0]["status"]["state"] == "active":
    # session = requests.Session()
    # session.auth = ('anupam.debnath@alefmobitech.com', 'tatu@1989')
    # session.verify = False
    # session.headers.update(
    #     {'Content-Type': 'application/json; charset=utf-8'})
    # result = session.post(url, data=json.dumps(spec))
    # response = result.content
