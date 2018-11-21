create database referencias;
use referencias;

-- fast
-- harris
-- orb
-- shiTomasi
-- star
-- surf

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

CREATE TABLE medias_desvios (
Nome varchar(30) not null,
MediaMatches float(30) not null,
DesvioMatches float(30) not null,
MediaCorretos float(30) not null,
DesvioCorretos float(30) not null,
Porcentagem float(30) not null,
primary key(Nome)
);

select *from fast_brisk;

