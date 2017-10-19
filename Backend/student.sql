<<<<<<< HEAD
CREATE TABLE public.Student
(
    idstudent SERIAL PRIMARY KEY NOT NULL,
    traitID INT,
    pictureID INT,
    major VARCHAR(45),
    creditHours VARCHAR(45),
    degree VARCHAR(45)
);
=======
CREATE TABLE public.Student
(
    idstudent SERIAL PRIMARY KEY NOT NULL,
    traitID INT,
    pictureID INT,
    major VARCHAR(45),
    creditHours VARCHAR(45),
    degree VARCHAR(45)
);
>>>>>>> c9d69db426ac4532f4d8edbc6797f95a7aad8196
CREATE UNIQUE INDEX Student_idstudent_uindex ON public.Student (idstudent);