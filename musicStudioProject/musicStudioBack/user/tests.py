from django.test import TestCase

# Create your tests here.
import requests,pprint

payload = {
    'username': '1935010205',
    'password': '12345678'
}

response = requests.get('https://localhost/user',
              data=payload)

pprint.pprint(response.json())