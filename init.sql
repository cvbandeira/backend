/* 
crie uma tabela users com pelo menos:

- id: chave primária;
- name: nome do usuário;
- email: e-mail único.
*/



CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100)
);

INSERT INTO users (name, email) VALUES
('JOSÉ', 'jose@gmail.com'),
('MARIA', 'maria@hotmail.com'),
('ISAQUE', 'isaque@outlook.com');