CREATE TABLE users (id SERIAL PRIMARY KEY, username TEXT, password TEXT, admin BOOLEAN);

CREATE TABLE hints (id SERIAL PRIMARY KEY, owner_id INT REFERENCES users, decimal INT, content TEXT);

CREATE TABLE scores (id SERIAL PRIMARY KEY, owner_id INT REFERENCES users, SCORE INT, HINTS INT);

CREATE TABLE friends (id SERIAL PRIMARY KEY, user_id INT REFERENCES users, friend_id INT REFERENCES users);