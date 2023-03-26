import streamlit as st
from pytube import YouTube
import streamlit.components.v1 as components
import fontawesome as fa

import streamlit as st

st.set_page_config(
    page_title="YouTube Video Downloader",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

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
    st.success('Successfully Downloaded', icon="✅")
    

#display text 
with st.expander("**More Downloaders**"):
     st.write("• [**AudioDownloader**](https://nandhipatiganesh-ytaudiodownloader-py-downloader-j7w1w3.streamlit.app/)")
     st.write("• Instagram Reels Downloader is available click on left sidebar and select there")
     st.write("• This apps take time to open and also for downloading files also")
     
   

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