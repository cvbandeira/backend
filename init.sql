
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100)
);

INSERT INTO users (name, email) VALUES
('JOSÉ', 'jose@gmail.com'),
('MARIA', 'maria@hotmail.com'),
('ISAQUE', 'isaque@outlook.com');