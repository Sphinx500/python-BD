create database personasDB;


Create table personasdb.personas (
id int auto_increment not null,
nombre varchar(50) null,
edad numeric(10) null,
correo varchar(50) null,
telefono varchar(15) null,
primary key(id)
);