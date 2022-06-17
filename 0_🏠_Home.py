import streamlit as st
from PIL import Image

st.set_page_config(
                   page_title='Raspberry Shake App | Home',
                   page_icon='🤖',
                   layout='wide',
                   menu_items={
                   'Get Help': None,
                   'About': '# Raspberry Shake App',
                   'Report a bug': None})

lc, mc, rc = st.columns([4, 1, 2])

rc.image(Image.open('./media/shake_logo.png'), width=350)
rc.image(Image.open('./media/crisislab_logo.png'), width=200)
rc.image(Image.open('./media/massey_logo.png'), width=350)
rc.image(Image.open('./media/jackbord_logo.png'), width=150)
rc.image(Image.open('./media/paraparaumu_logo.png'), width=350)

lc.title('Raspberry Shake App')
lc.write('This app is designed to display data for the Raspberry Shake for '
    'the [CRISiSLab](/CRISiSLab) challenge 2022. You can find information on '
    'the supporters and the competition using the navigation menu to the '
    'left.')
lc.write('This app was created by one of the teams competing in the '
    'competition, {Insert Name}. Learn more about our team in the '
    '[Our Team](/Our_Team) section.')