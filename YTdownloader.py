import streamlit as st
from pytube import YouTube

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
        stream.download()
        st.write("Video downloaded successfully!")
    except:
        st.write("Invalid URL or some error occurred.")
