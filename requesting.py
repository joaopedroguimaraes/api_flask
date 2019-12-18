import requests
import time

print("Enviando GET request")
requests.get('http://127.0.0.1:5000/')

time.sleep(5)

print("Enviando POST request")
requests.post('http://127.0.0.1:5000/')
