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
