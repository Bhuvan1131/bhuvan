import streamlit as st
import pandas as pd
from openpyxl import load_workbook
import os

excel_file = "HRFormData.xlsx"
sheet_name = "Sheet1"  # or change based on your sheet

st.title("HR Entry Form")

# Form UI
with st.form("hr_form"):
    first_name = st.text_input("First Name")
    last_name = st.text_input("Last Name")
    dob = st.date_input("Date of Birth")
    email = st.text_input("Email")
    phone = st.text_input("Phone Number")
    department = st.text_input("Department")
    joining_date = st.date_input("Joining Date")

    submit = st.form_submit_button("Submit")

if submit:
    new_data = {
        "First Name": first_name,
        "Last Name": last_name,
        "DOB": dob.strftime("%Y-%m-%d"),
        "Email": email,
        "Phone Number": phone,
        "Department": department,
        "Joining Date": joining_date.strftime("%Y-%m-%d"),
    }

    if os.path.exists(excel_file):
        df = pd.read_excel(excel_file)
        df = df.append(new_data, ignore_index=True)
    else:
        df = pd.DataFrame([new_data])

    df.to_excel(excel_file, index=False)
    st.success("Form submitted and saved to Excel!")
