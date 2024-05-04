# import streamlit as st

# def run_report():
#     st.title('Report')
#     st.write('Please select the date, subject, and branch, then click the "View Attendance" button:')

#     # Select date
#     selected_date = st.date_input("Select Date", value=None)

#     # Select subject
#     selected_subject = st.selectbox("Select Subject", ["Math", "Science", "English", "History", "Other"])

#     # Select branch
#     selected_branch = st.selectbox("Select Branch", ["Computer Science", "Electrical", "Mechanical", "Civil", "Other"])

#     # View Attendance button
#     if st.button("View Attendance"):
#         st.write(f"Attendance for {selected_subject} on {selected_date} in {selected_branch} branch:")

# if __name__ == "__main__":
#     run_report()


import streamlit as st
import pandas as pd

def run_report():
    st.title('Attendance Report')
    st.write('Please select the date and subject, then click the "View Attendance" button:')

    # Load student details and attendance data
    student_details_df = pd.read_csv('Students_details.csv')
    attendance_df = pd.read_csv('attendance_of_students.csv')

    # Filter unique dates and subjects from attendance data
    unique_dates = sorted(attendance_df['Date'].unique())
    unique_subjects = sorted(attendance_df['Subject'].unique())

    # Select date and subject
    selected_date = st.selectbox("Date", unique_dates)
    selected_subject = st.selectbox("Subject", unique_subjects)

    # View Attendance button
    if st.button("View Attendance"):
        st.write(f"Attendance for {selected_subject} on {selected_date}:")

        # Filter attendance data based on selected options
        filtered_attendance = attendance_df[(attendance_df['Date'] == selected_date) &
                                             (attendance_df['Subject'] == selected_subject)]

        # Merge attendance data with student details based on roll number
        merged_data = pd.merge(filtered_attendance, student_details_df, on='RollNumber')

        # Select and display relevant columns
        attendance_report = merged_data[['FirstName', 'LastName', 'RollNumber', 'Branch', 'Year', 'Date', 'Subject']]

        # Display the report
        st.write(attendance_report)

if __name__ == "__main__":
    run_report()
