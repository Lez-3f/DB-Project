#! python3
# _*_ coding: utf-8 _*_
# @Time    :   2022/05/12 20:58:29
# @FileName:   modules.py
# @Author  :   Erler_ZHU
# @Email   :   2995441811@qq.com

from ast import In
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer

Base = declarative_base()

class Admin(Base):
    """
    管理员类
    """
    
    __tablename__ == 'admin'
    
    ano = Column(Integer, primary_key=True) # 编号 
    aname = Column(String, nullable = False) # 姓名
    apasswd = Column(String, nullable = False)
    