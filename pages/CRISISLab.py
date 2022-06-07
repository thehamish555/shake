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

lc, mc, rc = st.columns([4, 1, 2])

rc.image(Image.open('crisislab_logo.png'), width=250, caption='CRISISLab Logo')

st.title('CRISISLab')