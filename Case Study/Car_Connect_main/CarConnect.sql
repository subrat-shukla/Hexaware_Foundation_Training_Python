use casestudy_db;
-- Customer Table
CREATE TABLE Customer (
    -- Auto-incrementing unique ID for each customer
    FirstName NVARCHAR(50) NOT NULL,
    LastName NVARCHAR(50) NOT NULL,
    Email NVARCHAR(100) NOT NULL UNIQUE,
    PhoneNumber NVARCHAR(15) NOT NULL,
    Address NVARCHAR(255) NOT NULL,
    Username NVARCHAR(50) NOT NULL UNIQUE,  -- Unique username for login
    Password NVARCHAR(255) NOT NULL,  -- Securely hashed password
    RegistrationDate DATETIME NOT NULL DEFAULT GETDATE()  -- Default to the current date and time
);
ALTER TABLE Customer
ADD CustomerID INT PRIMARY KEY IDENTITY(1,1);
EXEC sp_help 'Customer';

select * from Customer;
-- Vehicle Table
CREATE TABLE Vehicle (
    VehicleID INT PRIMARY KEY IDENTITY(1,1),  -- Auto-incrementing unique ID for each vehicle
    Model NVARCHAR(50) NOT NULL,
    Make NVARCHAR(50) NOT NULL,
    Year INT NOT NULL,
    Color NVARCHAR(20),
    RegistrationNumber NVARCHAR(20) NOT NULL UNIQUE,  -- Unique registration number
    Availability BIT NOT NULL DEFAULT 1,  -- 1 = Available, 0 = Not Available
    DailyRate DECIMAL(10, 2) NOT NULL  -- Daily rental rate with two decimal places
);

select * from Vehicle;

-- Reservation Table
CREATE TABLE Reservation (
    ReservationID INT PRIMARY KEY IDENTITY(1,1),  -- Auto-incrementing unique ID for each reservation
    CustomerID INT NOT NULL,
    VehicleID INT NOT NULL,
    StartDate DATETIME NOT NULL,
    EndDate DATETIME NOT NULL,
    TotalCost DECIMAL(10, 2) NOT NULL,  -- Total cost with two decimal places
    Status NVARCHAR(20) NOT NULL,  -- e.g., pending, confirmed, completed
    CONSTRAINT FK_Reservation_Customer FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID),
    CONSTRAINT FK_Reservation_Vehicle FOREIGN KEY (VehicleID) REFERENCES Vehicle(VehicleID)
);

select * from Reservation;

-- Admin Table
CREATE TABLE Admin (
    AdminID INT PRIMARY KEY IDENTITY(1,1),  -- Auto-incrementing unique ID for each admin
    FirstName NVARCHAR(50) NOT NULL,
    LastName NVARCHAR(50) NOT NULL,
    Email NVARCHAR(100) NOT NULL UNIQUE,
    PhoneNumber NVARCHAR(15) NOT NULL,
    Username NVARCHAR(50) NOT NULL UNIQUE,  -- Unique username for login
    Password NVARCHAR(255) NOT NULL,  -- Securely hashed password
    Role NVARCHAR(50) NOT NULL,  -- Role within the system (e.g., super admin, fleet manager)
    JoinDate DATETIME NOT NULL DEFAULT GETDATE()  -- Default to the current date and time
);

select * from Admin;

-- Adding Indexes for Performance on Username and Email fields
CREATE INDEX IDX_Customer_Username ON Customer(Username);
CREATE INDEX IDX_Customer_Email ON Customer(Email);
CREATE INDEX IDX_Admin_Username ON Admin(Username);
CREATE INDEX IDX_Admin_Email ON Admin(Email);
