CREATE SCHEMA neoway;
	
CREATE TABLE neoway.scores
(
    pk bigint,
    score bigint
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE neoway.scores
    OWNER to postgres;


-- Table: neoway.users

-- DROP TABLE neoway.users;
/*
CREATE TABLE neoway.users
(
    first_name character varying(256) COLLATE pg_catalog."default",
    last_name character varying(256) COLLATE pg_catalog."default",
    email character varying(256) COLLATE pg_catalog."default",
    "Id" SERIAL PRIMARY KEY
--   CONSTRAINT "User_pkey" PRIMARY KEY ("Id")
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.users
    OWNER to postgres;
*/	
