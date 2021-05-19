DROP TABLE IF EXISTS books CASCADE;
DROP TABLE IF EXISTS genres CASCADE;
DROP TABLE IF EXISTS stylistics CASCADE;
DROP TABLE IF EXISTS authors CASCADE;
DROP TABLE IF EXISTS countries CASCADE;
DROP TABLE IF EXISTS persons CASCADE;
DROP TABLE IF EXISTS person_has_book CASCADE;

CREATE TABLE genres (
    id SERIAL PRIMARY KEY,
    name VARCHAR(32) NOT NULL
);

CREATE TABLE stylistics (
    id SERIAL PRIMARY KEY,
    name VARCHAR(32) NOT NULL
);

CREATE TABLE countries (
    id SERIAL PRIMARY KEY,
    name VARCHAR(32) NOT NULL
);

CREATE TABLE authors (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(32) NOT NULL,
    last_name VARCHAR(32) NOT NULL,
    birth_date DATE,
    country_id INT REFERENCES countries ON DELETE SET NULL
);

CREATE TABLE books (
    id SERIAL PRIMARY KEY,
    title VARCHAR(64) NOT NULL,
    author_id INT NOT NULL REFERENCES authors ON DELETE CASCADE,
    genre_id INT REFERENCES genres ON DELETE SET NULL,
    stylistics_id INT REFERENCES stylistics ON DELETE SET NULL,
    pages_count INT,
    release_date DATE,
    age_restrictions VARCHAR(8)
);

CREATE TABLE persons (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(32) NOT NULL,
    last_name VARCHAR(32) NOT NULL,
    age INT
);


CREATE TABLE person_has_book (
    person_id INT NOT NULL REFERENCES persons,
    book_id INT NOT NULL REFERENCES books,
    PRIMARY KEY (person_id, book_id)
);
