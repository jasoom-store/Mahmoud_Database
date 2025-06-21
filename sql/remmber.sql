-- MySQL
SELECT * FROM `tabel_name`

CREATE DATABASE tettt CHARACTER SET utf8;

-- SQLite
SELECT * FROM `tabel_name`

---------------------------------------------------------
-- Delete All from table

-- MySQL
DELETE FROM `table_name`
ALTER TABLE 'table_name' AUTO_INCREMENT = 1

-- SQLite
DELETE FROM `table_name`
UPDATE SQLITE_SEQUENCE SET SEQ = 0 WHERE NAME = 'table_name'

---------------------------------------------------------
-- Data types

-- MySQL
string
    TEXT
    BLOB 
    CHAR
    VARCHAR
    ENUM ('male', 'female') = 65535 
    SET ('one', 'two') = 64 
    BINARY
    VARBINARY

json
    JSON

int = Signed | Unsigned | default value is Signed
    TINYINT -128 to 127 = 255
    SMALLINT -32768 to 32767 = 
    MEDIUMINT -8388608 to 8388607
    INT = Equal to INT(size)
    BIGINT
    FLOAT 0 to 24, becomes FLOAT() | 25 to 53, becomes DOUBLE()

date & datetime 
    DATE '1000-01-01' to '9999-12-31'
    TIMESTAMP '1970-01-01 00:00:01.000000' to '2038-01-19 03:14:07.499999'
    DATETIME '1000-01-01 00:00:00.000000' to '9999-12-31 23:59:59.499999'
    TIME 
    YEAR 

boolean
    BOOL = TRUE | FALSE
    BOOLEAN
    
null
    NULL


-- SQLite
NULL = Null
INTEGER = int
REAL = float
TEXT = string | json | date | datetime
BLOB = big string | file as string

----------------------------------------------------------------
create table colors_log (
    'color_name' VARCHAR(30) not null,
    'R' TINYINT Unsigned, -128 t 127 | 255
    'G' TINYINT Unsigned, 
    'B' TINYINT Unsigned
);

rgb(0-255, 0-255, 0-255)
----------------------------------------------------------------

SELECT users.user_id, users.username, posts.user_id, posts.title FROM users, posts


users(
    user_id,
    username,
    password,
    gendor,

)

SELECT username, password, gendor FROM users

