# 使用brew安装mongodb
    - brew install mongodb-community@4.2

# 启动MongoDB
## 方式1
    - brew services start mongodb-community@4.2
    - brew services stop mongodb-community@4.2
## 方式2
    - `vim .bash_profile`
    - `export PATH=/usr/local/Cellar/mongodb-community/4.2.5/bin:${PATH}`
    - sudo mongod

# 假如mac启动后退出后重启报错时：
    `2020-04-20T20:27:24.597+0800 I  CONTROL  [main] Automatically disabling TLS 1.0, to force-enable TLS 1.0 specify --sslDisabledProtocols 'none'`
    `2020-04-20T20:27:24.609+0800 W  ASIO     [main] No TransportLayer configured during NetworkInterface startup`
    `2020-04-20T20:27:24.614+0800 I  CONTROL  [initandlisten] MongoDB starting : pid=2744 port=27017 dbpath=/data/db 64-bit host=zkydeiMac.local`
    `2020-04-20T20:27:24.614+0800 I  CONTROL  [initandlisten] db version v4.2.5`
    `2020-04-20T20:27:24.614+0800 I  CONTROL  [initandlisten] git version: 2261279b51ea13df08ae708ff278f0679c59dc32`
    `2020-04-20T20:27:24.614+0800 I  CONTROL  [initandlisten] allocator: system`
    `2020-04-20T20:27:24.614+0800 I  CONTROL  [initandlisten] modules: none`
    `2020-04-20T20:27:24.614+0800 I  CONTROL  [initandlisten] build environment:`
    `2020-04-20T20:27:24.614+0800 I  CONTROL  [initandlisten]     distarch: x86_64`
    `2020-04-20T20:27:24.614+0800 I  CONTROL  [initandlisten]     target_arch: x86_64`
    `2020-04-20T20:27:24.614+0800 I  CONTROL  [initandlisten] options: {}`
    `2020-04-20T20:27:24.615+0800 I  STORAGE  [initandlisten] exception in initAndListen: NonExistentPath: Data directory /data/db not found., terminating`
    `2020-04-20T20:27:24.615+0800 I  NETWORK  [initandlisten] shutdown: going to close listening sockets...`
    `2020-04-20T20:27:24.615+0800 I  -        [initandlisten] Stopping further Flow Control ticket acquisitions.`
    `2020-04-20T20:27:24.615+0800 I  CONTROL  [initandlisten] now exiting`
    `2020-04-20T20:27:24.615+0800 I  CONTROL  [initandlisten] shutting down with code:100`
    解决办法是按照提示，添加对应的文件夹 `mkdir /data/db`

# 要停止MongoDB一定要正确的退出，不然下次连接数据库会出问题
    `use admin;`
    `db.shutdownServer();`

# mongoDB 中比较符号
| 符号 | 含义 | 示例 |
| ---------- | ---------- | ---------- |
| $lt | 小于 | {'age':{'$lt':20}} |
| $gt | 大于 | {'age':{'$gt':20}} |
| $lte | 小于或等于 | {'age':{'$lte':20}} |
| $gte | 大于或大于 | {'age':{'$gte':20}} |
| $ne | 不等于 | {'age':{'$ne':20}} |
| $in | 在范围内 | {'age':{'$in':20}} |
| $nin | 不在范围内 | {'age':{'$nin':20}} |


| 符号 | 含义 | 示例 | 示例含义
| ---------- | ---------- | ---------- | ---------- |
| $regex | 匹配正则表达式 | {'name':{'$regex':'^M.*'}} | name以M开头 | 
| $exists | 属性是否存在 | {'name':{'$exists':True}} | name属性存在 |
| $type | 类型判断 | {'age':{'$type':'int'}} |  age的类型为int |
| $mod | 数字模操作 | {'age':{'$mod':[5,0]}} |  年龄模5余0 |
| $text | 文本查询 | {'$text':{'$search':'Mike'}} | text类型的属性中包含Mike字符串 |
| $where | 高级条件查询 | {'$where':'obj.fans_count== obj.follows_count'} |  自身粉丝数等于关注数 |




# MongoDB常用的命令
    - `db.stats() ` 查看数据库状态
    - `db.tablename.stats()` 查看具体的表
    - 