# Flask sqlalchemy 实现的 crud操作(Create Read Update Delete)


文件目录如下：
~~~
├── api_calling                              --接口测试
│   ├── add_user.py
│   ├── add_user_single.py
│   ├── add_users.py
│   ├── del_user_byID.py
│   ├── del_user_byUsername.py
│   ├── get_user_all.py
│   ├── get_user_byID.py
│   ├── get_user_byPage.py
│   └── put_user_byID.py
├── app.py                                    -- 主程序入口
├── instance                                  -- database
│   └── project.db
├── python_base                               --python review  
│   ├── decortor
│   │   ├── decoration1.py
│   │   ├── decoration2.py
│   │   ├── decoration3.py
│   │   └── readme.md
│   └── while.py
└── readme.md
~~~
# Quick start

>git clone git@github.com:RKwork85/rk_sqlalchemy_crud.git

>pip install -r requirements.txt

>cd rk_sqlalchemy_crud

>python app.py

## abstract摘要

一、**api calling**：

1、CREATE：包含单个用户创建，多个用户创建；

- 实现原理：数据来源于faker,构造符合数据模型的数据，通过确认状态码，来确保数据发送成功，字段username属性为unique,需作为跳出循环的判别条件（服务器会发送400状态码：数据库已有该用户）
    
- post请求需带上headers，要包含数据格式：{'Content-Type':'applacation/json'}

2、 READ包含: 
- 单个用户查询：
- 按id查询：
- 分页查询：第几页数据的多少条数据；page&per_page
- 数据库所有数据查询；

3、 UPDATE 更新单条数据：需要传入username&email

4、 DELETE 包含：按ID删除，按username删除数据

二、**app.py**:

flask创建的服务器接口如下

```
add_user              POST     /user                  
del_user_by_id        DELETE   /user/<int:uid>        
del_user_by_username  DELETE   /user/<string:username>
get_user_by_id        GET      /user/<int:uid>        
get_user_page         GET      /user                  
get_users             GET      /users                 
update_user           PUT      /user/<int:uid>   
```

实现原理：

- 1、flask_sqlalchemy + sqlite 提供数据库
- 2、restful api格式 实现crud
- 3、库引用：from flask import sqlalchemy, request, jsonify 
- 4、knowledges: 
    
    --4.1：路由参数 <<int:uid>> <<string:username>>

    --4.2: 获取路由参数： username = request.args.get('username')

    --4.3: 得到json数据： data  = request.get_json(); username = data.get('username')

    --4.4: 数据库操作：

        1 按主键查找数据：user= db.get_or_404(User,uid)
        2 按字段查找： user = User.query.filter_by(username=username).first()
        3 paginate 按数据库字段选择：
        q = db.select(User).order_by(User.id);db.paginate(q, page= page, 
        per_page = per_page)
        paginate = db.paginate(db.select(User).order_by(User.id), page=page,per_page=per_page)
        4 user.json()可以得到该条数据；
    
    --4.5: return: jsonify({'':'','',''}); jsonify(msg='',data=''); {'':'','':''} 

    --4.6: receive: resp.json()

    --4.7： 报错情形： 1 数据库中数据不存在；2 数据格式错误有的时候返回是页面； 3 找不到数据库位置

---

三、vscode 插件 

预览sql:

> SQLite Viewer v0.3.13

# If you find me

please give me a star ⭐ 
