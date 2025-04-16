# face_siwes
An Attendance System based on Facial Recognition

![image](https://github.com/user-attachments/assets/8828f549-afb9-4119-836c-96b3b8939ba0)

# Overview
This project is a Facial Recognition Attendance System designed to automate the process of taking attendance using facial recognition technology. The system captures live video feed from a webcam, detects faces, and matches them against a pre-trained database of facial encodings. Once a match is found, the system records the attendance in an Excel sheet. The project is built using Python, OpenCV, and the face_recognition library, with a user-friendly interface created using customtkinter.

# Features
Real-time Face Detection: Captures live video feed and detects faces in real-time.

Facial Recognition: Matches detected faces against a pre-trained database of facial encodings.

Attendance Recording: Automatically records attendance in an Excel sheet with the name, date, and time of recognition.

User Interface: Provides a simple and intuitive GUI for interacting with the system.

View Attendance: Allows users to view the recorded attendance in a tabular format.

# Requirements
To run this project, you need the following Python libraries installed:

opencv-python

customtkinter

face_recognition

numpy

Pillow

openpyxl

pandas

You can install these libraries using pip:

bash
Copy
pip install opencv-python customtkinter face_recognition numpy Pillow openpyxl pandas
How to Use
Prepare the Facial Encodings:

Place images of the individuals in the load_images folder. The images should be named after the individuals (e.g., john.jpg).

Run the face_funcs.py script to generate facial encodings and save them in encoded_faces.dat.

# Run the Application:

Execute the face_rec.py script to start the application.

The application will open a window with a live video feed from your webcam.

Click the "VERIFY FACE" button to detect and recognize faces. If a match is found, the attendance will be recorded.

View Attendance:

Click the "VIEW ATTENDANCE" button to open a new window displaying the recorded attendance in a tabular format.

Project Structure
face_rec.py: The main script that runs the application, handles the GUI, and processes the webcam feed.

face_funcs.py: Contains functions for facial recognition, encoding, and attendance recording.

view_attendance.py: Provides a GUI to view the recorded attendance in an Excel sheet.

encoded_faces.dat: Stores the facial encodings of individuals.

attendance.xlsx: The Excel file where attendance records are stored.

# Future Improvements
Multiple Face Detection: Enhance the system to handle multiple faces in a single frame.

Unknown Face Handling: Add functionality to handle unknown faces and prompt the user to add them to the database.

Improved UI: Enhance the user interface with more features and better design.

Database Integration: Integrate with a database for more robust attendance management.
