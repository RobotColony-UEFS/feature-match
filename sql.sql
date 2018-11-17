create database referencias;
use referencias; 

CREATE TABLE surf_brief(
Nome varchar(30) not null,
Matches int(10) not null,
Correto int(10) not null,
ImgReferente varchar(30) not null,
rastreio boolean,
primary key (Nome)
);

CREATE TABLE surf_brisk(
Nome varchar(30) not null,
Matches int(10) not null,
Correto int(10) not null,
ImgReferente varchar(30) not null,
rastreio boolean,
primary key (Nome)
);

CREATE TABLE surf_freak(
Nome varchar(30) not null,
Matches int(10) not null,
Correto int(10) not null,
ImgReferente varchar(30) not null,
rastreio boolean,
primary key (Nome)
);

CREATE TABLE surf_orb(
Nome varchar(30) not null,
Matches int(10) not null,
Correto int(10) not null,
ImgReferente varchar(30) not null,
rastreio boolean,
primary key (Nome)
);

CREATE TABLE surf_sift(
Nome varchar(30) not null,
Matches int(10) not null,
Correto int(10) not null,
ImgReferente varchar(30) not null,
rastreio boolean,
primary key (Nome)
);

select *from fast_brisk;
truncate fast_brief;
