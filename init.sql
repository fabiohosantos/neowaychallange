
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
