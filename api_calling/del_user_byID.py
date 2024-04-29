import requests 

with requests.delete('http://127.0.0.1:5000/user/562') as res:
    print(res.json())


