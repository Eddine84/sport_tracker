import requests
from datetime import datetime
import os 
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_ID = os.getenv("API_ID")
END_POINT =  os.getenv("END_POINT")
SECOND_END_POINT = os.getenv("SECOND_END_POINT")
TOKEN = os.getenv("TOKEN_NUMBER")






GENDER = "male"
WEIGHT_KG = 70
HEIGHT_CM = 175
AGE = 30


exercice_text = input("Tell me wich exercice you did:")



headers = {
    "x-app-id":API_ID,
    "x-app-key":API_KEY
}

parameters = {
      "query": exercice_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE

}

response = requests.post(url=END_POINT,json=parameters,headers=headers)
response.raise_for_status()
result = response.json()

now = datetime.now()


for exercise in result["exercises"]:

    sheet_inputs = {
        "workout":{
            "date":now.strftime("%Y-%m-%d"),
            "time":now.strftime("%H:%M:%S"),
            "exercise":exercise["name"].title(),
            "duration":exercise["duration_min"],
            "calories":exercise["nf_calories"]
        }
    }

headers = {
    "Authorization":f"Bearer {TOKEN}"
}

second_response = requests.post(url=SECOND_END_POINT,json=sheet_inputs,headers=headers)
second_response.raise_for_status()

print(second_response.text)
   
