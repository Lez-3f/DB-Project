#! python3
# _*_ coding: utf-8 _*_
# @Time    :   2022/05/12 21:09:18
# @FileName:   config.py
# @Author  :   Erler_ZHU
# @Email   :   2995441811@qq.com

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+pymysql://root:s6d5v15sa1dva5s6d@localhost:3306/course_homework?charset=utf8') # 引擎
Session = sessionmaker(bind=engine) # 会话

