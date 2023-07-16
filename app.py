import streamlit as st
import tempfile
import subprocess
import cv2
import AnalyzerModule as pm
import numpy as np
import mediapipe as mp
import matplotlib.pyplot as plt

joints = [pm.SHOULDER_RIGHT,pm.HIP_RIGHT,pm.KNEE_RIGHT,pm.ANKLE_RIGHT,pm.ELBOW_RIGHT]
limbs = [pm.ARM_LOWER_RIGHT,pm.ARM_UPPER_RIGHT,pm.UPPER_BODY_RIGHT,pm.LEG_UPPER_RIGHT,pm.LEG_LOWER_RIGHT, pm.FOOT_RIGHT]
video = st.file_uploader('upload your video',type=['mp4','mpeg4','avi'])

if video is not None:
  tfile = tempfile.NamedTemporaryFile(delete=False)
  tfile.write(video.read())
  subprocess.call(['ffmpeg','-i',tfile.name,'user.MOV'])
  st.write('done')
  st.video('user.MOV')
  pm.pipeline(path = path, output_name = name, joints=joints,limbs=limbs, out_frame_rate=12)
