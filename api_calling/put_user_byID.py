import requests 

with requests.put('http://127.0.0.1:5000/user/563?username=muzi&email=123456') as res:
    print(res.json())


