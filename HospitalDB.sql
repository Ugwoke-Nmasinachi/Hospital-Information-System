-- Hospital Information System SQL schema
CREATE DATABASE IF NOT EXISTS HospitalDB;
USE HospitalDB;

-- PATIENT
CREATE TABLE IF NOT EXISTS Patient (
    PatientID INT PRIMARY KEY AUTO_INCREMENT,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    DOB DATE,
    Gender VARCHAR(10),
    Address VARCHAR(150),
    Phone VARCHAR(20),
    EmergencyContact VARCHAR(100),
    MedicalHistory TEXT,
    DateRegistered TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- STAFF (Doctors, Nurses, Technicians, Admin)
CREATE TABLE IF NOT EXISTS Staff (
    StaffID INT PRIMARY KEY AUTO_INCREMENT,
    FullName VARCHAR(100) NOT NULL,
    Role VARCHAR(50) NOT NULL,
    Specialty VARCHAR(100),
    Phone VARCHAR(20),
    Email VARCHAR(100)
);

-- APPOINTMENT
CREATE TABLE IF NOT EXISTS Appointment (
    AppointmentID INT PRIMARY KEY AUTO_INCREMENT,
    PatientID INT NOT NULL,
    DoctorID INT NOT NULL,
    AppointmentDate DATE NOT NULL,
    AppointmentTime TIME NOT NULL,
    Purpose VARCHAR(200),
    Status VARCHAR(50) DEFAULT 'Scheduled'
);

-- MEDICAL RECORD
CREATE TABLE IF NOT EXISTS MedicalRecord (
    RecordID INT PRIMARY KEY AUTO_INCREMENT,
    AppointmentID INT NOT NULL,
    Diagnosis TEXT,
    Symptoms TEXT,
    TreatmentPlan TEXT,
    Prescription TEXT,
    DoctorNotes TEXT,
    RecordDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- LAB TEST
CREATE TABLE IF NOT EXISTS LabTest (
    LabTestID INT PRIMARY KEY AUTO_INCREMENT,
    PatientID INT NOT NULL,
    DoctorID INT NOT NULL,
    TechnicianID INT,
    TestType VARCHAR(100),
    DateRequested DATE,
    Result TEXT,
    ResultDate DATE
);

-- DRUG / PHARMACY
CREATE TABLE IF NOT EXISTS Drug (
    DrugID INT PRIMARY KEY AUTO_INCREMENT,
    DrugName VARCHAR(100) NOT NULL,
    Dosage VARCHAR(100),
    StockQuantity INT DEFAULT 0,
    ExpiryDate DATE
);

-- ROOM
CREATE TABLE IF NOT EXISTS Room (
    RoomID INT PRIMARY KEY AUTO_INCREMENT,
    RoomNumber VARCHAR(20) NOT NULL,
    RoomType VARCHAR(50),
    Status VARCHAR(20) DEFAULT 'Available'
);

-- ADMISSION
CREATE TABLE IF NOT EXISTS Admission (
    AdmissionID INT PRIMARY KEY AUTO_INCREMENT,
    PatientID INT NOT NULL,
    RoomID INT NOT NULL,
    AdmissionDate DATE,
    DischargeDate DATE
);

-- BILLING
CREATE TABLE IF NOT EXISTS Billing (
    BillID INT PRIMARY KEY AUTO_INCREMENT,
    PatientID INT NOT NULL,
    ServicesProvided TEXT,
    TotalCost DECIMAL(12,2),
    BillDate DATE,
    PaymentMethod VARCHAR(50),
    PaymentStatus VARCHAR(50) DEFAULT 'Unpaid'
);

-- FOREIGN KEYS
ALTER TABLE Appointment
    ADD CONSTRAINT fk_Appointment_Patient FOREIGN KEY (PatientID) REFERENCES Patient(PatientID),
    ADD CONSTRAINT fk_Appointment_Doctor FOREIGN KEY (DoctorID) REFERENCES Staff(StaffID);

ALTER TABLE MedicalRecord
    ADD CONSTRAINT fk_MedicalRecord_Appointment FOREIGN KEY (AppointmentID) REFERENCES Appointment(AppointmentID);

ALTER TABLE LabTest
    ADD CONSTRAINT fk_LabTest_Patient FOREIGN KEY (PatientID) REFERENCES Patient(PatientID),
    ADD CONSTRAINT fk_LabTest_Doctor FOREIGN KEY (DoctorID) REFERENCES Staff(StaffID),
    ADD CONSTRAINT fk_LabTest_Technician FOREIGN KEY (TechnicianID) REFERENCES Staff(StaffID);

ALTER TABLE Admission
    ADD CONSTRAINT fk_Admission_Patient FOREIGN KEY (PatientID) REFERENCES Patient(PatientID),
    ADD CONSTRAINT fk_Admission_Room FOREIGN KEY (RoomID) REFERENCES Room(RoomID);

ALTER TABLE Billing
    ADD CONSTRAINT fk_Billing_Patient FOREIGN KEY (PatientID) REFERENCES Patient(PatientID);

-- Sample staff and patients
INSERT INTO Staff (FullName, Role, Specialty, Phone, Email) VALUES
('Dr. Adewale Bamidele', 'Doctor', 'Cardiology', '07010000001', 'adewale@example.com'),
('Dr. Helen Obasi', 'Doctor', 'General Practice', '07010000002', 'helen@example.com'),
('Michael Ojo', 'Technician', NULL, '07010000003', 'michael@example.com'),
('Sarah Ahmed', 'Nurse', NULL, '07010000004', 'sarah@example.com');

INSERT INTO Patient (FirstName, LastName, DOB, Gender, Address, Phone, EmergencyContact) VALUES
('John', 'Doe', '1990-05-10', 'Male', '12 Allen Avenue, Lagos', '07012345678', 'Jane Doe - 08098765432'),
('Mary', 'Johnson', '1996-11-02', 'Female', '5 Ikeja GRA, Lagos', '08123456789', 'Peter Johnson - 08122334455');

INSERT INTO Room (RoomNumber, RoomType, Status) VALUES
('101', 'General', 'Available'),
('102', 'ICU', 'Available');
