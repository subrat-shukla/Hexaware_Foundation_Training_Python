create database HospitalManagementSystem;
use HospitalManagementSystem;

create table Patient(
	patientId INT Primary Key,
	firstName varchar(255),
	lastName varchar(255),
	dateOfBirth Date,
	gender varchar(255),
	contactNumber varchar(15),
	address TEXT
);


create table Doctor(
	doctorId INT primary key,
	firstName varchar(255),
	lastName varchar(255),
	specialization varchar(255),
	contactNumber varchar(15)
);


create table Appointment(
	appointmentID INT Primary key,
	patientId Int,
	doctorId Int,
	appointmentDate Date,
	description TEXT,
	Foreign Key(patientId) References Patient (patientId),
	Foreign Key(doctorId) References Doctor (doctorId)
);


-----------------------inserting values------------------
insert into Doctor(doctorId, firstName, lastName, specialization, 
contactNumber) Values
(1, 'Subrat', 'Shukla', 'Neuro Sugeon', '9928211389'),
(2, 'Deepa', 'Shankar', 'Orthopedic Surgeon', '8765432109'),
(3, 'Rajesh', 'Mohan', 'Neurologist', '6543210987'),
(4, 'Priya', 'Raj', 'Gynecologist', '7654321098'),
(5, 'Anitha', 'Kumar', 'Pediatrician', '5432109876'),
(6, 'Senthil', 'Devi', 'Dermatologist', '4321098765'),
(7, 'Vijay', 'Lakshmi', 'ENT Specialist', '3210987654'),
(8, 'Malathi', 'Venkatesh', 'Ophthalmologist', '2109876543'),
(9, 'Ganesh', 'Priya', 'Urologist', '1098765432'),
(10, 'Suresh', 'Meena', 'Radiologist', '9876543210');

select *from Doctor;


insert into Patient(patientId, firstName, lastName, dateOfBirth, gender, 
contactNumber, address) Values
(1, 'Shubh', 'Shukla', '2002-10-17', 'Male', '9928211389', 'Jaipur'),
(2, 'Priya', 'Kumar', '1985-08-22', 'Female', '8765432109', 'Jodhpur'),
(3, 'Mohan', 'Sharma', '1992-03-10', 'Male', '7654321098', 'Surat'),
(4, 'Lakshmi', 'Ganesh', '1988-11-28', 'Female', '6543210987', 'Salem'),
(5, 'Kartik', 'Anand', '1996-06-18', 'Male', '5432109876', 'Delhi'),
(6, 'Deepa', 'Rajesh', '1980-09-05', 'Female', '4321098765', 'Vellore'),
(7, 'Raj', 'Malathi', '1998-01-30', 'Male', '3210987654', 'Chennai'),
(8, 'Saranya', 'Suresh', '1983-07-12', 'Female', '2109876543', 'Kochi'),
(9, 'Prakash', 'Meena', '1993-04-25', 'Male', '1098765432', 'Erode'),
(10, 'Aishwarya', 'Venkatesh', '1987-12-08', 'Female', '9876543210', 'Pune');

select *from Patient;

select *from Appointment;

INSERT INTO Appointment(appointmentID, patientId, doctorId, appointmentDate, description)
VALUES (1, 1, 1, '2024-10-17', 'null');