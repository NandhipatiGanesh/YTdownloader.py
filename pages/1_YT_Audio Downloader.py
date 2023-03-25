import streamlit as st
from pytube import YouTube
import moviepy.editor as mp

# set up the Streamlit app
st.title("YouTube Downloader")

# allow user to input the video URL
url = st.text_input("Enter the YouTube video URL")

# when the user clicks the download button
if st.button("Download Audio"):

    # download the video
    yt = YouTube(url)
    video = yt.streams.get_highest_resolution()
    video_file = video.download()

    # convert video to audio
    audio_file = video_file[:-4] + '.mp3'
    clip = mp.AudioFileClip(video_file)
    clip.write_audiofile(audio_file)

    # save the downloaded audio to the user's device
    with open(audio_file, 'rb') as f:
        audio_bytes = f.read()
    st.download_button(label='Download Audio', data=audio_bytes, file_name='my_audio.mp3')