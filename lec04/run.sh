rm -f database.sqlite3
sqlite3 database.sqlite3 < schema.sql
sqlite3 database.sqlite3 < data.sql