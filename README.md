# YTdownloader.py
Youtube Video Downloader 
<h3 align="center">A passionate frontend developer from India</h3>

<h3 align="left">Connect with me:</h3>
<p align="left">
</p>

<p> Simple Guide</p>
<ul>
  <li>Install streamlit </li>
  <li>install Pytube</li>
  </ul>
  
  And write code your own or else put this  code :-
  
  /*you can simply copy */
  
  
  import streamlit as st
from pytube import YouTube


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
    
    <p>If you want add more features or any  Do your own or else takes AI help</p>
    
    <h5>You if want to add a footer for your branding</h5>
    copy this code:- 
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
<p>Developed with ❤ by <a style='display: block; text-align: center;' href="https://github.com/NandhipatiGanesh" target="_blank">Your Name</a></p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)    
    
    
