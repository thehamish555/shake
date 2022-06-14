import streamlit as st
from PIL import Image

st.set_page_config(
    page_title='Raspberry Shake App | CRISiSLab',
    page_icon='🤖',
    layout='wide',
    menu_items={
    'Get Help': None,
    'About': '# Raspberry Shake App',
    'Report a bug': None}
    )

lc, mc, rc = st.columns([4, 1, 2])

rc.image(Image.open('./media/crisislab_logo.png'), width=250,
    caption='CRISiSLab Logo')

lc.title('CRISiSLab')
lc.subheader('About CRISiSLab')
lc.write('The CRISiSLab (Crisis Response and Integrated Simulation Science '
    'Laboratory) is a research and learning laboratory based in the Joint '
    'Centre for Disaster Research (JCDR), Massey University, Wellington. '
    'CRISiSLab provides a platform to conduct transdisciplinary '
    'socio-technical research at the human-technology interface. It provides '
    'a physical space as well as software and hardware resources for various '
    'research and learning activities. Lab activities include design, '
    'development and testing of technology and systems supported by '
    'simulations and experiments. Beyond physical space, the lab provides a '
    'collaborative environment for learning. Currently, the lab is composed '
    'of researchers and PhD students conducting research on artificial '
    'intelligence, big data analytics, decision support systems, warning '
    'systems, technology acceptance and user behaviour. The lab looks to '
    'attract researchers and research students to engage in more '
    'technologically aligned projects for crisis management.')
lc.subheader('Mission')
lc.write('CRISiSLab’s mission is to contribute to advancing technology-driven '
    'solutions in crisis management. The Lab supports building a community of '
    'practice bringing together students and researchers from multiple '
    'universities and agencies to study the design, implementation, and '
    'evaluation of technological tools for crisis management. CRISiSLab '
    'provides physical space as well as software and hardware resources for '
    'various research and learning activities. Lab activities include running '
    'simulations and experiments and design and testing of products and '
    'systems.')
lc.subheader('Vision')
lc.write('To be the pioneer in New Zealand to introduce one stop cross '
    'functional simulation laboratory capable of delivering integrated '
    'requirements of Crisis Related Research, Product Design and Civil '
    'Defence Training.')
st.markdown('[Learn More](https://crisislab.org.nz)', unsafe_allow_html=True)
