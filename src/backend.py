'''
Autor: Zel
Email: 2995441811@qq.com
Date: 2022-05-28 21:21:14
LastEditors: Zel
LastEditTime: 2022-06-10 12:43:58
'''
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func
from sqlalchemy import desc

from modules import Court, Equipment, Rental, Reservation, User, Admin, Student, Teacher
from utils import CT_ST_MAINTAIN, EQ_ST_MAINTAIN, FAIL_CODE, LEGAL_TIME, NORMAL_STU, RSV_ST_PASS, RSV_ST_REJ, RSV_ST_WAIT, RT_ST_DRAW, RT_ST_RET, SUCCESS_CODE, TALENT_STU
from utils import BASKETBALL, BADMINTON, TABLETENNIS, VOLLEYBALL
from utils import TEACHER, STUDENT, ADMIN

from utils import session_commit
from utils import sports

from datetime import date, datetime, timedelta
from time import strftime

engine = create_engine('mysql+pymysql://root:s6d5v15sa1dva5s6d@localhost:3306/db_proj_test?charset=utf8') # 引擎
DBSession = sessionmaker(bind=engine) # 会话

# newUser = User(1, "祝尔乐", '男', 'xxx98765431')

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
    
def add_student(no, name, sex, passwd, clazz, dept,  phnum, rank=0):
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

"""用户通用功能接口begin"""
def login(no, passwd):
    # 返回登录状态、错误信息、用户信息
    rtn = {}
    
    session = DBSession()
    user:User = session.query(User).filter(User.uno == no).first()
    
    if not user:
        rtn['ret'] = FAIL_CODE
        rtn['err_msg'] = '用户不存在'
        return rtn
    
    user_type = 0
    user_sp = session.query(Admin)\
                .filter(Admin.ano == no)\
                .first()
    if not user_sp:
        user_sp = session.query(Student)\
            .filter(Student.sno == no)\
            .first()
        user_type = 1
    if not user_sp:
        user_sp = session.query(Teacher)\
            .filter(Teacher.sno == no)\
            .first()
        user_type = 2

    if user.upasswd != passwd:
        rtn['ret'] = FAIL_CODE
        rtn['err_msg'] = '用户密码错误'
        return rtn
    
    rtn['ret'] = SUCCESS_CODE
    rtn['user'] = (user_type, user, user_sp)

    return rtn

def get_eqs_info():
    """
        return: a dict
            'ret'
            'eq_info': a list of equipment objects
    """
    session = DBSession()
    eqs = (
        session.query(Equipment)
        .filter(Equipment.estate != EQ_ST_MAINTAIN)
        .all()
    )
    return list(eqs)

def get_eq(no):
    session = DBSession()
    eq = (
        session.query(Equipment)
        .filter(Equipment.eno == no)
        .one_or_none()
    )
    return eq
    

def get_court_info():
    """
        return: a dict
            'ret'
            'court_info': [basketball, badminton, ...]
                each sport obj is a list of court
    """
    session = DBSession()
        
    cts = (
        session.query( Court)
        .filter(Court.cstate != CT_ST_MAINTAIN)
        .all()
    )
    return cts

def get_court(no):
    session = DBSession()
    ct = (
        session.query(Court)
        .filter(Court.cno == no)
        .one_or_none()
    )
    return ct

def get_court_rsv_pass(no):
    rtn = {}
    session = DBSession()
    
    ct_rsv = (
        session.query(Reservation)
        .filter(Reservation.rcourt == no)
        .filter(Reservation.rstate == RSV_ST_PASS)
        .all()
    )
    
    return ct_rsv

def get_court_rsv_wait(no):
    rtn = {}
    session = DBSession()
    
    ct_rsv = (
        session.query(Reservation)
        .filter(Reservation.rcourt == no)
        .filter(Reservation.rstate == RSV_ST_WAIT)
        .all()
    )
    
    return ct_rsv

def get_court_rsv_wait_or_pass(no):
    rtn = {}
    session = DBSession()
    
    ct_rsv = (
        session.query(Reservation)
        .filter(Reservation.rcourt == no)
        .filter(Reservation.rstate < 2)
        .all()
    )
    
    return ct_rsv

def get_rsv_all_wait():
    rtn = {}
    session = DBSession()
    
    ct_rsv = (
        session.query(Reservation)
        .filter(Reservation.rstate == 0)
        .all()
    )
    
    return ct_rsv
    
def get_rsv(rno):
    session = DBSession()
    
    rsv = (
        session.query(Reservation)
        .filter(Reservation.rno == rno)
        .one_or_none()
    ) 
    return rsv
      
"""用户通用功能接口end"""


"""管理员功能接口begin"""

def set_court(no, attr, val):
    rtn = {}
    session = DBSession()
    
    session.query(Court)\
        .filter(Court.cno == no)\
        .update({attr: val})
    rtn = session_commit(session)
    if 'err_msg' in rtn.keys():
        return rtn
    
    session.close()
    rtn['ret'] = SUCCESS_CODE
    return rtn

def set_eq(no, attr, val):
    rtn = {}
    session = DBSession()
    
    session.query(Equipment)\
        .filter(Equipment.eno == no)\
        .update({attr: val})
    rtn = session_commit(session)
    if 'err_msg' in rtn.keys():
        return rtn
    
    session.close()
    rtn['ret'] = SUCCESS_CODE
    return rtn

def add_court(cno, cname, ctype, cinfo=''):
    rtn = {}
    new_court = Court(cno, cname, cinfo, ctype)
    session = DBSession()
    
    session.add(new_court)
    rtn = session_commit(session)
    if 'err_msg' in rtn.keys():
        return rtn
    
    session.close()
    rtn['ret'] = SUCCESS_CODE
    return rtn
    
def add_equipment(eno, ename, ebrand, enum_t):
    rtn = {}
    new_eq = Equipment(eno, ename, ebrand, enum_t)
    session = DBSession()
    
    session.add(new_eq)
    rtn = session_commit(session)
    if 'err_msg' in rtn.keys():
        return rtn
    
    session.close()
    rtn['ret'] = SUCCESS_CODE
    return rtn

def remove_court(no):
    rtn = {}
    session = DBSession()
    session.query(Court).filter(Court.cno == no).delete()
    rtn = session_commit(session)
    if 'err_msg' in rtn.keys():
        return rtn
    
    session.close()
    rtn['ret'] = SUCCESS_CODE
    return rtn
    

def remove_eq(no):
    rtn = {}
    session = DBSession()
    session.query(Equipment).filter(Equipment.eno == no).delete()
    rtn = session_commit(session)
    if 'err_msg' in rtn.keys():
        return rtn
    
    session.close()
    rtn['ret'] = SUCCESS_CODE
    return rtn    

def pass_reservation(no):
    
    rtn = {}
    session = DBSession()
    
    session.query(Reservation)\
    .filter(Reservation.rno == no)\
    .update({'rstate' : RSV_ST_PASS})
    rtn = session_commit(session)
    if 'err_msg' in rtn.keys():
        return rtn
    
    session.close()
    rtn['ret'] = SUCCESS_CODE
    return rtn

def reject_reservation(no):
    
    rtn = {}
    session = DBSession()
    
    session.query(Reservation)\
    .filter(Reservation.rno == no)\
    .update({'rstate' : RSV_ST_REJ})
    rtn = session_commit(session)
    if 'err_msg' in rtn.keys():
        return rtn
    
    session.close()
    rtn['ret'] = SUCCESS_CODE
    return rtn   

def start_rental(rtguest, rteq, rtnum):
    rtguest = int(rtguest)
    rteq = int(rteq)
    rtnum = int(rtnum)
    rtn = {}
    new_rental = Rental(rtguest, rteq, rtnum)
    new_no = new_rental.rtno
    session = DBSession()
    session.add(new_rental)
    rtn = session_commit(session)
    if 'err_msg' in rtn.keys():
        return rtn
    
    num_a = session.query(Equipment.enum_a)\
           .filter(Equipment.eno == rteq)\
           .one_or_none()[0]
    if rtnum > num_a:
        rtn['ret'] = FAIL_CODE
        rtn['err_msg'] = '器材数量不足'
        
        return rtn

    session.query(Equipment)\
           .filter(Equipment.eno == rteq)\
           .update({'enum_a': Equipment.enum_a - rtnum}) # 更新数量
    rtn = session_commit(session)
    if 'err_msg' in rtn.keys():
        return rtn
    
    session.close()
    rtn['ret'] = SUCCESS_CODE
    rtn['no'] = new_no
    return rtn

def end_rental(no):
    
    rtn = {}
    session = DBSession()
    eq, num = session.query(Rental.rteq, Rental.rtnum)\
        .filter(Rental.rtno == no)\
        .one_or_none()
    print(eq, num)
        
    session.query(Rental)\
           .filter(Rental.rtno == no)\
           .update({'rtstate': RT_ST_RET})
    rtn = session_commit(session)
    if 'err_msg' in rtn.keys():
        return rtn
           
    session.query(Equipment)\
           .filter(Equipment.eno == eq)\
           .update({'enum_a': Equipment.enum_a + num})
    rtn = session_commit(session)
    if 'err_msg' in rtn.keys():
        return rtn
    
    session.close()
    rtn['ret'] = SUCCESS_CODE
    return rtn

def get_user():
    
    session = DBSession()
    
    
    

"""管理员功能接口end"""

"""老师学生功能接口begin"""
def make_reservation(guest, court, begin:datetime, end:datetime, reason):
    
    def time_coincidence(bg1:datetime, ed1:datetime, bg2:datetime, ed2:datetime)->bool:
        return not( (bg1 >= ed2) or (bg2 >= ed1))
    
    def is_talent_stu(guest):
        session = DBSession()
        rank = (
            session.query(Student.srank)
            .filter(Student.sno == guest)
            .one_or_none()
        )
        # print(rank)
        if rank != None and rank[0] == TALENT_STU:
            return True
        else: return False
        
    def time_legal(begin:datetime, end:datetime)->bool:
        return end > begin and begin.hour >= LEGAL_TIME[0] and end.hour <= LEGAL_TIME[1]
    
    rtn = {}
    if not time_legal(begin, end):
        rtn['ret'] = FAIL_CODE
        rtn['err_code'] = '时间段错误'
        return rtn
        
    ct_rsv = get_court_rsv_wait_or_pass(court)
    for rsv in ct_rsv:
        rsv:Reservation
        if time_coincidence(rsv.rbegin, rsv.rend, begin, end):
            rtn['ret'] = FAIL_CODE
            rtn['err_code'] = '时间段已存在预约'
            return  rtn
    
    state = RSV_ST_WAIT
    if is_talent_stu(guest): state = RSV_ST_PASS # 体育生不用审批
    new_rsv = Reservation(guest, court, begin, end, reason, state)
    new_no = new_rsv.rno
    
    session = DBSession()
    session.add(new_rsv)
    rtn = session_commit(session)
    if 'err_msg' in rtn.keys():
        return rtn
    
    session.close()
    rtn['ret'] = SUCCESS_CODE
    rtn['no'] = new_no
    return rtn

def get_user_rsv_all(no):
    session = DBSession()
    
    ct_rsv = (
        session.query(Reservation)
        .filter(Reservation.rguest == no)
        .order_by(desc(Reservation.rtime))
        .all()
    )
    return ct_rsv
    
def get_user_rsv_just_now(uno):
    session = DBSession()
    
    ct_rsv = (
        session.query(Reservation)
        .filter(Reservation.rguest == uno)
        .filter(datetime.now() <  Reservation.rtime + timedelta(minutes=10))
        .order_by(desc(Reservation.rtime))
        .all()
    )
    return ct_rsv
    
def get_rt_draw():
    session = DBSession()
    
    rts = (
        session.query(Rental)
        .filter(Rental.rtstate == RT_ST_DRAW)
        .all()
    )
    return rts
    
def get_rt(rtno):
    session = DBSession()
    rt = (
        session.query(Rental)
        .filter(Rental.rtno == rtno)
        .all()
    )
    return rt

def get_user_rt_all(uno):
    session = DBSession()
    rts = (
        session.query(Rental)
        .filter(Rental.rtguest == uno)
        .all()
    )
    return rts
    

"""老师学生功能接口end"""

## test
if __name__ == '__main__':
    # add_student(100000, '测试特长生', '男', '123', '开发组', '开发01', '11111111111', TALENT_STU)
    remove_user(100002)
    # print(remove_user(1))
    
    # print(make_reservation(10001, 1, datetime(2022, 6, 11, hour=9), datetime(2022, 6, 11, hour=11), '练习'))
    # print(make_reservation(20001, 1, datetime(2022, 6, 11, hour=13), datetime(2022, 6, 11, hour=16), '练习'))
    
    # print(make_reservation(10003, 1, datetime(2022, 6, 12, hour=10), datetime(2022, 6, 12, hour=12), '练习'))
    # print(make_reservation(10004, 1, datetime(2022, 6, 12, hour=15), datetime(2022, 6, 12, hour=17), '练习'))
    # print(make_reservation(10005, 1, datetime(2022, 6, 12, hour=19), datetime(2022, 6, 12, hour=21), '练习'))
    # print(make_reservation(20002, 1, datetime(2022, 6, 13, hour=14), datetime(2022, 6, 13, hour=18), '练习'))
    # print(make_reservation(10007, 1, datetime(2022, 6, 14, hour=14), datetime(2022, 6, 14, hour=17), '练习'))
    start_rental(1, 32, 10)
    end_rental(20220610115410000001318)
    # add_equipment('篮球7号球', 'NIKE', 50)
    # remove_eq(1)
    # pass_reservation(20220603210958000001245)
    # pass_reservation(20220606104138000002142)
    # pass_reservation(20220606105424000004756)
    # reject_reservation(20220606112107100000738)
    # print(get_court_info())
    
    # def time_coincidence(bg1:datetime, ed1:datetime, bg2:datetime, ed2:datetime)->bool:
    #     return not( (bg1 >= ed2) or (bg2 >= ed1)) 
    # bg1 = datetime(2022, 6, 7, 9)
    # ed1 = datetime(2022, 6, 7, 11)
    # bg2 = datetime(2022, 6, 7, 10)
    # ed2 = datetime(2022, 6, 7, 12)
    # print(time_coincidence(bg1, ed2, ed1, ed2))
    # print( start_rental(1, 1, 1) )
    # print(end_rental(20220607003027000001100))
    # print(set_court(1, 'cstate', CT_ST_MAINTAIN))
    
    pass
