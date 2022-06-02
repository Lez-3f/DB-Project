'''
Autor: Zel
Email: 2995441811@qq.com
Date: 2022-05-28 22:08:18
LastEditors: Zel
LastEditTime: 2022-06-03 00:45:22
'''
from datetime import datetime
from random import randint
SUCCESS_CODE = 0
FAIL_CODE = 1

MALE = 1
FEMALE = 0

NORMAL_STU = 0
TALENT_STU = 1

BASKETBALL = 0
BADMINTON = 1
TABLETENNIS = 2
VOLLEYBALL = 3

CT_ST_AVAILABLE = 0
CT_ST_OCCUPIED = 1
CT_ST_MAINTAIN = 2

RSV_ST_WAIT = 0
RSV_ST_PASS = 1
RSV_ST_REJ = 2
RSV_ST_UNVALUE = 999

RT_ST_DRAW = 0
RT_ST_RET = 1
RT_ST_UNVALUE = 999

def session_commit(session):
    rtn = {}
    try:
        session.commit()
    except Exception as e:
        print(e)
        rtn['err_msg'] = str(e)
        rtn['ret'] = FAIL_CODE
        return rtn
    
    return rtn

def get_order_no(guest:int, dt:datetime):
    dt_int = dt.year*10000000000 + dt.month*100000000 + dt.day*1000000 + dt.hour*10000 + dt.minute*100 + dt.second
    no = dt_int * 1000000000 + (guest%1000000) * 1000 + randint(0,1000)
    return no
    
if __name__ == '__main__':
    print(get_order_no(100231, datetime.now()))