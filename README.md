# End-to-end-Face-Recognition-System
This project leverages facial recognition technology to automate student attendance tracking, reducing manual effort and increasing accuracy. Built with Streamlit, the system includes user-friendly interfaces for registration, real-time attendance monitoring, and dynamic data visualization dashboards to provide insightful attendance analytics.

# Features
- Face Detection and Recognition
- Multi-face recognition
- Automated attendance tracking
- User-friendly interface
- Subject-based attendance option
- Instant report generated
- Dynamic Data Visualization

# Requirements
- Python 3.7 or Python 3.6
- Streamlit
- Open CV
- Face-recognition library
- Pandas
- Numpy

  # Description
  - `app.py:-` The app.py file serves as the main entry point for the application, managing the navigation and integration of all the pages within the Streamlit-based attendance management system.
  - `registration.py:-` The registration.py file handles the student registration process, capturing and storing their details and facial images.
  - `Images Folder:-` The Images folder stores the facial images of registered students used for attendance tracking.
  - `Students_details.csv:-` The Students_details.csv file stores detailed information about each registered student, including their name, roll number, branch, year, and other personal details.
  - `attendance.py:-` The attendance.py file manages the process of taking attendance using facial recognition, matches detected faces with registered students, and records attendance data along with the selected subject in the attendance CSV file.
  - `report.py:-` The report.py file generates a report by providing options to select the date, subject, and branch. It then retrieves attendance records based on the selected criteria from the attendance CSV file and displays them also we can download and save the attendance records.
  - `dashboard.py:-` The dashboard.py file creates an interactive dashboard using Streamlit and Plotly libraries. It allows users to filter attendance records by branch and year, select a date using a calendar, and view attendance statistics through KPI cards, bar charts for subjects, and a line chart for attendance over time.
 
# Demo
1. Home Page
![WhatsApp Image 2024-05-02 at 10 06 46_bd6f0322](https://github.com/talhamomin000/End-to-end-Face-Recognition-System/assets/121718008/34dd9a40-2670-4a81-880e-21c194540c87)
2. Registration Page
![WhatsApp Image 2024-05-02 at 10 07 00_76a92b79](https://github.com/talhamomin000/End-to-end-Face-Recognition-System/assets/121718008/fe829744-da43-49ac-8aa9-c8afef1fe10e)
3. Attendance Page
![WhatsApp Image 2024-05-02 at 10 07 25_c350d755](https://github.com/talhamomin000/End-to-end-Face-Recognition-System/assets/121718008/1ef71068-0bff-4ef9-8243-622a65329b7f)
![WhatsApp Image 2024-05-02 at 10 08 22_5a18f300](https://github.com/talhamomin000/End-to-end-Face-Recognition-System/assets/121718008/e771fa5b-73dd-4b73-a09f-5b34bea1405f)
4. View Attendace Record Page
![WhatsApp Image 2024-05-02 at 10 09 20_f6eb4672](https://github.com/talhamomin000/End-to-end-Face-Recognition-System/assets/121718008/c7731c9c-96cd-4da8-ae29-1483e7f938e6)
5. Dashboard Page
![WhatsApp Image 2024-05-02 at 10 10 53_893df2c1](https://github.com/talhamomin000/End-to-end-Face-Recognition-System/assets/121718008/0ee5377f-f7ba-4a3b-8339-e90b7c02031f)
<br>

## Important Note- If facing any issue while installing `face-recognition`, `dlib` and `cmake` then follow steps that are mentioned below.
1. Go to this github link:-  https://github.com/coding-with-Ash/10-video_app
2. Then download the `face_recog_dlib_file-master` folder.
3. Ater downloading that, copy the entire `face_recog_dlib_file-master` folder and paste it in your project file.
4. Finally, you can install all these libraries `face-recognition`, `dlib` and `cmake`.

## Contact:- If you have any questions, feel free to contact me via email: talhamomin000@gmail.com
