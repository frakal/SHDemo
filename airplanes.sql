CREATE TABLE crew_member (
    id              SERIAL PRIMARY KEY,
    full_name       VARCHAR(100) NOT NULL,
    date_of_birth   TIMESTAMP
);

CREATE TABLE aircraft (
    id       SERIAL PRIMARY KEY,
    name     VARCHAR(50) NOT NULL
);

CREATE TABLE aircraft_crew (
    id              SERIAL PRIMARY KEY,
    aircraft_id     INTEGER REFERENCES aircraft,
    crew_id         INTEGER REFERENCES crew_member
);


/* Random test data */
INSERT INTO crew_member (full_name, date_of_birth) VALUES ('Ritchie Blackmore', '2000-04-18 00:00:00'), ('Ian Gillan', '1978-08-14 00:00:00'), ('Roger Glover', '1988-08-14 00:00:00'), ('Ian Paice', '1998-08-14 00:00:00'), ('Jon Lord', '2008-08-14 00:00:00')

INSERT INTO aircraft(name) VALUES ('Smoke'), ('Fireball'), ('Stormbringer'), ('Speedking');

INSERT INTO aircraft_crew(crew_id, aircraft_id) VALUES (1,1), (1,2), (1,3), (2,2), (3,4), (4,4);

SELECT full_name FROM crew_member ORDER BY date_of_birth LIMIT 1; /* Oldest */
SELECT full_name FROM crew_member ORDER BY date_of_birth LIMIT 1 OFFSET 3; /* 4th oldest */
SELECT full_name FROM crew_member ORDER BY (SELECT COUNT(*) FROM aircraft_crew WHERE aircraft_crew.crew_id = crew_member.id) DESC LIMIT 1; /* Most experienced */
SELECT full_name FROM crew_member ORDER BY (SELECT COUNT(*) FROM aircraft_crew WHERE aircraft_crew.crew_id = crew_member.id) ASC LIMIT 1; /* Least experienced */
