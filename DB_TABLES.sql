CREATE DATABASE student;

USE student;

CREATE TABLE STUDENTS(
SID varchar(10) primary key, 
SNAME  varchar(20),
SEMAIL  varchar(50),
SENROLL int check(SENROLL>=0 AND SENROLL<=3),
SDISENROLL int);

CREATE TABLE COURSES(
CID varchar(10) primary key, 
CNAME  varchar(50),
CREDITS int);

CREATE TABLE ENROLLMENTS(
SID varchar(10),
CID varchar(10),
GRADE VARCHAR(5));

CREATE TABLE DISENROLLMENTS(
SID varchar(10),
CID varchar(10),
DATETIME DATE,
COMMENTS VARCHAR(50));
