import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="123456",
    db="test",
    cursorclass = pymysql.cursors.DictCursor
)