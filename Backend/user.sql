CREATE TABLE public.Users
(
    iduser SERIAL PRIMARY KEY NOT NULL,
    username VARCHAR(45),
    password VARCHAR(45),
    cellNum VARCHAR(45),
    fName VARCHAR(45),
    lname VARCHAR(45),
    dob VARCHAR(45),
    email VARCHAR(45),
    timeCreated TIMESTAMP,
    column_10 INT,
    studentID INT
);
CREATE UNIQUE INDEX Users_iduser_uindex ON public.Users (iduser);

ALTER TABLE public.users
ADD CONSTRAINT users_student_idstudent_fk
FOREIGN KEY (studentid) REFERENCES student (idstudent);