from lib.eksekusi import maps
from lib.penanganancsv import bukacsv
import configparser
import time

config = configparser.ConfigParser()
config.read('config.ini')
request = config['LOKASI']
proses = config.getboolean('PROSES','headless')

akun = bukacsv.bukaberkas("accounts.csv")
for index, row in akun.iterrows():
    print("Proses "+row['user']+" proses rating")

    minta = maps.kasihrating(request,proses,row)
    time.sleep(2)