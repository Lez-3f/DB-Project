'''
Autor: Zel
Email: 2995441811@qq.com
Date: 2022-05-28 21:21:14
LastEditors: Zel
LastEditTime: 2022-05-29 16:53:41
'''
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from modules import User, Admin
from define import NORMAL_STU, TALENT_STU
from define import BASKETBALL, BADMINTON, TABLETENNIS, VOLLEYBALL

engine = create_engine('mysql+pymysql://root:s6d5v15sa1dva5s6d@localhost:3306/db_proj_test?charset=utf8') # 引擎
DBSession = sessionmaker(bind=engine) # 会话

newUser = User(1, "祝尔乐", '男', 'xxx98765431')

## 增
def add_admin(no, name, sex, passwd):
    new_user = User(no, name, sex, passwd)
    new_admin = Admin(no)
    session = DBSession()
    session.add(new_user)
    session.commit()
    
    session.add(new_admin)
    session.commit()
    
def add_student(no, name, sex, passwd, dept, clazz, phnum, rank=0):
    pass

def add_teacher(no, name, sex, passwd, dept, phnum):
    pass

if __name__ == '__main__':
    add_admin(4, '紫光', '男', 'weiyangshuyuan')