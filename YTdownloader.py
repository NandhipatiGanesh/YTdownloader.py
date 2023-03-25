import os
import platform
import streamlit as st
from pytube import YouTube
from pytube.exceptions import *

st.title("YouTube Video Downloader")

# Get video URL input from user
url = st.text_input("Enter the YouTube video URL:")

# Download the video if URL is valid and download button is clicked
if st.button("Download"):
    try:
        # Create YouTube object and get the highest resolution stream
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()

        # Download the video
        st.write("Downloading video...")
        if platform.system() == "Windows":
            download_path = os.path.join(os.path.expanduser("~"), "Downloads")
        elif platform.system() == "Darwin":
            download_path = os.path.join(os.path.expanduser("~"), "Downloads")
        elif platform.system() == "Linux":
            download_path = os.path.join(os.path.expanduser("~"), "Downloads")
        elif platform.system() == "Android":
            download_path = os.path.join(os.path.expanduser("~"), "Download")
        elif platform.system() == "iOS":
            download_path = os.path.join(os.path.expanduser("~"),)
            
        stream.download()
        st.write("The video is downloaded")    
    except:
          st.write("Invalid URL or some error occurred.")    