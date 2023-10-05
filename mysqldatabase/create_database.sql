CREATE Database flask_database;
use flask_database;
CREATE TABLE flask_table (PrimaryID int not null auto_increment, 
                        fname varchar(15) not null, 
                        lname varchar (15) not null, 
                        username varchar (20) not null, 
                        password varchar (30) not null, 
                        favnum int not null, 
                        favelement varchar(15) not null, 
                        email varchar(30) not null, 
                        currentmood varchar(30), 
                        primary key(PrimaryID));