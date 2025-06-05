import streamlit as st
import cv2
import numpy as np

st.title("Face Recognition Attendance System - Demo")

start_cam = st.checkbox('Start Camera')

FRAME_WINDOW = st.image([])

# Load Haar cascade face detector
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

camera = cv2.VideoCapture(0)

if start_cam:
    while True:
        ret, frame = camera.read()
        if not ret:
            st.error("Failed to access camera.")
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(frame, "Face Detected", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

        FRAME_WINDOW.image(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

else:
    camera.release()
    st.write("Camera stopped")
