import streamlit as st
import tempfile
import subprocess

video = st.file_uploader('upload your video',type=['mp4','mpeg4','avi'])
if video is not None:
  tfile = tempfile.NamedTemporaryFile(delete=False)
  tfile.write(f.read())
  subprocess.call(['ffmpeg','-i',tfile.name,'user.MOV'])
  
