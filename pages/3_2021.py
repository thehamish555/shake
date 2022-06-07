import streamlit as st

st.set_page_config(
    page_title='Raspberry Shake App',
    page_icon='🤖',
    layout='wide',
    menu_items={
    'Get Help': None,
    'About': '# Raspberry Shake App',
    'Report a bug': None}
    )

st.title('CRISiSLab Challenge 2021')
st.write('In 2021, we launched our inaugural event and 6 colleges with over '
    '50 students in the Wellington region participated.')
st.video(open('CRISiSLab Challenge 2021.mp4', 'rb').read())
