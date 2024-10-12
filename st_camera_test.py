import streamlit as st
from camera_input_live import camera_input_live
deb = st.slider(
        "debounce(処理実行制御):", min_value=240, max_value=300, value=270, step=10
)
image = ""
image= camera_input_live(
        debounce=deb,
        height= 132*2,
        width= 176*2, 
        ) #>300


if image is not None:
        st.image(image)
        #image=""
        
