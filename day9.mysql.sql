use techbros;
alter table PWDS drop column location;
describe PWDS;  
alter table PWDS change YOS YOE varchar(50) not null;
describe PWDS;
ALTER TABLE pwds RENAME TO python_with_data_science;
describe python_with_data_science;
drop table python_with_data_science;


create table PWDS(ID int not null,SName varchar(255) not null, Age int not null, Gender varchar(10) not null, SLevel varchar(25) not null, Phonenumber varchar(45) not null, YOS varchar(45) not null);

alter table PWDS change YOS YOE varchar(50) not null;
describe PWDS;

select * from PWDS;









create index Gender on PWDS(Geder);