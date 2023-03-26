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
    st.success('Downloading Success', icon="✅")
    
    #add a footer 

footer="""<style>
a:link , a:visited{
color: blue;
background-color: transparent;
text-decoration: none;
}
a:hover,  a:active {
color: red;
background-color: transparent;
text-decoration: underline;
}
.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: white;
color: black;
text-align: center;
}
</style>
<div class="footer">
<p>Developed with ❤ by <a style='display: block; text-align: center;' href="https://github.com/NandhipatiGanesh" target="_blank">Ganesh Kumar</a></p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)    