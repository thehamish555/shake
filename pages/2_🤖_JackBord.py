import streamlit as st
from PIL import Image

st.set_page_config(
                   page_title='Raspberry Shake App | JackBord',
                   page_icon='🤖',
                   layout='wide',
                   menu_items={
                   'Get Help': None,
                   'About': '# Raspberry Shake App',
                   'Report a bug': None})

lc, mc, rc = st.columns([4, 1, 2])

rc.image(Image.open('./media/jackbord_logo.png'), width=250,
    caption='JackBord Logo')

lc.title('JackBord')
lc.write('JackBord is the main supporter for this project at Paraparaumu '
    'College. They have encouraged several groups of students to particpate '
    'in this competition.')
lc.write('By recognising the challenges in teaching and learning robotics, '
    'Jack and his students created the JackBord. The JackBord is the ultimate '
    'educational system for learning STEM subjects and opens up a world of '
    'opportunities for students of all abilities and backgrounds. The '
    'JackBord is fun and easy to learn for teachers, students, and family. No '
    'prior knowledge is required, and everyone can learn at their own pace. '
    'The JackBord was created and developed on the Kāpiti Coast and continues '
    'to be produced here. Environmentally friendly, 25% of the materials are '
    'recycled and sourced in New Zealand')
st.markdown('[Learn More](https://jackbord.org)', unsafe_allow_html=True)
