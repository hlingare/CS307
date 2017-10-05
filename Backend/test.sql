drop DATABASE test;
create DATABASE test;
use test;
create TABLE student (
       id   INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
       name VARCHAR(20),
       puid VARCHAR(20),
       standing ENUM('Freshman','Sophomore','Junior','Senior'),
       degree ENUM('BS','MS','PhD'),
       major VARCHAR(20)
);
#
# add rows to a student table
#
INSERT INTO `student` (`id`, `name` , `puid`, `standing`, `degree`, `major`) VALUES (NULL, "sanat", "0027914763", 'Freshman', 'BS', "Computer Science");

INSERT INTO `student` (`id`, `name` , `puid`, `standing`, `degree`, `major`) VALUES (NULL, "john", "0024763997", 'Sophomore', 'BS', "Health Science");

INSERT INTO `student` (`id`, `name` , `puid`, `standing`, `degree`, `major`) VALUES (NULL, "theron", "0015414568", 'Junior', 'MS', "Economics");

INSERT INTO `student` (`id`, `name` , `puid`, `standing`, `degree`, `major`) VALUES (NULL, "dog", "0015619574", 'Senior', 'PhD', "Physics");

INSERT INTO `student` (`id`, `name` , `puid`, `standing`, `degree`, `major`) VALUES (NULL, "frank", "0018896542", 'Junior', 'MS', "Finance");

create table course (
       id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
       name varchar(20),
       cid varchar(20),
       department varchar(100),
       degree ENUM('BS','MS','PhD')
);
#
# add courses to a course table
#

insert into `course` (`id`, `name`, `cid`, `department`, `degree`) values (null, "CS", "25000", "Computer Science", "BS");

insert into `course` (`id`, `name`, `cid`, `department`, `degree`) values (null, "CS", "25100", "Computer Science", "BS");

insert into `course` (`id`, `name`, `cid`, `department`, `degree`) values (null, "CS", "25200", "Computer Science", "BS");

insert into `course` (`id`, `name`, `cid`, `department`, `degree`) values (null, "MGMT", "20100","Management", "BS");

insert into `course` (`id`, `name`, `cid`, `department`, `degree`) values (null, "EAPS", "30100","Earth and Planetary Sciences", "BS");



create table student_course (
       id int not null primary key auto_increment, 
       studentID int,
       courseID int,
       foreign key(studentID) references student(id),
       foreign key(courseID) references course(id)
);
insert into `student_course` (`id`, `studentID`, `courseID`) values (null, 1, 1);
insert into `student_course` (`id`, `studentID`, `courseID`) values (null, 1, 2);
insert into `student_course` (`id`, `studentID`, `courseID`) values (null, 1, 3);
insert into `student_course` (`id`, `studentID`, `courseID`) values (null, 2, 1);
insert into `student_course` (`id`, `studentID`, `courseID`) values (null, 2, 3);
insert into `student_course` (`id`, `studentID`, `courseID`) values (null, 3, 3);
insert into `student_course` (`id`, `studentID`, `courseID`) values (null, 3, 2);
insert into `student_course` (`id`, `studentID`, `courseID`) values (null, 4, 1);
insert into `student_course` (`id`, `studentID`, `courseID`) values (null, 4, 3);
insert into `student_course` (`id`, `studentID`, `courseID`) values (null, 5, 4); 

select a.name, a.puid, a.standing, a.degree, a.major, b.name, b.cid, b.department, b.degree from student a, course b, student_course c where c.studentID=a.id and c.courseID=b.id;
