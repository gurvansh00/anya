import streamlit as st
import tempfile
import subprocess
import cv2
import AnalyzerModule as pm
import numpy as np
import mediapipe as mp
import matplotlib.pyplot as plt
import base64

st.title('Trackmen')
joints = [pm.SHOULDER_RIGHT,pm.HIP_RIGHT,pm.KNEE_RIGHT,pm.ANKLE_RIGHT,pm.ELBOW_RIGHT]
limbs = [pm.ARM_LOWER_RIGHT,pm.ARM_UPPER_RIGHT,pm.UPPER_BODY_RIGHT,pm.LEG_UPPER_RIGHT,pm.LEG_LOWER_RIGHT, pm.FOOT_RIGHT]
players2 = ['user']
def analyze_multiple_players(names):
    for name in names:
        path = name + '.MOV'
        st.video(path)
        pm.pipeline(path = path, output_name = name, joints=joints,limbs=limbs, out_frame_rate=12)
def displayPDF(file):
    # Opening file from file path
    with open(file, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')

    # Embedding PDF in HTML
    pdf_display = F'<embed src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf">'

    # Displaying File
    st.markdown(pdf_display, unsafe_allow_html=True)
  
video = st.file_uploader('upload your video')

if video is not None:
  tfile = tempfile.NamedTemporaryFile(delete=False)
  tfile.write(video.read())
  subprocess.call(['ffmpeg','-i',tfile.name,'user.MOV'])
  st.write('done')
  #analyze_multiple_players(players2)
  st.video('Videos/user.avi')
  displayPDF('Graphs/user.pdf')
