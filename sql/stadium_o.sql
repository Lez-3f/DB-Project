CREATE TABLE IF NOT EXISTS court(
    cno INT,
    cname VARCHAR,
    cinfo TEXT,
    ctype INT,
    cstate INT,
    PRIMARY KEY (cno)
);

CREATE TABLE IF NOT EXISTS equipment(
    eno INT,
    ename VARCHAR,
    enum_t INT,
    enum_a INT,
    estate INT,
    PRIMARY KEY (eno)
);

CREATE TABLE IF NOT EXISTS reservation(
    rno INT,
    rguest INT,
    rcourt INT,
    rdate DATE,

);
