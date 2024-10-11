import streamlit as st
from camera_input_live import camera_input_live

image= camera_input_live(debounce=300) #>300

if image is not None:

    st.image(image)
