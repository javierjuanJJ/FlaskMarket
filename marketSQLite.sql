create table main.user
(
    id            INTEGER     not null
        primary key,
    username      VARCHAR(30) not null
        unique,
    email_address VARCHAR(50) not null
        unique,
    password_hash VARCHAR(60) not null,
    budget        INTEGER     not null
);

create table main.item
(
    id          INTEGER       not null
        primary key,
    name        VARCHAR(30)   not null
        unique,
    price       INTEGER       not null,
    barcode     VARCHAR(12)   not null
        unique,
    description VARCHAR(1024) not null
        unique,
    owner       INTEGER
        references main.user
);


