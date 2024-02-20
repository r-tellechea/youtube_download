import streamlit as st
import pytube as pt
from download_youtube_video import download_youtube_video

st.set_page_config(
	page_title='Youtube Download', 
	page_icon='🎞️', 
	layout='centered', 
	initial_sidebar_state='auto'
)
st.title('Download a Youtube video')

url = st.text_input(label='Copy here your youtube url:', value='', key='url')

col_toogle_audio, col_click_get_data, col_click_download = st.columns([4,1,1])
with col_toogle_audio:
	only_audio = st.toggle(label='Download only audio', value=False, key='only_audio')
with col_click_get_data:
	click_get_data = st.button(label = 'Get data', key='get_information')

spinner_placeholder = st.empty()

if url:
	st.video(url)

	if click_get_data:
		text_spinner = (
			'Downloading video...' 
				if not only_audio 
					else 'Downloading audio...'
		)
		with spinner_placeholder:
			with st.spinner(text_spinner):
				buffer = download_youtube_video(url=url, only_audio=only_audio)
			st.success('Download completed', icon='✅')
		with col_click_download:
			st.download_button(
				label='Download',
				file_name='youtube_download.mp4',
				data=buffer,
				on_click=st.balloons,
			)
