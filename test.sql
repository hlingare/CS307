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
