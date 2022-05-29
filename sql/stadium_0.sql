CREATE TABLE IF NOT EXISTS court(
    cno INT NOT NULL,
    cname VARCHAR(50),
    cinfo TEXT,
    ctype INT NOT NULL,
    cstate INT NOT NULL,
    PRIMARY KEY (cno)
);

CREATE TABLE IF NOT EXISTS equipment(
    eno INT NOT NULL,
    ename VARCHAR(50) NOT NULL,
    enum_t INT NOT NULL,
    enum_a INT NOT NULL,
    estate INT NOT NULL,
    PRIMARY KEY (eno)
);

-- DROP TABLE reservation;
CREATE TABLE IF NOT EXISTS reservation(
    rno INT NOT NULL,
    rguest INT NOT NULL,
    rcourt INT NOT NULL,
    rdate DATE NOT NULL,
    rbegin TIME NOT NULL,
    rend TIME NOT NULL,
    rstate INT NOT NULL,
    rreason TEXT,
    PRIMARY KEY(rno),
    CONSTRAINT FK_GST_RS FOREIGN KEY(rguest) REFERENCES user(uno),
    CONSTRAINT FK_CT FOREIGN KEY(rcourt) REFERENCES court(cno)
);

CREATE TABLE IF NOT EXISTS rental(
    rtno INT NOT NULL,
    rtguest INT NOT NULL,
    rteq INT NOT NULL,
    rtnum INT NOT NULL,
    rtstate INT NOT NULL,
    PRIMARY KEY(rtno),
    CONSTRAINT FK_GST_RT FOREIGN KEY(rtguest) REFERENCES user(uno),
    CONSTRAINT FK_EQ FOREIGN KEY(rteq) REFERENCES equipment(eno)
);

CREATE TABLE IF NOT EXISTS dept_info(
    dname VARCHAR(50) NOT NULL,
    dhour_r FLOAT NOT NULL,
    dnum_rt INT NOT NULL,
    PRIMARY KEY(dname)
);

CREATE TABLE IF NOT EXISTS sport_info(
    sptype VARCHAR(50) NOT NULL,
    spname VARCHAR(50) NOT NULL,
    sphour_r FLOAT NOT NULL,
    spnum_rt INT NOT NULL,
    PRIMARY KEY(sptype)
)