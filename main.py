import json
import requests
import os

response = requests.get(os.environ.get('JSON_URL'))
vm = response.json()
