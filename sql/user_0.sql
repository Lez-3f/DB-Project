CREATE TABLE IF NOT EXISTS user(
    uno INT NOT NULL,
    uname VARCHAR(20) NOT NULL,
    usex INT NOT NULL,
    upasswd TEXT NOT NULL,
    PRIMARY KEY(uno)
);

CREATE TABLE IF NOT EXISTS admintt(
    ano INT NOT NULL,
    PRIMARY KEY(ano),
    CONSTRAINT FK_AD FOREIGN KEY(ano) REFERENCES user(uno)
);

CREATE TABLE IF NOT EXISTS teacher(
    tno INT NOT NULL,
    tdept VARCHAR(100) NOT NULL,
    tphnum CHAR(30),
    PRIMARY KEY(tno),
    CONSTRAINT FK_TC FOREIGN KEY(tno) REFERENCES user(uno)
);

CREATE TABLE IF NOT EXISTS student(
    sno INT,
    sdept VARCHAR(100),
    sclazz VARCHAR(50),
    srank INT,
    sphnum CHAR(30),
    PRIMARY KEY(sno),
    CONSTRAINT FK_ST FOREIGN KEY(sno) REFERENCES user(uno)
);

