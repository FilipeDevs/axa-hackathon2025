import json

import requests


def get_token():
    url = "http://hackathon2025-prod-env.eba-sa8j9hq2.eu-central-1.elasticbeanstalk.com"
    endpoint = "/api/security/token/5103fe9d-aac9-4027-adf8-1f9a9ffddffd"

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