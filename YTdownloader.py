import streamlit as st
from pytube import YouTube

# set up the Streamlit app
st.title("YouTube Downloader")

# allow user to input the video URL
url = st.text_input("Enter the YouTube video URL")

# when the user clicks the download button
if st.button("Download"):

    # download the video
    yt = YouTube(url)
    video = yt.streams.get_highest_resolution()
    video_file = video.download()

    # save the downloaded video to the user's device
    with open(video_file, 'rb') as f:
        video_bytes = f.read()
    st.download_button(label='Download Video', data=video_bytes, file_name='my_video.mp4')
