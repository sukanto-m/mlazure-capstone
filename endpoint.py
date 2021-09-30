import json
import requests

#url for the webservice

uri = 'http://fe44eac5-c709-4c0f-8ec0-aec61116f5b0.southcentralus.azurecontainer.io/score'

#two samples to test
#this is randomly constructed for test purposes so I apologise for
#any medical inaccuracies

data = {"data":
       [
       {"age": 45,
        "anaemia": 0,
        "creatinine_phosphokinase": 900,
        "diabetes": 1,
        "ejection_fraction": 30,
        "high_blood_pressure": 1,
        "platelets": 140000,
        "serum_creatinine": 1.1,
        "serum_sodium": 140,
        "sex": 1,
        "smoking": 1,
        "time": 10
        },

        {"age": 35,
         "anaemia": 0,
         "creatinine_phosphokinase": 800,
         "diabetes": 0,
         "ejection_fraction": 30,
         "high_blood_pressure": 1,
         "platelets": 150000,
         "serum_creatinine": 1.1,
         "serum_sodium": 140,
         "sex": 0,
         "smoking": 1,
         "time": 12

        },]}

#convert to json string

input_data = json.dumps(data)
with open("data.json", "w") as _f:
    _f.write(input_data)

#set output type

headers = {'Content-type' : 'application/json'}

#make request and get response

resp = requests.post(uri, input_data, headers=headers)
print(resp.json())
