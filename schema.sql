CREATE TABLE users (
    id SERIAL PRIMARY KEY, 
    username TEXT UNIQUE, 
    password TEXT
    );
CREATE TABLE datings (
    id SERIAL PRIMARY KEY, 
    dating TEXT UNIQUE
    );
CREATE TABLE types (
    id SERIAL PRIMARY KEY, 
    type_name TEXT UNIQUE
    );
CREATE TABLE locations (
    id SERIAL PRIMARY KEY, 
    name TEXT UNIQUE, 
    dating_id INTEGER REFERENCES datings, 
    type_id INTEGER REFERENCES types,
    createdby_id INTEGER REFERENCES users
    ); 
CREATE TABLE comments (
    id SERIAL PRIMARY KEY, 
    content TEXT, user_id INTEGER REFERENCES users, 
    sent_at TIMESTAMP, 
    location_id INTEGER REFERENCES locations
    );
CREATE TABLE coordinates (
    id SERIAL PRIMARY KEY, 
    location_id INTEGER REFERENCES locations, 
    x FLOAT8, 
    y FLOAT8, 
    z FLOAT8
    );
