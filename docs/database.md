## 数据库结构说明

### 管理员表（后台更改）

表名：`admin`

| 属性        | 键类型 | 数据类型    | 说明    |
| --------- | --- | ------- | ----- |
| Ano       | 主键  | int     | 管理员编号 |
| Aname     |     | varchar | 管理员姓名 |
| Apassword |     | text    | 管理员密码 |

### 学生表

表名：`student`

| 属性          | 键类型 | 数据类型    | 说明                 |
| ----------- | --- | ------- | ------------------ |
| Sno         | 主键  | int     | 学生编号               |
| Sname       |     | varchar | 学生姓名               |
| Ssex        |     | int     | 学生性别 0-♀， 1-♂      |
| Sdepartment | 可空  | text    | 院系名称               |
| Sidentity   | 可空  | int     | 学生身份 0-普通学生， 1-特长生 |
| Sphnumber   |     | int     | 学生手机号码             |

### 场地信息表

表名：`court`

| 属性     | 键类型 | 数据类型    | 说明     |
| ------ | --- | ------- | ------ |
| Cno    | 主键  | int     | 场地编号   |
| Cname  |     | varchar | 场地名称   |
| Cinfo  | 可空  | text    | 场地描述   |
| Ctype  |     | int     | 场地类型   |
| Cstate |     | int     | 场地当前状态 |

### 体育器材表

表名：`equipment`

| 属性     | 键类型 | 数据类型    | 说明     |
| ------ | --- | ------- | ------ |
| Eno    | 主键  | int     | 器材编号   |
| Ename  |     | varcahr | 器材名称   |
| Etnum  |     | int     | 器材总数量  |
| Eanum  |     | int     | 器材可用数量 |
| Estate |     | int     | 器材状态   |

### 预约信息表

表名：`reservation`

| 属性     | 键类型 | 数据类型 | 说明     |
| ------ | --- | ---- | ------ |
| Rno    | 主键  | int  | 预约订单编号 |
| Rstu   | 外码  | int  | 预约者编号  |
| Rcourt | 外码  | int  | 场地名称   |
| Rdate  | 日期  |      | 预约日期   |
| Rstate | 状态  |      | 预约的状态  |


