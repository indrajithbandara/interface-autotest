--建立角色
CREATE ROLE pms_dev LOGIN
  ENCRYPTED PASSWORD 'md58aa7ce0873f150936ed654b63a077998'
  SUPERUSER INHERIT CREATEDB CREATEROLE NOREPLICATION;

--建立数据库
CREATE DATABASE pms_dev
  WITH OWNER = pms_dev
       ENCODING = 'UTF8'
       TABLESPACE = pg_default
       LC_COLLATE = 'zh_CN.UTF-8'
       LC_CTYPE = 'zh_CN.UTF-8'
       CONNECTION LIMIT = -1;
GRANT CONNECT, TEMPORARY ON DATABASE pms_dev TO public;
GRANT ALL ON DATABASE pms_dev TO pms_dev;

--建立schema
CREATE SCHEMA pms_dev
  AUTHORIZATION pms_dev;

--安装加密扩展包
create extension pgcrypto;
--安装分区扩展包
create extension pg_pathman;



GRANT CONNECT, TEMPORARY ON DATABASE pms_dev TO public;
GRANT ALL ON DATABASE pms_dev TO pms_dev;

--建立schema
CREATE SCHEMA pms_dev
  AUTHORIZATION pms_dev;

--安装加密扩展包
create extension pgcrypto;
--安装分区扩展包
create extension pg_pathman;

GRANT CONNECT, TEMPORARY ON DATABASE grp_dev TO public;
GRANT ALL ON DATABASE grp_dev TO grp_dev;

--建立schema
CREATE SCHEMA grp_dev
  AUTHORIZATION grp_dev;

--安装加密扩展包
create extension pgcrypto;
--安装分区扩展包
create extension pg_pathman;

GRANT CONNECT, TEMPORARY ON DATABASE pcm_dev TO public;
GRANT ALL ON DATABASE pcm_dev TO pcm_dev;

--建立schema
CREATE SCHEMA pcm_dev
  AUTHORIZATION pcm_dev;

--安装加密扩展包
create extension pgcrypto;
--安装分区扩展包
create extension pg_pathman;




-- Use this to show the current search_path
-- Should return: "$user",public
SHOW search_path;

-- Create another schema
CREATE SCHEMA my_schema;
GRANT ALL ON SCHEMA my_schema TO my_user;

-- To change search_path on a connection-level
SET search_path TO my_schema;

-- To change search_path on a database-level
ALTER database "my_database" SET search_path TO my_schema;


