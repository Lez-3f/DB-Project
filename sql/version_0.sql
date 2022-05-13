CREATE TABLE IF NOT EXISTS admin(
    ano INT,
    aname VARCHAR,
    apasswd TEXT,
    PRIMARY KEY (ano)
);

CREATE TABLE IF NOT EXISTS student(
    sno INT,
    sname VARCHAR,
    spasswd TEXT,
    ssex INT,
    sdept TEXT,
    srank, INT,
    sphnum, TEXT,
    PRIMARY KEY (sno)
);

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
    estate INT
    PRIMARY KEY (eno)
);

