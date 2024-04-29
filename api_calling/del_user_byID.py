import requests 

with requests.delete('http://127.0.0.1:5000/user/601') as res:
    print(res.json())

'''
第二次运行：需修改url的用户id
'''


