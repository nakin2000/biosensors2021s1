# -*- coding: utf-8 -*-
"""

@author: kin45
"""
import requests,pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df_json = pd.read_csv('download_province_timeline.csv')
df_json_vaccination = pd.read_csv('owid-covid-data.csv')
array = np.zeros( (78, 224) )
newcase = df_json['new_case']
province = df_json['province']
array_vaccination = np.zeros((224,1))
array_new_vaccination = np.zeros((224,1))
array_date = np.zeros((224,1))
people_vaccinated = df_json_vaccination['people_vaccinated']
new_vaccinations = df_json_vaccination['new_vaccinations']
eng_province = ['Krabi','Bangkok','Kanchanaburi','Kalasin','Kamphaeng Phet',
                'Khon Kaen','Chanthaburi','Chachoengsao','Chon Buri','Chai Nat',
                'Chaiyaphum','Chumphon','Trang','Trat','Tak',
                'Nakhon Nayok','Nakhon Pathom','Nakhon Phanom','Nakhon Ratchasima','Nakhon Si Thammarat',
                'Nakhon Sawan','Nonthaburi','Narathiwat','Nan','Buang Kan',
                'Buri Ram','Pathum Thani','Prachuap Khiri Khan','Prachin Buri','Pattani',
                'Phra Nakhon Si Ayutthaya','Phayao','Phangnga','Phatthalung','Phichit',
                'Phitsanulok','Phuket','Maha Sarakham','Mukdahan','	Yala',
                'Yasothon','Ranong','Rayong','Ratchaburi','Roi Et',
                'Lop Buri','Lampang','Lamphun','Si Sa Ket','Sakon Nakhon',
                'Songkhla','Satun','Samut Prakan','Samut Songkhram','Samut Sakhon',
                'Saraburi','Sa Kaeo','Sing Buri','Suphan Buri','Surat Thani',
                'Surin','Sukhothai','Nong Khai','Nong Bua Lam Phu','Amnat Charoen',
                'Udon Thani','Uttaradit','Uthai Thani','Ubon Ratchathani','Ang Thong',
                'Chiang Rai','Chiang Mai','Phetchaburi','Phetchabun','Loei',
                'Phrae','Mae Hong Son','Not Specified']

i=0
for row in range(78):
    for col in range(224):
        array[row,col] = newcase[i]
        i=i+78
    i=1
    i=i+row
    
j=120827 
for row1 in range(224):
    array_vaccination[row1,0] = people_vaccinated[j]
    j=j+1

k=120827 
for row2 in range(224):
    array_new_vaccination[row2,0] = new_vaccinations[k]
    k=k+1

# array_date[0,0] = date[j]


x_close = [110,110]
y_close = [0,50000000]
x = np.arange(0,224)
y = array[0,:]
y_Samut_Sakhon = array[54,:]
y_Samut_Songkhram = array[53,:]
y_Ratchaburi = array[43,:]
y_Nakhon_Pathom = array[16,:]
y_Nonthaburi = array[21,:]
y_Bangkok = array[1,:]
y_Samut_Prakan = array[52,:]
y_vac = array_vaccination[:,0]
y_new_vac = array_new_vaccination[:,0]
# plt.plot(x, y_Samut_Sakhon, label = eng_province[54])
# plt.plot(x, y_Samut_Songkhram, label = eng_province[53])
# plt.plot(x, y_Ratchaburi, label = eng_province[43])
# plt.plot(x, y_Nakhon_Pathom, label = eng_province[16])
# plt.plot(x, y_Nonthaburi, label = eng_province[21])
# plt.plot(x, y_Bangkok, label = eng_province[1])
# plt.plot(x, y_Samut_Prakan, label = eng_province[52])
plt.plot(x,y_vac, label = "vac")
# plt.plot(x,y_new_vac, label = "new vaccination")
plt.plot(x_close, y_close, label = "province closing date", linestyle="--")
plt.title("Vaccination")
plt.xlabel("Day")
# plt.ylabel("number of infected people")
plt.legend()
plt.show()
# font2 = {'family':'serif','color':'darkred','size':12}
# l=0
# for p in range(0,12):
#     plt.subplot(6,2, l+1)
#     plt.plot(x,y)
#     plt.title(eng_province[p], fontdict = font2, loc = 'left')
#     y = array[p+1,:]
#     l=l+1
# plt.show()