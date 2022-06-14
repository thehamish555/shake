import streamlit as st
from PIL import Image

st.set_page_config(
    page_title='Raspberry Shake App | Our Team',
    page_icon='🤖',
    layout='centered',
    menu_items={
    'Get Help': None,
    'About': '# Raspberry Shake App',
    'Report a bug': None}
    )

columns = st.columns(3)

columns[0].image(Image.open('./portraits/hamish_lester.png'), width=150, caption='Hamish Lester | Software Developer')
columns[1].image(Image.open('./portraits/unknown_person.png'), width=150, caption='Dayna Engelen | Role')
columns[2].image(Image.open('./portraits/unknown_person.png'), width=150, caption='Kentaro Baggott | Role')

columns = st.columns([1, 2, 3])
columns[1].image(Image.open('./portraits/unknown_person.png'), width=150, caption='Shekinah Bryson | Role')
columns[2].image(Image.open('./portraits/unknown_person.png'), width=150, caption='Joshua Ray | Role')