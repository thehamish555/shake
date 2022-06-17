import streamlit as st
from PIL import Image

st.set_page_config(
                   page_title='Raspberry Shake App | Data',
                   page_icon='🤖',
                   layout='wide',
                   menu_items={
                   'Get Help': None,
                   'About': '# Raspberry Shake App',
                   'Report a bug': None})


@st.cache
def load_data():
    pass


st.title('Data')
if st.checkbox('Show Raw Data'):
    st.subheader('Raw Data')
    load_data()

columns = st.columns(2)
columns[0].subheader('Time Frame')
x = columns[0].slider('Select Time', 0, 23, 12)
columns[0].write(f'Viewing Time Frame For {x}:00:')