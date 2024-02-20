import streamlit as st
import pytube as pt
from io import BytesIO

@st.cache_resource(show_spinner=False)
def download_youtube_video(url : str, only_audio : bool=False):
	yt_video = pt.YouTube(url)
	
	list_streams = (
		yt_video
		.streams
		.filter(
			file_extension='mp4', 
			only_audio=only_audio
		)		
	)
	
	stream = (
		list_streams.get_highest_resolution()
			if not only_audio
				else list_streams.first()
	)

	buffer = BytesIO()
	stream.stream_to_buffer(buffer)
	buffer.seek(0)

	return buffer
