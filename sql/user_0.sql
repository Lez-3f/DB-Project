CREATE TABLE IF NOT EXISTS user(
    uno INT,
    uname VARCHAR,
    usex INT,
    upasswd TEXT,
    PRIMARY KEY(uno)
);

CREATE TABLE IF NOT EXISTS admintt(
    ano INT,
    PRIMARY(ano)
    FOREIGN KEY(ano) REFERENCES user(uno),
);

CREATE TABLE IF NOT EXISTS teacher(
    tno INT,
    tdept VARCHAR,
    tphnum CHAR(20),
    PRIMARY(tno),
    FOREIGN KEY(tno) REFERENCES user(uno),
);

CREATE TABLE IF NOT EXISTS student(
    sno INT,
    sdept VARCHAR,
    sclazz VARCHAR
    srank INT,
    sphnum CHAR(20),
    PRIMARY KEY (sno),
    FOREIGN KEY(sno) REFERENCES user(uno),
);

