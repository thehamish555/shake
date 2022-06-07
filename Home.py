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

lc, rc = st.columns(2)

lc.title('Raspberry Shake Data')
lc.write('This app is designed to display data for the Raspberry Shake')
