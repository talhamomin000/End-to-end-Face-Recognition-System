# dashboard.py
import streamlit as st
import pandas as pd
import plotly.express as px

def run_dashboard():
    st.title('Interactive Attendance Dashboard')

    # Load attendance and student details data
    attendance_df = pd.read_csv('attendance_of_students.csv')
    student_details_df = pd.read_csv('Students_details.csv')

    # Sidebar filters
    st.sidebar.title('Filters')
    selected_branch = st.sidebar.selectbox('Select Branch', ['All'] + student_details_df['Branch'].unique().tolist())
    selected_year = st.sidebar.selectbox('Select Year', ['All', '1st Year', '2nd Year', '3rd Year', '4th Year'])
    selected_date = st.sidebar.date_input('Select Date')

    # Apply filters to attendance data
    filtered_attendance_df = attendance_df.copy()
    if selected_branch != 'All':
        filtered_attendance_df = filtered_attendance_df[filtered_attendance_df['RollNumber'].isin(student_details_df[student_details_df['Branch'] == selected_branch]['RollNumber'])]
    if selected_year != 'All':
        filtered_attendance_df = filtered_attendance_df[filtered_attendance_df['RollNumber'].isin(student_details_df[student_details_df['Year'] == selected_year]['RollNumber'])]
    if selected_date:
        selected_date_str = selected_date.strftime('%Y-%m-%d')
        filtered_attendance_df = filtered_attendance_df[filtered_attendance_df['Date'] == selected_date_str]

    # KPIs
    total_students = len(student_details_df)
    total_attendance_count = len(filtered_attendance_df)
    present_percentage = (total_attendance_count / total_students) * 100

    st.write('## Key Performance Indicators (KPIs)')
    st.write(f'Total Students: {total_students}')
    st.write(f'Total Attendance Count: {total_attendance_count}')
    st.write(f'Present Percentage: {present_percentage:.2f}%')

    # Visualizations
    st.write('## Visualizations')

    # Bar chart for attendance by subject
    subject_counts = filtered_attendance_df['Subject'].value_counts().reset_index()
    subject_counts.columns = ['Subject', 'Attendance Count']
    bar_fig = px.bar(subject_counts, x='Subject', y='Attendance Count', title='Attendance by Subject')
    st.plotly_chart(bar_fig, use_container_width=True)

    # Line chart for attendance over date
    attendance_by_date = filtered_attendance_df.groupby('Date').size().reset_index()
    attendance_by_date.columns = ['Date', 'Attendance Count']
    line_fig = px.line(attendance_by_date, x='Date', y='Attendance Count', title='Attendance over Date')
    st.plotly_chart(line_fig, use_container_width=True)

if __name__ == "__main__":
    run_dashboard()
