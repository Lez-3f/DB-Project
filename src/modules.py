#! python3
# _*_ coding: utf-8 _*_
# @Time    :   2022/05/12 20:58:29
# @FileName:   modules.py
# @Author  :   Erler_ZHU
# @Email   :   2995441811@qq.com
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, String, Integer, Text, CHAR
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
        
class Student(Base):
    
    __tablename__ = 'student'
    
    sno = Column(Integer, primary_key=True)
    sdept = Column(String, nullable=False)
    sclazz = Column(String, nullable=False)
    srank = Column(Integer)
    sphnum = Column(CHAR(20))
    
    def __init__(self, no, dept, clazz, phnum, rank=0):
        self.sno = no
        self.sdept = dept
        self.sclazz = clazz
        self.srank = rank
        self.sphnum = phnum
        
class Teacher(Base):
    
    __tablename__ = 'teacher'
    
    tno = Column(Integer, primary_key=True)
    tdept = Column(String, nullable=False)
    tphnum = Column(CHAR(20))
    
    def __init__(self, no, dept, phnum):
        self.tno = no
        self.tdept = dept
        self.tphnum = phnum
        
    