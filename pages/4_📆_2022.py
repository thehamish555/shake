import streamlit as st

st.set_page_config(
    page_title='Raspberry Shake App | 2022',
    page_icon='🤖',
    layout='wide',
    menu_items={
    'Get Help': None,
    'About': '# Raspberry Shake App',
    'Report a bug': None}
    )

st.title('CRISiSLab Challenge 2022')
st.subheader('About')
st.write('Our vision for CRISiSLab Challenge is to encourage more students to '
    'get interested in science and technology, as well as build awareness of '
    'disaster resilience. The students will work in teams and demonstrate '
    'their skills in science communication, presentation and creativity! The '
    'CRISiSLab Challenge 2022 has officially launched on 16 May 2022, and we '
    'have 10 colleges in Wellington joining the competition! They are '
    'Wellington College, Wellington High School, Wellington East Girls’ '
    'College, St Patrick’s College, St Mary’s College, Taita College, Te Kura '
    'Māori o Porirua, Hutt International Boys’ School, Samuel Marsden '
    'Collegiate School and Paraparaumu College. We can’t wait for another '
    'awesome event where the winners will win a summer internship with '
    'CRISiSLab at Massey University!')
st.markdown('[Learn More](https://crisislab.org.nz/crisislab-challenge-2022/)',
    unsafe_allow_html=True)
