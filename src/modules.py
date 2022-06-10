#! python3
# _*_ coding: utf-8 _*_
# @Time    :   2022/05/12 20:58:29
# @FileName:   modules.py
# @Author  :   Erler_ZHU
# @Email   :   2995441811@qq.com
from datetime import datetime

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Date, ForeignKey, String, Integer, Text, CHAR, TIMESTAMP, DateTime
from sqlalchemy import BigInteger

from utils import EQ_ST_AVAILABLE, get_order_no
from utils import CT_ST_AVAILABLE
from utils import RT_ST_DRAW, RT_ST_RET
from utils import RSV_ST_REJ, RSV_ST_WAIT, RSV_ST_PASS

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
        
    
class Court(Base):
    
    __tablename__ = 'court'
    
    cno = Column(Integer, primary_key=True)
    cname = Column(String, nullable=False)
    cinfo = Column(Text, nullable=True)
    ctype = Column(Integer)
    cstate = Column(Integer)
    
    def __init__(self, no, name, info, type):
        self.cno = no
        self.cname = name
        self.cinfo = info
        self.ctype = type
        self.cstate = CT_ST_AVAILABLE
        
class Equipment(Base):
    
    __tablename__ = 'equipment'
    
    eno = Column(Integer, primary_key=True)
    ename = Column(String)
    ebrand = Column(String, nullable=True)
    enum_t = Column(Integer)
    enum_a = Column(Integer)
    estate = Column(Integer)
    
    def __init__(self, no, name, brand, num_t):
        
        self.eno = no
        self.ename = name
        self.ebrand = brand
        self.enum_t = num_t
        self.enum_a = num_t # 初始认为可用数量和总数量相等
        self.estate = EQ_ST_AVAILABLE

class Reservation(Base):
    
    __tablename__ = 'reservation'
    
    rno = Column(BigInteger, primary_key = True)
    rguest = Column(Integer, ForeignKey(User.uno))
    rcourt = Column(Integer, ForeignKey(Court.cno))
    rtime = Column(DateTime)
    rbegin = Column(DateTime)
    rend = Column(DateTime)
    rstate = Column(Integer)
    rreason = Column(Text)
    
    def __init__(self, guest, court, begin, end, reason, state=RSV_ST_PASS):
        
        self.rguest = guest
        self.rtime = datetime.now()
        self.rno = get_order_no(self.rguest, self.rtime)
        
        self.rcourt = court
        self.rbegin = begin
        self.rend = end
        self.rstate = state
        self.rreason = reason
        
class Rental(Base):
    
    __tablename__ = 'rental'
    
    rtno = Column(BigInteger, primary_key=True)
    rtguest = Column(Integer, ForeignKey(User.uno))
    rteq = Column(Integer, ForeignKey(Equipment.eno))
    rtdraw = Column(DateTime)
    rtreturn = Column(DateTime)
    rtnum = Column(Integer)
    rtstate = Column(Integer)
    
    def __init__(self, guest, eq, num):
        self.rtdraw = datetime.now()
        self.rtreturn = datetime(2050, 1, 1, 0)
        self.rtguest = guest
        self.rtno = get_order_no(self.rtguest, self.rtdraw)
        
        self.rteq = eq
        self.rtnum = num
        self.rtstate = RT_ST_DRAW