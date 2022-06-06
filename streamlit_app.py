
import streamlit as st
from helpers import read_markdown

import page_distances as pd

st.set_page_config(page_title='Cosmolator')

pages = {
        "Cosmological Distances": pd,
    }

st.sidebar.title("Main options")

page = st.sidebar.radio("", tuple(pages.keys()))

pages[page].show_page()
        
