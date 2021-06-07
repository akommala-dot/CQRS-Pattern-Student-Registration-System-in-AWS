import pymysql
import logging
import sys
import json
import os
endpoint = 'student-read-db.cufvs6xowc1l.us-east-1.rds.amazonaws.com'
username = 'admin'
password = 'password'
db_name = 'student'
db_port = 3306
logger = logging.getLogger()
logger.setLevel(logging.INFO)
try:
    conn = pymysql.connect(host=endpoint, user=username, passwd=password, db=db_name, connect_timeout=10, port=db_port)
    print("Connected")
except pymysql.MySQLError as e:
    logger.error("ERROR: Unexpected error: Could not connect to MySQL instance.")
    logger.error(e)
    sys.exit()
logger.info("SUCCESS: Connection to RDS MySQL instance succeeded")

def lambda_handler( event,context ) :
    cur = conn.cursor()
    cur.execute("SELECT * FROM STUDENTS")
    print("**********************Student List************************")
    print('SID  SNAME   SEMAIL      ENROLL DISENROLL')
    for row in cur.fetchall() :
        print(row[0], row[1], row[2],row[3], row[4])
    cur.execute("SELECT S.SID,SNAME,SEMAIL,CNAME,CREDITS FROM STUDENTS S,COURSES C,ENROLLMENTS E WHERE S.SID=E.SID AND E.CID=C.CID;")
    print("**************************Student Enrollments List***********************")
    for row in cur.fetchall() :
        print(row[0], row[1], row[2],row[3], row[4])
    cur.execute("SELECT S.SID,SNAME,SEMAIL,CNAME,CREDITS,GRADE FROM STUDENTS S,COURSES C,ENROLLMENTS E WHERE S.SID=E.SID AND E.CID=C.CID;")
    print("**************************Student Grades Listt***********************")
    for row in cur.fetchall() :
        print(row[0], row[1], row[2],row[3], row[4], row[5])