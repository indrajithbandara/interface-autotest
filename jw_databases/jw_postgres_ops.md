    1  /mnt/app/pgsql/bin/initdb -D /mnt/data/pgsql/
    2  vim /mnt/data/pgsql/pg_hba.conf
    3  vim /mnt/data/pgsql/postgresql.conf
    4  cat >> /etc/sysctl.conf <<EOF
    5  kernel.sem = 50100 128256000 50100 2560
    6  EOF
    7  exit
    8  /mnt/app/pgsql/bin/pg_ctl -D /mnt/data/pgsql/ -l /mnt/log/pgsql/pgsql.log start
    9  cat /mnt/log/pgsql/pgsql.log
   10  /mnt/app/pgsql/bin/psql -d postgres
   11  /mnt/app/pgsql/bin/pg_ctl -D /mnt/data/pgsql/ -l /mnt/log/pgsql/pgsql.log restart
   12  netstat -lntp
   13  history |grep pgsql
   14  /mnt/app/pgsql/bin/psql -d postgres
   15  vim /mnt/data/pgsql/pg_hba.conf
   16  ip add
   17  /mnt/app/pgsql/bin/pg_ctl -D /mnt/data/pgsql/ -l /mnt/log/pgsql/pgsql.log restart
   18  ip add
   19  vim /mnt/data/pgsql/pg_hba.conf
   20  /mnt/app/pgsql/bin/pg_ctl -D /mnt/data/pgsql/ -l /mnt/log/pgsql/pgsql.log restart
   21  /mnt/app/pgsql/bin/psql -d postgres
   22  cat /mnt/data/pgsql/pg_hba.conf
   23  exit
   24  /mnt/app/pgsql/bin/psql -d postgres
   25  /mnt/app/pgsql/bin/psql --help
   26  /mnt/app/pgsql/bin/psql -d gre_dev -U gre_dev -W 123456
   27  /mnt/app/pgsql/bin/psql -d gre_dev -U gre_dev -W
   28  /mnt/app/pgsql/bin/psql -d postgres
   29  /mnt/app/pgsql/bin/psql -d gre_dev -U grp_dev -W
   30  /mnt/app/pgsql/bin/psql -d grp_dev -U grp_dev -W
   31  /mnt/app/pgsql/bin/psql -d postgres
   32  /mnt/app/pgsql/bin/psql -d grp_dev -U grp_dev -W
   33  /mnt/app/pgsql/bin/psql -d postgres
   34  /mnt/app/pgsql/bin/psql -d postgres
   35  clear
   36  history
