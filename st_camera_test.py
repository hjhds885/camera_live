import streamlit as st
from camera_input_live import camera_input_live
deb = st.slider(
        "debounce(処理実行制御):", min_value=0.0, max_value=2000.0, value=300.0, step=10.0
)
image = ""
image= camera_input_live(
        debounce=deb,
        height: int = 265,
        width: int = 352, 
 　　　　) #>300


if image is not None:
        st.image(image)
        image=""
        
