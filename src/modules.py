#! python3
# _*_ coding: utf-8 _*_
# @Time    :   2022/05/12 20:58:29
# @FileName:   modules.py
# @Author  :   Erler_ZHU
# @Email   :   2995441811@qq.com
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, String, Integer, Text
Base = declarative_base()

class User(Base):
    
    __tablename__ = 'user'
    
    uno = Column(Integer, primary_key=True)
    uname = Column(String, nullable=False)
    usex = Column(Integer, nullable=False)
    upasswd = Column(Text, nullable=False)
    
    def __init__(self, no, name, sex, passwd):
        self.uno = no
        self.uname = name
        self.usex = sex
        self.upasswd = passwd
        
class Admin(Base):
    
    __tablename__ = 'admintt'
    
    ano = Column(Integer, primary_key=True) # 编号
    
    def __init__(self, no):
        self.ano = no
    