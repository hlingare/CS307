CREATE TABLE public.trait
(
    idtrait SERIAL PRIMARY KEY NOT NULL,
    critThink INT,
    math INT,
    memory INT,
    speechDeb INT,
    teamWork INT
);
CREATE UNIQUE INDEX trait_idtrait_uindex ON public.trait (idtrait);

ALTER TABLE public.student
ADD CONSTRAINT student_trait_idtrait_fk
FOREIGN KEY (traitid) REFERENCES trait (idtrait);