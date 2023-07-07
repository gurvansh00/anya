import streamlit as st
import moviepy.editor as moviepy

video = st.file_uploader('upload your video')
if video is not None:
  clip = moviepy.VideoFileClip(video)
  clip.write_videofile("myvideo.MOV")
st.write('done processing')

st.video('myvideo.MOV')
