-- create the databases
CREATE DATABASE IF NOT EXISTS users_db;


use users_db

CREATE TABLE new_users (
    id INT AUTO_INCREMENT,
    f_name VARCHAR(30),
    l_name VARCHAR(30),
    address VARCHAR(30),
    phone VARCHAR(11),
    username VARCHAR(30),
    password VARCHAR(20),
    email VARCHAR(30),
    PRIMARY KEY(id)
);

