-- 1 Creating Tables
/*
Please formulate appropriate SQL statements to create these 6 tables using:
• Sequence number generators whose values automatically increase when data is inserted
• Appropriate data types
• Primary and foreign keys
*/

-- Create table for Student
CREATE TABLE student (
    sid SERIAL PRIMARY KEY,
    firstname VARCHAR(50),
    lastname VARCHAR(50),
    semester INT,
    birthdate DATE
);

-- Create table for Tutor
CREATE TABLE tutor (
    tid SERIAL PRIMARY KEY,
    firstname VARCHAR(50),
    lastname VARCHAR(50),
    issenior BOOLEAN
);

-- Create table for StudyGroup
CREATE TABLE studygroup (
    gid SERIAL PRIMARY KEY,
    tid INT,
    weekday VARCHAR(10),
    room VARCHAR(10),
    starttime TIME,
    FOREIGN KEY (tid) REFERENCES tutor(tid)
);

-- Create table for Exercise
CREATE TABLE exercise (
    eid SERIAL PRIMARY KEY,
    maxpoints INT
);

-- Create table for HandsIn
CREATE TABLE handsin (
    sid INT,
    eid INT,
    achievedpoints INT,
    PRIMARY KEY (sid, eid),
    FOREIGN KEY (sid) REFERENCES student(sid),
    FOREIGN KEY (eid) REFERENCES exercise(eid)
);

-- Create table for Member
CREATE TABLE member (
    sid INT,
    gid INT,
    PRIMARY KEY (sid, gid),
    FOREIGN KEY (sid) REFERENCES student(sid),
    FOREIGN KEY (gid) REFERENCES studygroup(gid)
);


-- 2 Querying Tables I
-- Translate the following queries into equivalent SQL statements that run on the tables created above.

-- 1. Find the different last names of the students whose first name is “Helle”.
SELECT DISTINCT lastname
FROM student
WHERE firstname = 'Helle';

--2. Find all the different last names of students that end with ’sen’.
SELECT DISTINCT lastname
FROM student
WHERE lastname LIKE '%sen';

-- 3. List the first and last names of the tutors that are senior.
SELECT firstname, lastname
FROM tutor
WHERE issenior = TRUE;

-- 4. Find the first and last names of all students who have study group on Wednesday or Friday.
SELECT DISTINCT s.firstname, s.lastname
FROM student s
JOIN member m ON s.sid = m.sid
JOIN studygroup sg ON m.gid = sg.gid
WHERE sg.weekday = 'Wednesday' OR sg.weekday = 'Friday';


-- 3 Querying Tables II
-- Considering the tables created above, identify the missing information that should go into the boxes to make the queries compute the requested information

-- 1. Find all the ids of the study groups without any members.
SELECT SG.gid
FROM studygroup SG
EXCEPT
SELECT M.gid  -- box 1
FROM member M  -- box 2
WHERE M.gid IS NOT NULL;  -- box 3 (optional, depending on DB constraints)

-- 2. Find the first and last names of all students that have “Helle” as tutor.
SELECT S.firstname, S.lastname
FROM student S, member M, tutor T, studygroup SG  -- boxes 1 and 2
WHERE T.firstname = 'Helle' AND T.tid = SG.tid  -- box 3
AND S.sid = M.sid  -- box 4
AND M.gid = SG.gid;  -- box 5

-- 3. Find the IDs of all students born before 01.03.1998 that have the same first name as one of the tutors that are not seniors.
SELECT S.sid
FROM student S, tutor T
WHERE S.birthdate < '1998-03-01'
AND S.firstname = T.firstname
AND T.issenior = FALSE;


-- 4 Manipulating Tables

-- 1. Populate the above created tables by inserting at least one valid tuple per table. Do foreign key impose any restriction?
-- Insert a tutor
INSERT INTO tutor (firstname, lastname, issenior) VALUES ('John', 'Doe', TRUE);

-- Insert a student
INSERT INTO student (firstname, lastname, semester, birthdate) VALUES ('Jane', 'Smith', 1, '2000-01-01');

-- Insert a study group (the tutor with id=1 must exist)
INSERT INTO studygroup (tid, weekday, room, starttime) VALUES (1, 'Monday', 'Room1', '09:00');

-- Insert an exercise
INSERT INTO exercise (maxpoints) VALUES (100);

-- Insert a hands-in (student id=1 and exercise id=1 must exist)
INSERT INTO handsin (sid, eid, achievedpoints) VALUES (1, 1, 80);

-- Insert a member (student id=1 and group id=1 must exist)
INSERT INTO member (sid, gid) VALUES (1, 1);

-- 2. Delete all student tuples from table student for which the first name is ’Tom’.
DELETE FROM student WHERE firstname = 'Tom';


-- 5 Using PostgreSQL



