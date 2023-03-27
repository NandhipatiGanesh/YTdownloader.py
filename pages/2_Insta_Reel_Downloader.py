import instaloader
import requests
import streamlit as st

# create a function to download the video
def download_video(post_url):
    # create an instance of Instaloader
    L = instaloader.Instaloader()

    # get the post data
    post_data = instaloader.Post.from_shortcode(L.context, post_url.split("/")[-2])

    # get the video URL and download it
    video_url = post_data.video_url
    video_bytes = requests.get(video_url).content

    # create a file downloader for the user to save the video file
    st.download_button(label="Download Video", data=video_bytes, file_name="my_video.mp4", mime="video/mp4")

# create the Streamlit app
st.title("Instagram Video Downloader")

# get the post URL from the user
post_url = st.text_input("Enter the Instagram post URL:")

# create a button to download the video
if st.button("Download Video"):
    download_video(post_url)











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