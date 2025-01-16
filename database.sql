-- Administrator Login Cerenditals:
-- Email->administrator@gmail.com
-- Password->admin
create table signup(
    sn int not null auto_increment,
    name varchar(200) not null,
    email varchar(500),
    user_type varchar(200),
    class varchar(200),
    Roll varchar(200),
    faculty varchar(200),
    phone varchar(15),
    sec_q varchar(500),
    ans varchar(500),
    pass varchar(200),
    primary key (sn)
);
insert into signup(name,email,user_type,phone,pass) values('Administrator','administrator@gmail.com','Administrator','0','admin');
create table attendence(
    sn int not null auto_increment,
    user_type varchar(200),
    email varchar(200),
    da date,
    dat datetime,
    stat varchar(200),
    primary key (sn)
);
create table profile(
    sn int not null auto_increment,
    name varchar(200) not null,
    email varchar(500),
    cont varchar(300),
    dob date,
    gender varchar(200),
    stat varchar(500),
    dist varchar(500),
    pin varchar(200),
    loaction varchar(5000),
    about varchar(4500),
    primary key(sn)
);
create table leave_details(
    sn int not null auto_increment,
    user_type varchar(200),
    email varchar(200),
    leave_type varchar(500),
    from_date date,
    to_date date,
    reason varchar(500),
    stat varchar(200),
    primary key (sn)
);