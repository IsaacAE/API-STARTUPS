create database CIID;
use CIID;

create user 'becario'@'localhost' identified by 'BecarioCIID24';

grant all privileges on CIID.* to 'becario'@'localhost'
with grant option;

DROP TABLE if exists Startups;
CREATE TABLE Startups(
	idStartup int auto_increment,
    nombre varchar(50) not null,
    fechaFundacion Date not null,
    ubicacion varchar (50) not null,
    categoria varchar (50) not null,
    inversionRecibida float not null,
    primary key (idStartup)
);


DROP TABLE if exists Technologies;
CREATE TABLE Technologies(
	idTechnologie int auto_increment,
    nombre varchar(50) not null,
    sector varchar(30) not null,
    descripcion varchar (150) not null,
    estadoAdopcion varchar (50) not null,
    primary key (idTechnologie)
);