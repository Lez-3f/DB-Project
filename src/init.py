'''
Autor: Zel
Email: 2995441811@qq.com
Date: 2022-05-28 21:21:14
LastEditors: Zel
LastEditTime: 2022-05-29 16:13:31
'''
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from modules import User, Admin
from define import NORMAL_STU, TALENT_STU
from define import BASKETBALL, BADMINTON, TABLETENNIS, VOLLEYBALL

engine = create_engine('mysql+pymysql://root:s6d5v15sa1dva5s6d@localhost:3306/db_proj_test?charset=utf8') # 引擎
Session = sessionmaker(bind=engine) # 会话

session = Session()

newUser = User(1, "祝尔乐", '男', 'xxx98765431')
session.add(newUser)
session.commit()


def add_student(no, name, )