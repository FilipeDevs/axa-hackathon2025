import json

import requests


def get_token():
    url = "http://hackathon2025-prod-env.eba-sa8j9hq2.eu-central-1.elasticbeanstalk.com"
    endpoint = "/api/security/token/c7deec0b-c680-4315-a85c-a5c30a2b2b82"

    headers = {"accept": "application/json"}
    response = requests.get(url + endpoint, headers=headers)
    if response.status_code == 200:
        token = response.json().get('hash')
        print("Token:", token)
        print("Token retrieved successfully.")
        return
    else:
        print("Failed to retrieve token. Status code:", response.status_code)
        return

if __name__ == "__main__":
    get_token()