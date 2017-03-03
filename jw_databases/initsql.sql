PostgreSQL是一个多用户数据库，可以为不同用户指定允许的权限。
http://www.cnblogs.com/stephen-liu74/archive/2012/05/18/2302639.html
角色
PostgreSQL使用角色的概念管理数据库访问权限。 根据角色自身的设置不同，一个角色可以看做是一个数据库用户，或者一组数据库用户。 角色可以拥有数据库对象(比如表)以及可以把这些对象上的权限赋予其它角色， 以控制谁拥有访问哪些对象的权限。
操作角色的语句：

create role db_role1; /*--创建角色*/
drop role db_role1;  /*--删除角色*/
select rolename from pg_roles; /*--查看所有角色*/
/du  --在命令格式下查看所有角色的命令
角色的权限
一个数据库角色可以有很多权限，这些权限定义了角色和拥有角色的用户可以做的事情。

create role db_role1 LOGIN; --创建具有登录权限的角色db_role1
create role db_role2 SUPERUSER; --创建具有超级用户权限的角色
create role db_role3 CREATEDB; --创建具有创建数据库权限的角色
create role db_role4 CREATEROLE --创建具有创建角色权限的角色
alter role db_role1 nologin nocreatedb; --修改角色取消登录和创建数据库权限
用户
其实用户和角色都是角色，只是用户是具有登录权限的角色。
create user db_user1 password '123'; --创建用户
create role db_user1 password '123' LOGIN;  --同上一句等价
drop user db_user1;   --删除用户
alter user db_user1 password '123456'; --修改密码
alter user db_user1 createdb createrole; --对用户授权
赋予角色控制权限
我们可以使用GRANT 和REVOKE命令赋予用户角色，来控制权限。
create user db_user1; --创建用户1
create user db_user2; --创建用户2
create role db_role1 createdb createrole; --创建角色1
grant db_role1 to db_user1,db_user2; --给用户1,2赋予角色1,两个用户就拥有了创建数据库和创建角色的权限
revoke db_role1 from db_user1; --从用户1移除角色1，用户不在拥有角色1的权限