from obspy.clients.fdsn import Client
from obspy import UTCDateTime
from datetime import datetime, timedelta

client = Client(base_url='https://fdsnws.raspberryshakedata.com/')

def LoadData(starttime, endtime, shake):
    shake = shake.upper().split('.')
    starttime = UTCDateTime(starttime)
    endtime = UTCDateTime(endtime)
    data = client.get_waveforms(shake[0], shake[1], shake[2], shake[3],
                                starttime, endtime) 
    data.detrend(type='demean')
    data.filter('bandpass', freqmin=0.7, freqmax=2, corners=4)
    return data

if __name__ == '__main__':
    print('Getting test data!')
    endtime = datetime.now()
    starttime = endtime - timedelta(days=1)
    LoadData(starttime, endtime, 'AM.R411A.00.EHZ')