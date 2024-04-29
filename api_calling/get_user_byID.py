import requests 

with requests.get('http://127.0.0.1:5000/user/561') as res:
    print(res.json())


