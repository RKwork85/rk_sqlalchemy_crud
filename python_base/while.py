import requests
import json
from faker import Faker 

data = {

    'username' :'123456',
    'email' : '啦啦啦'
}
headers = {'Content-Type':'application/json'}
resp = requests.post(url='http://127.0.0.1:5000/user', data=json.dumps(data), headers=headers)

while resp:  
    user_input = input("请输入内容（输入 'quit' 退出）：")  
    if user_input == "quit":  
        break  
    print("你输入了：", user_input)