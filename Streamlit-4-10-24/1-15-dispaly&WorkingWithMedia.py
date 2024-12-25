import streamlit as st

#working with media file
from PIL import Image
img=Image.open("Data/img.jpg")
st.image(img)

#display from url
# st.image("url of image")

#display  video
video_file=open("Data/video.mp4","rb").read()
st.video(video_file,start_time=10)

#work with audio file
# audio_file=open("Data/song.mp3","rb").read()
# st.audio(audio_file)