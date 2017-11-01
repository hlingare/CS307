CREATE TABLE public.Student
(
    idstudent SERIAL PRIMARY KEY NOT NULL,
    traitID INT,
    pictureID INT,
    major VARCHAR(45),
    creditHours VARCHAR(45),
    degree VARCHAR(45)
);
CREATE UNIQUE INDEX Student_idstudent_uindex ON public.Student (idstudent);