import streamlit as st
from PIL import Image
from datetime import datetime, timedelta
from load_data import LoadData
from obspy.clients.fdsn.header import FDSNNoDataException, FDSNException

st.set_page_config(
                   page_title='Raspberry Shake App | Data',
                   page_icon='🤖',
                   layout='wide',
                   menu_items={
                   'Get Help': None,
                   'About': '# Raspberry Shake App',
                   'Report a bug': None})


@st.cache
def get_data(starttime, endtime, shake):
    return LoadData(starttime, endtime, shake)


st.title('Data')

columns = st.columns([2, 1])
columns[1].subheader('Collecting Data Code')
columns[1].code(open('load_data.py', 'r').read())
columns[1].download_button('Download Code', open('load_data.py', 'rb'),
                           file_name='ShakeData.py', mime='text/python')
columns[0].subheader('Time Frame')
x = columns[0].slider('Select How Many Days to View Back', 1, 31, 1)
y = columns[0].slider('Select How Many Hours to View Back', 0, 23, 0)
columns[0].subheader('Raspberry Shake')
shake = columns[0].text_input('Shake ID', 'AM.R411A.00.EHZ')
endtime = datetime.now()
endtime = endtime.replace(second=0, microsecond=0, minute=0,
                          hour=endtime.hour) + timedelta(hours=\
                                                         endtime.minute//60)
starttime = endtime - timedelta(days=x, hours=y)
text = columns[0].text('Getting Data...')
try:
    data = get_data(starttime, endtime, shake)
except IndexError:
    text.text('No Shake ID or Invalid Shake ID')
except FDSNNoDataException:
    text.text('Invalid Shake ID or Shake Offline')
except FDSNException:
    text.text('No Internet Connection')
except:
    text.text('Unknown Error')
else:
    text.text('Data Loaded')
    endtime = endtime.strftime("%d/%m/%Y, %H:%M:%S")
    starttime = starttime.strftime("%d/%m/%Y, %H:%M:%S")
    columns[0].write(f'✨ Viewing Time Frame For {starttime} - {endtime} ✨')
    text.text('Loading Graph')
    columns[0].write(data.plot())
    text.text('')

    if st.checkbox('Show Raw Data'):
        st.subheader('Raw Data')
        text = st.text('Getting Data...')
        st.download_button('Download Data', str(data.__str__(extended=True)),
                           file_name=f'{shake}.mseed', mime='text/mseed')
        st.subheader('Data')
        st.write(data.__str__(extended=True))
        text.text('')