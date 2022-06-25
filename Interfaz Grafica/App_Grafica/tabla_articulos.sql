CREATE DATABASE `articulosDB`

CREATE TABLE articulosDB.articulos (
	codigo bigint auto_increment NOT NULL,
	descripcion varchar(255) NULL,
	precio decimal(10,2) null,
	PRIMARY KEY (`codigo`)
)