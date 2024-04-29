import requests 

with requests.delete('http://127.0.0.1:5000/user/王瑞') as res:
    print(res.json())


'''
第二次运行需要修改url username
'''