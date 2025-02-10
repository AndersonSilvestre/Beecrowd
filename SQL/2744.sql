--Criação da tabela
CREATE TABLE account (
    id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name varchar(100),
    login varchar(50),
    password varchar(50)
)
--Inserção dos Usuarios
INSERT INTO account (name, login, password)
VALUES
    ('Joyce P. Parry', 'Promeraw', 'noh1Oozei'),
    ('Michael T. Gonzalez', 'Phers1942', 'Iath3see9bi'),
    ('Heather W. Lawless', 'Hankicht', 'diShono4'),
    ('Otis C. Hitt', 'Conalothe', 'zooFohH7w'),
    ('Roger N. Brownfield', 'Worseente', 'fah7ohNg');
-- Execução do Ex.
SELECT id, password, MD5(password) FROM account;
