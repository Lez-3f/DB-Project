'''
Autor: Zel
Email: 2995441811@qq.com
Date: 2022-05-28 21:21:14
LastEditors: Zel
LastEditTime: 2022-06-04 10:42:15
'''
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func

from modules import Court, Equipment, Reservation, User, Admin, Student, Teacher
from utils import FAIL_CODE, NORMAL_STU, SUCCESS_CODE, TALENT_STU
from utils import BASKETBALL, BADMINTON, TABLETENNIS, VOLLEYBALL

from utils import session_commit

from datetime import date, datetime, timedelta
from time import strftime

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
    
def add_equipment(no, name, num_t):
    new_eq = Equipment(no, name, num_t)
    session = DBSession()
    
    session.add(new_eq)
    rtn = session_commit(session)
    if 'err_msg' in rtn.keys():
        return rtn
    
    session.close()
    rtn['ret'] = SUCCESS_CODE
    return rtn

def remove_court(no):
    session = DBSession()
    session.query(Court).filter(Court.cno == no).delete()
    rtn = session_commit(session)
    if 'err_msg' in rtn.keys():
        return rtn
    
    session.close()
    rtn['ret'] = SUCCESS_CODE
    return rtn

def remove_eq(no):
    session = DBSession()
    session.query(Equipment).filter(Equipment.eno == no).delete()
    rtn = session_commit(session)
    if 'err_msg' in rtn.keys():
        return rtn
    
    session.close()
    rtn['ret'] = SUCCESS_CODE
    return rtn    

"""增删改查场地器材信息end"""

"""用户通用功能接口begin"""
def login(no, passwd):
    # 返回登录状态、错误信息、用户信息
    rtn = {}
    
    session = DBSession()
    user:User = session.query(User).fliter(User.uno == no).first()
    
    if not user:
        rtn['ret'] = FAIL_CODE
        rtn['err_msg'] = '用户不存在'
        return rtn
        
    if user.upasswd != passwd:
        rtn['ret'] = FAIL_CODE
        rtn['err_msg'] = '用户密码错误'
        return rtn
    
    rtn['ret'] = SUCCESS_CODE
    rtn['user'] = user
    return rtn

def get_eq_info():
    """
        return: a dict
            'ret'
            'eq_info': [bkb, bmt, tt, vb]
                each sport obj is a list of tuple(court, statetable)
                statetable: a 7 * 14 matrix of court state
    """

def get_court_info():
    """
        return: a dict
            'ret'
            'court_info': [bkb, bmt, tt, vb]
                each sport obj is a list of tuple(court, statetable)
                statetable: a 7 * 14 matrix of court state
    """
    
    def get_this_week():
        today = datetime.today()
        today = datetime.strptime(today, '%Y-%m-%d')    # 将字符串格式化为datetime类型
        weekday = today.weekday()   # 获取输入的日期是周几：int 周一为0
        # print(weekday)
        ret = list()
        # 这周开始的时间：这周开始的日期为今天的日期减去周几，如周一的减0，所以开始日期就是输入日期了
        start_day = today - timedelta(weekday)
        for i in range(7):
            wd = start_day + timedelta(i)   # 从开始日期加一整周的时间
            ret.append(wd.strftime('%Y-%m-%d')) # 转换为字符串后加入列表中
        return ret


        
      
"""用户通用功能接口end"""


"""管理员功能接口begin"""

"""管理员功能接口end"""


"""老师学生功能接口begin"""
def make_reservation(guest, court, begin, end, reason):
    new_rsv = Reservation(guest, court, begin, end, reason)
    
    session = DBSession()
    session.add(new_rsv)
    rtn = session_commit(session)
    if 'err_msg' in rtn.keys():
        return rtn
    
    session.close()
    rtn['ret'] = SUCCESS_CODE
    return rtn 
"""老师学生功能接口end"""

## test
if __name__ == '__main__':
    # add_student(100002, '王五', '男', 'sjkcks', '电机系', '电01', '17818283928')
    # print(remove_user(1))
    begin = datetime(2022, 6, 3, 9)
    end = datetime(2022, 6, 3, 11)
    # make_reservation(1, 2001, begin, end, '系队训练')
    pass
