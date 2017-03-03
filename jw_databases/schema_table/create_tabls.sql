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


initdb /var/lib/pgsql/data/
pg_ctl -D /var/lib/pgsql/data -l logfile start


--CREATE FUNCTION aaa() RETURNS void AS $$
--DECLARE
--    tmp VARCHAR(512);
--DECLARE names CURSOR FOR
--    select tablename from pg_tables where schemaname='public';
--BEGIN
--  FOR stmt IN names LOOP
--    tmp := 'DROP TABLE '|| quote_ident(stmt.tablename) || ' CASCADE;';
--RAISE NOTICE 'notice: %', tmp;
--    EXECUTE 'DROP TABLE '|| quote_ident(stmt.tablename) || ' CASCADE;';
--  END LOOP;
--  RAISE NOTICE 'finished .....';
--END;
--
--
--$$ LANGUAGE plpgsql;

调用时用：
select aaa();


