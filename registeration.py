import streamlit as st
import pandas as pd
import os

def save_to_csv(data):
    file_path = 'Students_details.csv'
    if not os.path.exists(file_path):
        with open(file_path, 'w') as f:
            f.write(','.join(data.keys()) + '\n')
    df = pd.DataFrame(data, index=[0])
    df.to_csv(file_path, mode='a', header=False, index=False)

def save_image(file, roll_number):
    image_folder = 'Images'
    if not os.path.exists(image_folder):
        os.makedirs(image_folder)
    file_path = os.path.join(image_folder, f"{roll_number}.png")  # Modified file name format
    with open(file_path, "wb") as f:
        f.write(file.getbuffer())
    return file_path

def run_registration():
    st.title('Registration')
    st.write('Please fill out the following information to register:')

    # Input fields
    first_name = st.text_input("First Name")
    last_name = st.text_input("Last Name")
    roll_number = st.text_input("Roll Number")
    branch = st.selectbox("Branch", ["Computer Science", "Electrical", "Mechanical", "Civil", "Other"])
    year = st.selectbox("Year", ["1st Year", "2nd Year", "3rd Year", "4th Year"])
    mobile_number = st.text_input("Mobile Number")
    email = st.text_input("Email")
    address = st.text_area("Address")
    image = st.file_uploader("Upload Image", type=['png', 'jpg', 'jpeg'])

    # Submit button
    if st.button("Submit"):
        # Processing the form submission
        if first_name and last_name and roll_number and branch and year and mobile_number and email and address and image:
            data = {
                'FirstName': [first_name],
                'LastName': [last_name],
                'RollNumber': [roll_number],
                'Branch': [branch],
                'Year': [year],
                'MobileNumber': [mobile_number],
                'Email': [email],
                'Address': [address]
            }
            save_to_csv(data)
            image_path = save_image(image, roll_number)  # Save image with roll number
            st.success("Registration successful!")
            st.write("First Name:", first_name)
            st.write("Last Name:", last_name)
            st.write("Roll Number:", roll_number)
            st.write("Branch:", branch)
            st.write("Year:", year)
            st.write("Mobile Number:", mobile_number)
            st.write("Email:", email)
            st.write("Address:", address)
            st.write("Image saved as:", image_path)  # Show image path

if __name__ == "__main__":
    run_registration()
