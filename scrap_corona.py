'''
Coronavirus data update.
source : 'https://www.worldometers.info/coronavirus/'
Main idea taken from @amazing.python 
Sirloc Fri 10 2020
'''

import requests 
from bs4 import BeautifulSoup
import time
import os
from datetime import datetime


def scrap(x1,x2):
    a = 0
    
    r = requests.get(x1)
    s = BeautifulSoup(r.text,'html.parser')

    data = s.findAll('td')
    data = data[104:]
    
    for nn in data[0::13]:
        if a < 229:
            try:
                country = str(nn).split(path)[1].split('/')[0].split('<')[0]
                total_cases = str(data[a*13+1]).split('>')[1].split('<')[0]
                new_cases = str(data[a*13+2]).split('>')[1].split('<')[0]
                total_deaths = str(data[a*13+3]).split('>')[1].split('<')[0]
                new_deaths = str(data[a*13+4]).split('>')[1].split('<')[0]
                total_recovered = str(data[a*13+5]).split('>')[1].split('<')[0]
                active_cases = str(data[a*13+6]).split('>')[1].split('<')[0]
                serious_critical = str(data[a*13+7]).split('>')[1].split('<')[0]
                total_tests = str(data[a*13+10]).split('>')[1].split('<')[0]
                
                os.system('clear')
                print('''

                  Coronavirus Country Information
                  

                    ''')
                print(' Country:          ',country,
                      '\n Total Cases:      ',total_cases,
                      '\n New Cases:        ',new_cases,
                      '\n Total Deaths:     ',total_deaths,
                      '\n New Deaths:       ',new_deaths,
                      '\n Total Recovered:  ',total_recovered,
                      '\n Active Cases:     ', active_cases,
                      '\n Serious Critical: ', serious_critical,
                      '\n Total Tests:      ', total_tests)
                
                
                a+=1
            except:

                a+=1
                pass
        else:
            pass



        
pais = input('Input country name:  ')
print(' ')
path = '<td style="font-weight: bold; font-size:15px; text-align:left;"><a class="mt_a" href="country/' + str(pais) +'/">'
url = 'https://www.worldometers.info/coronavirus/'




try:

  while True:
      scrap(url,path)

      now = datetime.now()
      current_time = str(now.strftime("%H:%M:%S"))
      print('\n Source :  https://www.worldometers.info/coronavirus/#countries')
      print('\n \n Last update: ', current_time)
      print('\n Original idea : @amazingg.python')
      time.sleep(300)

except KeyboardInterrupt:
  os.system('clear')
  print('End Proram')


