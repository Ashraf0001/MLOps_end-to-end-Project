import requests
import json

# Test data
test_data = {
    "age": 39,
    "workclass": 7,
    "education_num": 13,
    "marital_status": 1,
    "occupation": 4,
    "relationship": 1,
    "race": 4,
    "sex": 1,
    "capital_gain": 2174,
    "capital_loss": 0,
    "hours_per_week": 40,
    "native_country": 39
}

# Send POST request
response = requests.post(
    "http://localhost:5000/predict",
    json=test_data,
    headers={"Content-Type": "application/json"}
)

# Print results
print("Status Code:", response.status_code)
print("Response:", response.json())
