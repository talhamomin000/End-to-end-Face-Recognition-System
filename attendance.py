# attendance.py
# import pandas as pd
# import streamlit as st
# import cv2
# import face_recognition
# import os
# from datetime import datetime

# # Function to load known faces from images in the 'Images' folder
# def load_known_faces():
#     known_faces = []
#     images_folder = 'Images'
#     valid_extensions = ['.png', '.jpg', '.jpeg']
#     for filename in os.listdir(images_folder):
#         if any(filename.lower().endswith(ext) for ext in valid_extensions):
#             image_path = os.path.join(images_folder, filename)
#             image = face_recognition.load_image_file(image_path)
#             face_encoding = face_recognition.face_encodings(image)[0]
#             known_faces.append({"name": filename.split('_')[0], "face_encoding": face_encoding})
#     return known_faces

# def run_attendance():
#     st.title('Attendance Tracking')
#     st.write('Please select the subject, date, and click the "Take Attendance" button:')

#     # Input fields
#     subject = st.selectbox("Subject", ["Math", "Science", "English", "History", "Other"])
#     selected_date = st.date_input("Date", value=datetime.now())

#     # Take Attendance button
#     if st.button("Take Attendance"):
#         st.write(f"Taking attendance for {subject} on {selected_date}.")

#         # Take attendance
#         take_attendance(subject, selected_date)

# def take_attendance(subject, date):
#     # Load known faces
#     known_faces = load_known_faces()

#     # Initialize webcam
#     cap = cv2.VideoCapture(0)
#     attendance = {student["name"]: 0 for student in known_faces}
#     detected_student = None  # To store the name of the detected student

#     while cap.isOpened():
#         ret, frame = cap.read()
#         if not ret:
#             break

#         # Convert frame to RGB
#         rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
#         # Find faces in the frame
#         face_locations = face_recognition.face_locations(rgb_frame)
#         face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
        
#         # Iterate over faces found in the frame
#         for face_location, face_encoding in zip(face_locations, face_encodings):
#             top, right, bottom, left = face_location
#             # Compare face encoding with known faces
#             for known_face in known_faces:
#                 matches = face_recognition.compare_faces([known_face['face_encoding']], face_encoding)
#                 if True in matches:
#                     name = known_face['name']
#                     attendance[name] += 1
#                     # Draw rectangle around the face and display name
#                     cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
#                     cv2.putText(frame, name, (left + 6, bottom - 6), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
#                     detected_student = name  # Store the name of the detected student

#         # Display the webcam feed
#         cv2.imshow('Webcam Feed', frame)

#         # Press '0' to save attendance of the detected student
#         if cv2.waitKey(1) & 0xFF == ord('0'):
#             if detected_student:
#                 save_attendance({detected_student: attendance[detected_student]}, subject, date)
#                 break
    
#     # Release resources
#     cap.release()
#     cv2.destroyAllWindows()

# def save_attendance(attendance, subject, date):
#     df = pd.DataFrame(list(attendance.items()), columns=['Name', 'Attendance'])
#     df['Subject'] = subject
#     df['Date'] = date
#     if os.path.exists('attendance.csv'):
#         existing_df = pd.read_csv('attendance.csv')
#         df = pd.concat([existing_df, df], ignore_index=True)
#     df.to_csv('attendance.csv', index=False)
#     st.write("Attendance saved successfully!")

# if __name__ == "__main__":
#     run_attendance()


# import streamlit as st
# import cv2
# from multiprocessing import Process
# import face_recognition
# import os
# import pandas as pd
# import numpy as np
# from datetime import datetime, timedelta

# def load_known_faces():
#     known_faces = []
#     images_folder = 'Images'
#     valid_extensions = ['.png', '.jpg', '.jpeg']
#     for filename in os.listdir(images_folder):
#         if any(filename.lower().endswith(ext) for ext in valid_extensions):
#             image_path = os.path.join(images_folder, filename)
#             image = face_recognition.load_image_file(image_path)
#             face_encoding = face_recognition.face_encodings(image)[0]
#             known_faces.append({"name": filename.split('_')[0], "face_encoding": face_encoding})
#     return known_faces

# def run_attendance():
#     st.title('Attendance Tracking')
#     st.write('Please select the subject, date, and click the "Take Attendance" button:')
#     subject = st.selectbox("Subject", ["Math", "Science", "English", "History", "Other"])
#     selected_date = st.date_input("Date", value=pd.Timestamp.now().date())
#     if st.button("Take Attendance"):
#         st.write(f"Taking attendance for {subject} on {selected_date}...")
#         attendance = take_attendance()
#         save_attendance(attendance, selected_date, subject)

# def take_attendance():
#     known_faces = load_known_faces()
#     attendance = {student["name"]: 0 for student in known_faces}
#     cap = cv2.VideoCapture(0)
#     start_time = datetime.now()
#     while (datetime.now() - start_time).total_seconds() < 300:  # 5 minutes
#         ret, frame = cap.read()
#         if not ret:
#             break
#         rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#         face_locations = face_recognition.face_locations(rgb_frame)
#         face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
#         for face_encoding in face_encodings:
#             for known_face in known_faces:
#                 matches = face_recognition.compare_faces([known_face['face_encoding']], face_encoding)
#                 if True in matches:
#                     name = known_face['name']
#                     attendance[name] += 1
#         cv2.imshow('Webcam Feed', frame)
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
#     cap.release()
#     cv2.destroyAllWindows()
#     return attendance

# def save_attendance(attendance, date, subject):
#     df = pd.DataFrame(list(attendance.items()), columns=['Name', 'Attendance'])
#     df['Date'] = date
#     df['Subject'] = subject
#     if os.path.exists('attendance.csv'):
#         existing_df = pd.read_csv('attendance.csv')
#         df = pd.concat([existing_df, df], ignore_index=True)
#     df.to_csv('attendance.csv', index=False)

# if __name__ == "__main__":
#     run_attendance()

# import streamlit as st
# import cv2
# import face_recognition
# import os
# import pandas as pd
# from datetime import datetime

# def load_known_faces():
#     known_faces = []
#     images_folder = 'Images'
#     valid_extensions = ['.png', '.jpg', '.jpeg']
#     for filename in os.listdir(images_folder):
#         if any(filename.lower().endswith(ext) for ext in valid_extensions):
#             image_path = os.path.join(images_folder, filename)
#             image = face_recognition.load_image_file(image_path)
#             face_encoding = face_recognition.face_encodings(image)[0]
#             known_faces.append({"name": filename.split('_')[0], "roll_number": filename.split('_')[1], "face_encoding": face_encoding})
#     return known_faces

# def run_attendance():
#     st.title('Attendance Tracking')
#     st.write('Please select the subject, date, and click the "Take Attendance" button:')

#     subject = st.selectbox("Subject", ["Math", "Science", "English", "History", "Other"])
#     selected_date = st.date_input("Date", value=datetime.now())

#     if st.button("Take Attendance"):
#         st.write(f"Taking attendance for {subject} on {selected_date}.")

#         known_faces = load_known_faces()
#         cap = cv2.VideoCapture(0)

#         attendance = []

#         while cap.isOpened():
#             ret, frame = cap.read()
#             if not ret:
#                 break

#             rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

#             face_locations = face_recognition.face_locations(rgb_frame)
#             face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

#             for face_location, face_encoding in zip(face_locations, face_encodings):
#                 top, right, bottom, left = face_location
#                 for known_face in known_faces:
#                     matches = face_recognition.compare_faces([known_face['face_encoding']], face_encoding)
#                     if True in matches:
#                         name = known_face['name'].split()[0]
#                         roll_number = known_face['roll_number']
#                         # Check if this student's attendance has already been recorded for the selected subject on the given date
#                         if not any(a["FirstName"] == name and a["Subject"] == subject and a["Date"] == selected_date.strftime("%Y-%m-%d") for a in attendance):
#                             attendance.append({"FirstName": name, "RollNumber": roll_number, "Subject": subject, "Date": selected_date.strftime("%Y-%m-%d")})
#                             cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
#                             cv2.putText(frame, f"{name} ({roll_number})", (left + 6, bottom - 6), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

#             cv2.imshow('Webcam Feed', frame)

#             if cv2.waitKey(1) & 0xFF == ord('0'):
#                 save_attendance(attendance)
#                 st.write("Attendance recorded for the detected students.")
#                 break

#             if cv2.waitKey(1) & 0xFF == ord('q'):
#                 break

#         cap.release()
#         cv2.destroyAllWindows()



# def save_attendance(attendance, subject, date):
#     df = pd.DataFrame({'Name': attendance.keys(), 'Roll Number': attendance.values()[:, 0], 'Subject': subject, 'Date': date})
#     if os.path.exists('attendance.csv'):
#         existing_df = pd.read_csv('attendance.csv')
#         df = pd.concat([existing_df, df], ignore_index=True)
#     df.to_csv('attendance.csv', index=False)
#     st.write("Attendance saved successfully!")

# if __name__ == "__main__":
#     run_attendance()


# import streamlit as st
# import cv2
# import face_recognition
# import os
# import pandas as pd
# from datetime import datetime

# def load_known_faces():
#     known_faces = {}
#     images_folder = 'Images'
#     valid_extensions = ['.png', '.jpg', '.jpeg']
#     for filename in os.listdir(images_folder):
#         if any(filename.lower().endswith(ext) for ext in valid_extensions):
#             roll_number = filename.split('.')[0]  # Extracting roll number from the file name
#             image_path = os.path.join(images_folder, filename)
#             image = face_recognition.load_image_file(image_path)
#             face_encoding = face_recognition.face_encodings(image)[0]
#             known_faces[roll_number] = face_encoding
#     return known_faces

# def run_attendance():
#     st.title('Attendance Tracking')
#     st.write('Please select the subject, date, and click the "Take Attendance" button:')

#     subject = st.selectbox("Subject", ["Math", "Science", "English", "History", "Other"])
#     selected_date = st.date_input("Date", value=datetime.now())

#     if st.button("Take Attendance"):
#         st.write(f"Taking attendance for {subject} on {selected_date}.")

#         known_faces = load_known_faces()
#         cap = cv2.VideoCapture(0)

#         attendance = {}

#         while cap.isOpened():
#             ret, frame = cap.read()
#             if not ret:
#                 break

#             rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

#             face_locations = face_recognition.face_locations(rgb_frame)
#             face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

#             for face_location, face_encoding in zip(face_locations, face_encodings):
#                 for roll_number, known_encoding in known_faces.items():
#                     matches = face_recognition.compare_faces([known_encoding], face_encoding)
#                     if True in matches:
#                         if roll_number not in attendance:
#                             attendance[roll_number] = []
#                         attendance[roll_number].append({"Subject": subject, "Date": selected_date.strftime("%Y-%m-%d")})

#             if cv2.waitKey(1) & 0xFF == ord('0'):
#                 save_attendance(attendance)
#                 st.write("Attendance recorded for the detected students.")
#                 break

#             if cv2.waitKey(1) & 0xFF == ord('q'):
#                 break

#         cap.release()
#         cv2.destroyAllWindows()

# def save_attendance(attendance):
#     if os.path.exists('attendance.csv'):
#         df = pd.read_csv('attendance.csv')
#     else:
#         df = pd.DataFrame(columns=['RollNumber', 'Subject', 'Date'])

#     for roll_number, entries in attendance.items():
#         for entry in entries:
#             df = df.append({"RollNumber": roll_number, "Subject": entry["Subject"], "Date": entry["Date"]}, ignore_index=True)

#     df.to_csv('attendance.csv', index=False)
#     st.write("Attendance saved successfully!")

# if __name__ == "__main__":
#     run_attendance()


# Final Code

import streamlit as st
import cv2
import face_recognition
import os
import csv
from datetime import datetime

def load_images_from_folder(folder):
    images = []
    roll_numbers = []
    for filename in os.listdir(folder):
        if filename.endswith(".png"):
            img = face_recognition.load_image_file(os.path.join(folder, filename))
            roll_number = os.path.splitext(filename)[0]
            images.append(img)
            roll_numbers.append(roll_number)
    return images, roll_numbers

def update_attendance_csv(name, subject):
    csv_file = "attendance_of_students.csv"
    now = datetime.now()
    date = now.strftime("%Y-%m-%d")
    time = now.strftime("%H:%M:%S")
    if not os.path.exists(csv_file):
        with open(csv_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Time", "RollNumber", "Subject"])
            writer.writerow([date, time, name, subject])
    else:
        with open(csv_file, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([date, time, name, subject])

def run_attendance():
    st.title('Attendance System')
    st.write('Select Subject and click on "Take Attendance" to mark attendance.')

    # Select subject
    subject = st.selectbox("Select Subject", ["Math", "Science", "English", "History", "Other"])

    # Take Attendance button
    if st.button("Take Attendance"):
        st.write("Taking attendance for", subject)

        images_folder = 'Images'
        known_encodings = []
        roll_numbers = []

        # Load images and their respective roll numbers
        images, roll_numbers = load_images_from_folder(images_folder)

        # Generate face encodings for each image
        known_encodings = [face_recognition.face_encodings(img)[0] for img in images]

        # Keep track of students for whom attendance is recorded
        attendance_recorded = []

        # Open a video capture stream
        video_capture = cv2.VideoCapture(0)

        while True:
            # Capture each frame from the video stream
            ret, frame = video_capture.read()

            # Convert the frame to RGB (OpenCV uses BGR by default)
            rgb_frame = frame[:, :, ::-1]

            # Find all face locations and encodings in the current frame
            face_locations = face_recognition.face_locations(rgb_frame)
            face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

            # Loop through each face found in the frame
            for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
                # Compare the current face encoding with all known encodings
                matches = face_recognition.compare_faces(known_encodings, face_encoding)

                name = "Unknown"  # Default name if face is not recognized

                # If a match is found, set the name to the corresponding roll number
                if True in matches:
                    index = matches.index(True)
                    name = roll_numbers[index]

                    # Check if attendance for this student has already been recorded
                    if name not in attendance_recorded:
                        update_attendance_csv(name, subject)
                        attendance_recorded.append(name)
                        cv2.putText(frame, "Attendance Recorded", (left + 6, bottom + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                                    (0, 255, 0), 1)
                    else:
                        cv2.putText(frame, "Attendance Already Recorded", (left + 6, bottom + 20),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)

                # Draw a rectangle around the face and display the name
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
                cv2.putText(frame, name, (left + 6, bottom - 6), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

            # Display the resulting frame
            cv2.imshow('Video', frame)

            # Check for 'q' key press to exit the loop
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # Release the video capture and close all OpenCV windows
        video_capture.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    run_attendance()








