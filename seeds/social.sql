-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS posts;
DROP TABLE IF EXISTS users;


-- Create the table without the foreign key first.
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username text,
    email text
);

-- Then the table with the foreign key second.
CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    title text,
    content text,
    views int,
-- The foreign key name is always {other_table_singular}_id
    user_id int,
    constraint fk_user foreign key(user_id)
        references users(id)
        on delete cascade
);

INSERT INTO users (username, email) VALUES ('TestUsername1', 'test1@email.com');
INSERT INTO users (username, email) VALUES ('TestUsername2', 'test2@email.com');
INSERT INTO users (username, email) VALUES ('TestUsername3', 'test3@email.com');

INSERT INTO posts (title, content, views, user_id) VALUES ('Test Title1 for user 1', 'Hello this is test post 1 u1', 39, 1);
INSERT INTO posts (title, content, views, user_id) VALUES ('Test Title2 for user 1', 'Hello this is test post 2 u1', 29, 1);
INSERT INTO posts (title, content, views, user_id) VALUES ('Test Title3 for user 1', 'Hello this is test post 3 u1', 102, 1);
INSERT INTO posts (title, content, views, user_id) VALUES ('Test Title1 for user 2', 'Hello this is test post 1 u2', 74, 2);
INSERT INTO posts (title, content, views, user_id) VALUES ('Test Title2 for user 2', 'Hello this is test post 2 u2', 39, 2);
INSERT INTO posts (title, content, views, user_id) VALUES ('Test Title3 for user 2', 'Hello this is test post 3 u2', 87, 2);
INSERT INTO posts (title, content, views, user_id) VALUES ('Test Title1 for user 3', 'Hello this is test post 1 u3', 21, 3);
INSERT INTO posts (title, content, views, user_id) VALUES ('Test Title2 for user 3', 'Hello this is test post 2 u3', 123, 3);
INSERT INTO posts (title, content, views, user_id) VALUES ('Test Title3 for user 3', 'Hello this is test post 3 u3', 12, 3);