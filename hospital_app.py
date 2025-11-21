import streamlit as st
import mysql.connector #help connect to our database
from mysql.connector import Error
import datetime #used this to set limit for dates

# Database Connection
def create_connection():
    return mysql.connector.connect(
        host="127.0.0.1",   # change if using remote server
        user="root",
        password="pamarhoung",
        database="hospitaldb"
    )

# functions to store form values
def add_patient(first_name, last_name, dob, gender, patient_address, patient_phone, emergency_contact, medical_history):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO Patient (FirstName, LastName, DOB, Gender, Address, Phone, EmergencyContact, MedicalHistory)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
    """, (first_name, last_name, dob, gender, patient_address, patient_phone, emergency_contact, medical_history))
    conn.commit()
    cursor.close()
    conn.close()

def add_staff(fullname, role, specialty, staff_phone, staff_email):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO Staff (Fullname, Role, Specialty, Phone, Email)
        VALUES (%s,%s,%s,%s,%s)
    """, (fullname, role, specialty, staff_phone, staff_email))
    conn.commit()
    cursor.close()
    conn.close()

def add_appointment(patient_id, doctor_id, appointment_date, appointment_time, purpose):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO Appointment (PatientID, DoctorID, AppointmentDate, AppointmentTime, Purpose)
        VALUES (%s,%s,%s,%s,%s)
    """, (patient_id, doctor_id, appointment_date, appointment_time, purpose))
    conn.commit()
    cursor.close()
    conn.close()

def add_medical_record(appointment_id, diagnosis, symptoms, treatment_plan, prescription, doctor_notes):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO MedicalRecord (AppointmentID, Diagnosis, Symptoms, TreatmentPlan, Prescription, DoctorNotes)
        VALUES (%s,%s,%s,%s,%s,%s)
    """, (appointment_id, diagnosis, symptoms, treatment_plan, prescription, doctor_notes))
    conn.commit()
    cursor.close()
    conn.close()

def add_lab_test(patient_id, doctor_id, technician_id,test_type, date_requested, result, result_date):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO LabTest (PatientID, DoctorID, TechnicianID, TestType, DateRequested, Result, ResultDate)
        VALUES (%s,%s,%s,%s,%s,%s,%s)
    """, (patient_id, doctor_id, technician_id,test_type, date_requested, result, result_date))
    conn.commit()
    cursor.close()
    conn.close()

def add_drug(drug_name, dosage, stock_quantity, expiry_date):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO Drug (DrugName, Dosage, StockQuantity, ExpiryDate)
        VALUES (%s,%s,%s,%s)
    """, (drug_name, dosage, stock_quantity, expiry_date))
    conn.commit()
    cursor.close()
    conn.close()

def add_billing(patient_id, services_provided, total_cost, date, payment_method, payment_status):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO Billing (PatientID, ServicesProvided, TotalCost, BillDate, PaymentMethod, PaymentStatus)
        VALUES (%s,%s,%s,%s,%s,%s)
    """, (patient_id, services_provided, total_cost, date, payment_method, payment_status))
    conn.commit()
    cursor.close()
    conn.close()

st.title("Hospital Information System")

menu = ["Patient", "Staff", "Appointment", "Medical Record", "Lab Test", "Pharmacy/Drug", "Billing", "Reports"]
choice = st.sidebar.selectbox("Menu Bar", menu)

# creating each form
if choice == "Patient":
    st.subheader("Add New Patient")
    first_name = st.text_input("First Name")
    last_name = st.text_input("Last Name")
    dob = st.date_input("Date of Birth", min_value=datetime.date(1900,1,1))
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    patient_address = st.text_input("Address")
    patient_phone = st.text_input("Phone")
    emergency_contact = st.text_input("Emergency Contact")
    medical_history = st.text_area("Medical History")
    if st.button("Add Patient"):
        add_patient(first_name, last_name, dob, gender, patient_address, patient_phone, emergency_contact, medical_history)
        st.success("Patient added successfully!")

elif choice == "Staff":
    st.subheader("Add Staff")
    fullname = st.text_input("Full Name")
    role = st.selectbox("Role", ["Doctor", "Nurse", "Admin", "Technician"])
    specialty = st.text_input("Specialty (if Doctor)")
    staff_phone = st.text_input("Phone")
    staff_email = st.text_input("Email")
    if st.button("Add Staff"):
        add_staff(fullname, role, specialty, staff_phone, staff_email)
        st.success("Staff added successfully!")

elif choice == "Appointment":
    st.subheader("Create Appointment")
    patient_id = st.number_input("Patient ID", min_value=1)
    doctor_id = st.number_input("Doctor ID", min_value=1)
    appointment_date = st.date_input("Date")
    appointment_time = st.time_input("Time")
    purpose = st.text_input("Purpose")
    if st.button("Add Appointment"):
        add_appointment(patient_id, doctor_id, appointment_date, appointment_time, purpose)
        st.success("Appointment added successfully!")

elif choice == "Medical Record":
    st.subheader("Add Medical Record")
    appointment_id = st.number_input("Appointment ID", min_value=1)
    diagnosis = st.text_input("Diagnosis")
    symptoms = st.text_area("Symptoms")
    treatment_plan = st.text_area("Treatment Plan")
    prescription = st.text_area("Prescription")
    doctor_notes = st.text_area("Doctor Notes")
    if st.button("Add Medical Record"):
        add_medical_record(appointment_id, diagnosis, symptoms, treatment_plan, prescription, doctor_notes)
        st.success("Medical record added successfully!")

elif choice == "Lab Test":
    st.subheader("Add Lab Test")
    patient_id = st.number_input("Patient ID", min_value=1)
    doctor_id = st.number_input("Doctor ID", min_value=1)
    test_type = st.text_input("Test Type")
    date_requested = st.date_input("Date Requested")
    result = st.text_area("Result")
    result_date = st.date_input("Result Date")
    technician_id = st.number_input("Technician ID", min_value=1)
    if st.button("Add Lab Test"):
        add_lab_test(patient_id, doctor_id, technician_id, test_type, date_requested, result, result_date)
        st.success("Lab test added successfully!")

elif choice == "Pharmacy/Drug":
    st.subheader("Add Drug")
    drug_name = st.text_input("Drug Name")
    dosage = st.text_input("Dosage")
    stock_quantity = st.number_input("Stock Quantity", min_value=0)
    expiry_date = st.date_input("Expiry Date")
    if st.button("Add Drug"):
        add_drug(drug_name, dosage, stock_quantity, expiry_date)
        st.success("Drug added successfully!")

elif choice == "Billing":
    st.subheader("Add Billing Record")
    patient_id = st.number_input("Patient ID", min_value=1)
    services_provided = st.text_area("Services Provided")
    total_cost = st.number_input("Total Cost", min_value=0.0)
    bill_date = st.date_input("Date")
    payment_method = st.selectbox("Payment Method", ["Cash", "Card", "Online"])
    payment_status = st.selectbox("Payment Status", ["Paid", "Pending", "Cancelled"])
    if st.button("Add Billing"):
        add_billing(patient_id, services_provided, total_cost, bill_date, payment_method, payment_status)
        st.success("Billing record added successfully!")


# create reports
elif choice == "Reports":
    st.subheader("Reports")
    report_type = st.selectbox("Select Report", ["Patient Appointments", "Patient Billing", "Lab Tests per Doctor"])

    conn = create_connection()
    cursor = conn.cursor(dictionary=True) #allows each row come as a dictionary rather than tuple

    if report_type == "Patient Appointments":
        if st.button("Show Patient Appointments"):
            cursor.execute("""
                SELECT p.FirstName, p.LastName, a.AppointmentDate, a.AppointmentTime, a.Purpose, s.FullName AS Doctor
                FROM Appointment a
                JOIN Patient p ON a.PatientID = p.PatientID
                JOIN Staff s ON a.DoctorID = s.StaffID
                ORDER BY a.AppointmentDate, a.AppointmentTime;
            """)
        
            data = cursor.fetchall() #retrieve data from sql
            st.dataframe(data) #display table

            """
            Explanation of Query
            -This query retrieves a list of all patient appointments, including the patient’s first and last name, the appointment date and time, the purpose of the appointment, and the doctor assigned.
            -JOIN is used to combine the Appointment table with the Patient table (to get patient names) and the Staff table (to get doctor names).
            -ORDER BY sorts the appointments by date and time, making the report chronologically organized.
            -Purpose: Helps hospital staff view all scheduled appointments in an organized manner
            """

    elif report_type == "Patient Billing":
        if st.button("Show Patient Billing"):
            cursor.execute("""
                SELECT p.FirstName, p.LastName, b.ServicesProvided, b.TotalCost, b.BillDate, b.PaymentStatus
                FROM Billing b
                JOIN Patient p ON b.PatientID = p.PatientID
                ORDER BY b.BillDate DESC;
            """)
            data = cursor.fetchall() #retrieve data from sql
            st.dataframe(data) #display table

            """
            Explanation of query
            -This query lists all billing records for patients, showing the patient’s name, services provided, total cost, the date of the bill, and payment status.
            -JOIN links the Billing table to the Patient table to display patient names.
            -ORDER BY b.BillDate DESC shows most recent bills first.
            -Purpose: Helps staff track payments and generate financial summaries for patients.
            """


    elif report_type == "Lab Tests per Doctor":
        if st.button("Show Lab Tests per Doctor"):
            cursor.execute("""
                SELECT s.FullName AS Doctor, l.TestType, l.DateRequested, l.Result, l.ResultDate
                FROM LabTest l
                JOIN Staff s ON l.DoctorID = s.StaffID
                ORDER BY s.FullName, l.DateRequested;
            """)
            data = cursor.fetchall() #retrieve data from sql
            st.dataframe(data) #display table

            """
            Explanation of Query
            -This query retrieves all lab tests requested by doctors, showing the doctor’s name, the type of test, the date it was requested, the result, and the result date.
            -JOIN connects the LabTest table with the Staff table to display staff names.
            -ORDER BY s.FullName, l.DateRequested sorts the report first by doctor, then by test request date.
            -Purpose: Helps doctors and lab staff monitor tests per doctor and review lab results efficiently.
            """

    cursor.close()
    conn.close()