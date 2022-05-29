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

class Student(Base):
    
    __tablename__ = 'student3'
    
    
    snum = Column('student_number', String, primary_key=True) # 编号 
    sname = Column('student_name', String, nullable = False) # 姓名
    sdept = Column('department_name', String, nullable = False) # 院系
    
    
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('mysql+pymysql://root:s6d5v15sa1dva5s6d@localhost:3306/course_homework?charset=utf8')
Session = sessionmaker(bind=engine)
session = Session()

res = session.query(Student).filter(Student.snum == '123456').delete()
print(res)
session.commit()
session.close()
