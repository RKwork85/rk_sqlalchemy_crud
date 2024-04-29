import requests 

with requests.get('http://127.0.0.1:5000/user/561') as res:
    print(res.json())


'''
换个uid就能找到该数据了：566
'''

