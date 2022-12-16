import streamlit as st
import numpy as np
import pandas as pd
from st_functions import st_button, load_css
from PIL import Image

load_css()

col1, col2, col3 = st.columns(3)
col2.image(Image.open('pp.png'))

st.header('Colin Karczewski, Data Engineer')

st.info('Application Development Analyst at Accenture Technology France')

icon_size = 20

st_button('linkedin', 'https://www.linkedin.com/in/colin-karczewski/?locale=en_US', 'Follow me on LinkedIn', icon_size)
st_button('tableau', 'https://public.tableau.com/app/profile/colin1402', 'Check my Tableau dashboards', icon_size)
