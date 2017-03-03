1.创建role
[wisdom@localhost ~]$ /mnt/app/pgsql/bin/psql -d postgres
postgres=# create role pms with login;
CREATE ROLE

2.创建用户grp_dev并加入角色pms
postgres=# create user grp_dev with in role pms password '123456';
CREATE ROLE

postgres=# \du
                                   List of roles
 Role name |                         Attributes                         | Member of
-----------+------------------------------------------------------------+-----------
 grp_dev   |                                                            | {pms}
 pms       | Cannot login                                               | {}
 repl      | Superuser                                                  | {}
 wisdom    | Superuser, Create role, Create DB, Replication, Bypass RLS | {}

3.创建数据库
postgres=# create database grp_dev;
CREATE DATABASE
postgres=# \l
                               List of databases
   Name    | Owner  | Encoding |   Collate   |    Ctype    | Access privileges
-----------+--------+----------+-------------+-------------+-------------------
 grp_dev   | wisdom | UTF8     | en_US.UTF-8 | en_US.UTF-8 |
 postgres  | wisdom | UTF8     | en_US.UTF-8 | en_US.UTF-8 |
 template0 | wisdom | UTF8     | en_US.UTF-8 | en_US.UTF-8 | =c/wisdom        +
           |        |          |             |             | wisdom=CTc/wisdom
 template1 | wisdom | UTF8     | en_US.UTF-8 | en_US.UTF-8 | =c/wisdom        +
           |        |          |             |             | wisdom=CTc/wisdom
(4 rows)

4.授权
postgres=# grant all privileges on database grp_dev to pms;
GRANT

5.创建一个schema
[wisdom@localhost ~]$ /mnt/app/pgsql/bin/psql -d grp_dev -U grp_dev
grp_dev=> create schema grp_dev;
CREATE SCHEMA