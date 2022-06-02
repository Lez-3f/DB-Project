'''
Autor: Zel
Email: 2995441811@qq.com
Date: 2022-05-28 21:21:14
LastEditors: Zel
LastEditTime: 2022-06-03 00:49:32
'''
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func

from modules import Court, User, Admin, Student, Teacher
from utils import FAIL_CODE, NORMAL_STU, SUCCESS_CODE, TALENT_STU
from utils import BASKETBALL, BADMINTON, TABLETENNIS, VOLLEYBALL

from utils import session_commit

engine = create_engine('mysql+pymysql://root:s6d5v15sa1dva5s6d@localhost:3306/db_proj_test?charset=utf8') # 引擎
DBSession = sessionmaker(bind=engine) # 会话

newUser = User(1, "祝尔乐", '男', 'xxx98765431')

"""增删改查用户信息begin"""

def add_admin(no, name, sex, passwd):
    new_user = User(no, name, sex, passwd)
    new_admin = Admin(no)
    
    session = DBSession()
    session.add(new_user)
    rtn = session_commit(session)
    if 'err_msg' in rtn.keys():
        return rtn
    
    session.add(new_admin)
    rtn = session_commit(session)
    if 'err_msg' in rtn.keys():
        return rtn
    
    session.close()
    rtn['ret'] = SUCCESS_CODE
    return rtn
    
def add_student(no, name, sex, passwd, dept, clazz, phnum, rank=0):
    new_user = User(no, name, sex, passwd)
    new_student = Student(no, dept, clazz, phnum, rank)
    
    session = DBSession()
    session.add(new_user)
    rtn = session_commit(session)
    if 'err_msg' in rtn.keys():
        return rtn
    
    session.add(new_student)
    rtn = session_commit(session)
    if 'err_msg' in rtn.keys():
        return rtn
       
    session.close() 
    rtn['ret'] = SUCCESS_CODE
    return rtn

def add_teacher(no, name, sex, passwd, dept, phnum):
    new_user = User(no, name, sex, passwd)
    new_teacher = Teacher(no, dept, phnum)
    
    session = DBSession()
    session.add(new_user)
    rtn = session_commit(session)
    if 'err_msg' in rtn.keys():
        return rtn
    
    session.add(new_teacher)
    rtn = session_commit(session)
    if 'err_msg' in rtn.keys():
        return rtn
    
    session.close()
    rtn['ret'] = SUCCESS_CODE
    return rtn
    
def remove_user(no):
    session = DBSession()
    
    rtn = {}
    # 无法从程序删除管理员，管理员只能从后台向数据库添加
    if session.query(func.count(Admin.ano)).filter(Admin.ano == no).scalar() > 0:
        rtn['ret'] = FAIL_CODE
        rtn['err_msg'] = '不能删除管理员'
        return rtn
    
    # 先从学生 和 老师中删除
    if not session.query(Student).filter(Student.sno == no).delete():
        session.query(Teacher).filter(Teacher.tno == no).delete()
    
    session.query(User).filter(User.uno == no).delete()
    rtn = session_commit(session)
    if 'err_msg' in rtn.keys():
        return rtn
    
    session.close()
    rtn['ret'] = SUCCESS_CODE
    return rtn

"""增删改查用户信息end"""

# rtn = session_commit(session)
# if 'err_msg' in rtn.keys():
#     return rtn

"""增删改查场地器材信息begin"""

def add_court(no, name, type, info=''):
    new_court = Court(no, name, info, type)
    session = DBSession()
    
    session.add(new_court)
    rtn = session_commit(session)
    if 'err_msg' in rtn.keys():
        return rtn
    
    session.close()
    rtn['ret'] = SUCCESS_CODE
    return rtn
    
def add_experiment(no, )

"""增删改查场地器材信息end"""

## test
if __name__ == '__main__':
    add_student(100002, '王五', '男', 'sjkcks', '电机系', '电01', '17818283928')
    # remove_user(100002)
    pass
