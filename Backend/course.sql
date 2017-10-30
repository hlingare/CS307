<<<<<<< HEAD
CREATE TABLE public.course
(
    idcourse SERIAL PRIMARY KEY NOT NULL,
    name VARCHAR(45),
    code VARCHAR(45),
    traitID INT,
    audit BOOLEAN,
    profList INT,
    prereq INT,
    upvote INT,
    timings VARCHAR(200)
);
CREATE UNIQUE INDEX course_idcourse_uindex ON public.course (idcourse);
ALTER TABLE public.course
ADD CONSTRAINT course_trait_idtrait_fk
=======
CREATE TABLE public.course
(
    idcourse SERIAL PRIMARY KEY NOT NULL,
    name VARCHAR(45),
    code VARCHAR(45),
    traitID INT,
    audit BOOLEAN,
    profList INT,
    prereq INT,
    upvote INT,
    timings VARCHAR(200)
);
CREATE UNIQUE INDEX course_idcourse_uindex ON public.course (idcourse);
ALTER TABLE public.course
ADD CONSTRAINT course_trait_idtrait_fk
>>>>>>> c9d69db426ac4532f4d8edbc6797f95a7aad8196
FOREIGN KEY (traitid) REFERENCES trait (idtrait);