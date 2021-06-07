import pymysql
import logging
import sys
import json
import os

endpoint = 'student-write-db.cufvs6xowc1l.us-east-1.rds.amazonaws.com'
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
    record = event["Records"][0]
    body = record["body"]
    command = body.split(" ")[0]
    if command == "sregister":
        studentid = body.split(" ")[1]
        name = body.split(" ")[2]
        email = body.split(" ")[3]
        enroll = body.split(" ")[4]
        disenroll = body.split(" ")[5]
        with conn.cursor() as cur:
            cur.execute('INSERT INTO STUDENTS (SID, SNAME, SEMAIL,SENROLL,SDISENROLL) values(%s, %s , %s, %s, %s)',(studentid, name, email, enroll,  disenroll))
        conn.commit()
    elif command == "cregister":
        courseid = body.split(" ")[1]
        cname = body.split(" ")[2]
        credit = body.split(" ")[3]
        with conn.cursor() as cur:
            cur.execute('INSERT INTO COURSES (CID, CNAME, CREDITS) values(%s, %s , %s)',(courseid, cname, credit))
        conn.commit()
    elif command == "enroll":
        studentid = body.split(" ")[1]
        courseid = body.split(" ")[2]
        grade = body.split(" ")[3]
        with conn.cursor() as cur:
            cur.execute('INSERT INTO ENROLLMENTS (SID, CID, GRADE) values(%s, %s , %s)',(studentid, courseid, grade))
        conn.commit()
    elif command == "disenroll":
        studentid = body.split(" ")[1]
        courseid = body.split(" ")[2]
        with conn.cursor() as cur:
            cur.execute('DELETE FROM ENROLLMENTS WHERE SID= %s AND CID= %s;',(studentid, courseid))
            cur.execute('INSERT INTO DISENROLLMENTS (SID, CID) values(%s, %s)',(studentid, courseid))
        conn.commit()
    elif command=='sdelete':
        sid= body.split(" ")[1]
        with conn.cursor() as cur:
            cur.execute('DELETE FROM STUDENTS WHERE SID= %s;',(sid))
        conn.commit()
    elif command=='cdelete':
        cid= body.split(" ")[1]
        with conn.cursor() as cur:
            cur.execute('DELETE FROM COURSES WHERE CID= %s;',(cid))
        conn.commit()
    elif command=='ddelete':
        sid= body.split(" ")[1]
        cid= body.split(" ")[2]
        with conn.cursor() as cur:
            cur.execute('DELETE FROM DISENROLLMENTS WHERE SID= %s AND CID= %s;',(sid,cid))
        conn.commit()
    elif command =='supdate':
        sid= body.split(" ")[1]
        senrollment = body.split(" ")[2]
        sdisenrollment = body.split(" ")[3]
        with conn.cursor() as cur:
            cur.execute('UPDATE STUDENTS SET SENROLL= %s , SDISENROLL= %s where SID= %s;',(senrollment, sdisenrollment, sid))
            conn.commit()
        conn.commit()