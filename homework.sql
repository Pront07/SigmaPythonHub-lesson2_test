CREATE TABLE IF NOT EXISTS comment (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    comment TEXT,
    article_id INTEGER REFERENCES arcticle(id),
    user_id INTEGER REFERENCES users(id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO comment (name, comment, article_id, user_id) VALUES ('Hi all', 'im here', 1, 1)

INSERT INTO comment (name, comment, article_id, user_id) VALUES ('Hi all', 'im here', 1, 1)

INSERT INTO comment (name, comment, article_id, user_id) VALUES ('Hi all', 'im here', 1, 1)