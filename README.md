# como fazer crud em python e mysql usando flask

Criação do CRUD em Python: com  flask e html para interface web.

tuturial simple de:
como fazer crud em python e mysql usando flask

# requisitos:
Python3: 3.10 +

pip

mysql-connector-python

BD: MySQL 8.3

navegador web

vscode ou outro editor


# linux
1:sudo apt update
sudo apt install python3

2:sudo apt install mysql-server

# windowns

1: Link para baixar python: https://python.org.br/instalacao-windows/

2: mysql: link 1: https://www.alura.com.br/artigos/mysql-do-download-e-instalacao-ate-sua-primeira-tabela

link para baixar mysql: https://dev.mysql.com/downloads/installer/


# Pip 
instalation:  sudo apt install python3-pip
3: pip install mysql-connector-python
4: pip install mysql-connector-python

# criar bd e tabela

- no prompt / cmd:
5: pc@pc: $
mysql -u root -p

CREATE DATABASE empresa;
USE empresa;
CREATE TABLE funcionarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255),
    localizacao VARCHAR(255),
    cargo VARCHAR(255),
    email VARCHAR(255),
    telefone VARCHAR(20)
);



desenvolvido por: Juliao LB
