CREATE TABLE users (id SERIAL PRIMARY KEY, username TEXT, password TEXT, admin BOOLEAN);

CREATE TABLE hints (id SERIAL PRIMARY KEY, owner_id INT REFERENCES users, decimal INT, content TEXT);

CREATE TABLE scores (id SERIAL PRIMARY KEY, owner_id INT REFERENCES users, SCORE INT, HINTS INT);

CREATE TABLE groups (id SERIAL PRIMARY KEY, name TEXT);

CREATE TABLE group_members (group_id INT REFERENCES groups, member_id INT REFERENCES users);