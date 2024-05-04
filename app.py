# app.py
import streamlit as st
from home import run_home
from registeration import run_registration
from attendance import run_attendance
from report import run_report
from dashboard import run_dashboard

PAGES = {
    "Home": run_home,
    "Registration": run_registration,
    "Attendance": run_attendance,
    "Report": run_report,
    "Dashboard": run_dashboard
}

def main():
    st.sidebar.title('Navigation')
    selection = st.sidebar.radio("Go to", list(PAGES.keys()))

    page = PAGES[selection]
    page()

if __name__ == "__main__":
    main()
