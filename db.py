import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="password",
    db="test",
    cursorclass = pymysql.cursors.DictCursor
)
