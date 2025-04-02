import requests
from getToken import get_token

def get_data_from_endpoint(endpoint : str = ""):
    URL = "http://hackathon2025-prod-env.eba-sa8j9hq2.eu-central-1.elasticbeanstalk.com/"
    TOKEN = get_token()
    res = requests.get(URL + endpoint)


if __name__ == "__main__":
    get_data_from_endpoint()
    