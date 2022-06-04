'''
Autor: Zel
Email: 2995441811@qq.com
Date: 2022-06-03 20:24:43
LastEditors: Zel
LastEditTime: 2022-06-03 20:52:00
'''
with open('sql/add_court.txt', 'w') as f:
    f.write('INSERT INTO\ncourt(cno, cname, cinfo, ctype)\nVALUE\n')
    for i in range(8):
        f.write( '({0}, \'室内篮球场-{1}\', \'位于篮球馆，有灯光\', 0),\n'.format(i+1, str(i+1).rjust(2,'0')))
    for i in range(24):
        f.write( '({0}, \'室外篮球场-{1}\', \'位于露天球场, 晚上有灯\', 0),\n'.format(i+9, str(i+9).rjust(2,'0')))
    for i in range(24):
        f.write( '({0}, \'室内羽毛球场-{1}\', \'位于羽毛球馆, 有灯\', 1),\n'.format(i+1 + 1000 , str(i+1).rjust(2,'0')))
    for i in range(48):
        f.write( '({0}, \'室内乒乓球场-{1}\', \'位于羽毛球馆, 有灯\', 2),\n'.format(i+1 + 2000 , str(i+1).rjust(2,'0')))
    for i in range(4):
        f.write( '({0}, \'室内排球场-{1}\', \'位于羽毛球馆, 有灯\', 3),\n'.format(i+1 + 3000 , str(i+1).rjust(2,'0')))
    for i in range(4):
        f.write( '({0}, \'室外排球场-{1}\', \'位于露天球场, 晚上有灯\', 3),\n'.format(i+5 + 3000 , str(i+5).rjust(2,'0')))
    for i in range(4):
        f.write( '({0}, \'室外排球场-{1}\', \'位于露天球场, 晚上有灯\', 3),\n'.format(i+5 + 3000 , str(i+5).rjust(2,'0')))
    for i in range(4):
        f.write( '({0}, \'室外足球场-{1}\', \'5人制足球场, 位于露天球场, 晚上有灯\', 4),\n'.format(i+1 + 4000 , str(i+1).rjust(2,'0')))
    for i in range(4):
        f.write( '({0}, \'室外足球场-{1}\', \'7人制足球场, 位于露天球场, 晚上有灯\', 4),\n'.format(i+5 + 4000 , str(i+5).rjust(2,'0')))
    for i in range(1):
        f.write( '({0}, \'室外足球场-{1}\', \'7人制足球场, 位于露天球场, 晚上有灯\', 4),\n'.format(i+9 + 4000 , str(i+9).rjust(2,'0')))
    for i in range(11):
        f.write( '({0}, \'室外网球场-{1}\', \'位于露天球场, 晚上有灯\', 5),\n'.format(i+1 + 5000 , str(i+1).rjust(2,'0')))
    f.write( '({0}, \'室外网球场-{1}\', \'位于露天球场, 晚上有灯\', 5),\n'.format(11+1 + 5000 , str(11+1).rjust(2,'0')))