import cv2
import streamlit as st
from datetime import datetime


st.title("Motion Cam")


#columns for buttons columns 3 and 4 are just filler
col1, col2, col3, col4 = st.columns([1,2,1,1])

with col1:
    #buttons
    start = st.button("Start Cam")

with col2:
    stop = st.button("Stop Cam", type='primary')


if start:
    streamlit_image = st.image([])
    camera = cv2.VideoCapture(0)
    if stop:
        camera.release()

    while True:
        now = datetime.now()
        check, frame = camera.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        cv2.putText(img=frame, text=now.strftime('%A'), org=(50, 70),
                    fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=4,
                    color=(255, 255, 255), thickness=2, 
                    lineType=cv2.LINE_AA)
        cv2.putText(img=frame, text=now.strftime('%m/%Y, %H:%M:%S'), org=(50, 140),
                    fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=4,
                    color=(255, 0, 0), thickness=5, 
                    lineType=cv2.LINE_AA)
        
        streamlit_image.image(frame)