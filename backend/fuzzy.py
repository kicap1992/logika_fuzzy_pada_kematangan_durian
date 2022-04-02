import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import csv
import skfuzzy as fuzz

import asyncio

async def contoh_dulu(data_durian,anggota_usia,anggota_berat,anggota_keliling,anggota_ukuran_batang,anggota_jarak_duri,i):
  # hitungan fuzzy tsukamoto berdasarkan rule base
  df = pd.read_csv("dataset/rule.csv")
  rule_length = len(df.index)
  list_rule = df
  hitungan_fuzzy_tsukamoto = []
  for e in range(i):
    ket_usia = "Tinggi" if  anggota_usia[e][0] < anggota_usia[e][1] else "Rendah"
    ket_berat = "Tinggi" if anggota_berat[e][0] < anggota_berat[e][1]   else "Rendah" 
    ket_keliling = "Tinggi" if anggota_keliling[e][0] <= anggota_keliling[e][1] else "Rendah"
    ket_ukuran_batang = "Tinggi" if anggota_ukuran_batang[e][0] <= anggota_ukuran_batang[e][1] else "Rendah"
    ket_jarak_duri = "Tinggi" if anggota_jarak_duri[e][0] < anggota_jarak_duri[e][1] else "Rendah"
    
    keterangan = None
    for n in range(rule_length):
        if str(list_rule.at[n,'Usia']) == ket_usia and str(list_rule.at[n,'Berat']) == ket_berat and str(list_rule.at[n,'Keliling']) == ket_keliling and str(list_rule.at[n,'Ukuran Batang']) == ket_ukuran_batang and str(list_rule.at[n,'Jarak Duri']) == ket_jarak_duri:
            keterangan = str(list_rule.at[n,'Keterangan'])
   
    data = {"No" : e, "Usia" :  ket_usia, "Berat" : ket_berat, "Keliling" :  ket_keliling, 
            "Ukuran Batang" :  ket_ukuran_batang, "Jarak Duri" :  ket_jarak_duri ,"Variable Linguistic" :  keterangan,
            "Keterangan" : data_durian.at[e,'Keterangan'], "MSE" : 0 if keterangan == data_durian.at[e,'Keterangan'] else 1
           }
    hitungan_fuzzy_tsukamoto.append(data)    
  await asyncio.sleep(0.1)
  return(hitungan_fuzzy_tsukamoto)


def FungsiKeanggotaan(_range, _min , _hi, _nilai):
    mini = fuzz.interp_membership(_range,_min,_nilai)
    hi = fuzz.interp_membership(_range,_hi,_nilai)
    # await asyncio.sleep(0.1)
    return mini , hi

def RangeSubjektif(_low, _high, _step):
    subjektif =  np.arange(_low, _high , _step)
    return subjektif

def FuzzyShow(_rule, _range_subjektif, _title, _pic_title):
    lo = fuzz.trapmf(_range_subjektif, _rule[0])
    hi = fuzz.trapmf(_range_subjektif, _rule[1])
    
    fig,ax = plt.subplots(nrows=1, figsize=(7,3))
    ax.plot(_range_subjektif, lo, 'g' , linewidth = 1.5 , label= "Mentah")
    ax.plot(_range_subjektif, hi, 'r' , linewidth = 1.5 , label= "Masak")
    
    ax.set_title(_title)
    ax.legend()
    
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()
   
    plt.tight_layout()
    plt.savefig(_pic_title+'.png')
    # plt.show()
    
    
    return lo, hi

def FuzzyShow1(_rule, _range_subjektif, _title,_pic_title):
    lo = fuzz.trapmf(_range_subjektif, _rule[0])
    hi = fuzz.trapmf(_range_subjektif, _rule[1])
    
    fig,ax = plt.subplots(nrows=1, figsize=(7,3))
    ax.plot(_range_subjektif, lo, 'r' , linewidth = 1.5 , label= "Masak")
    ax.plot(_range_subjektif, hi, 'g' , linewidth = 1.5 , label= "Mentah")
    
    ax.set_title(_title)
    ax.legend()
    
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()
    
    plt.tight_layout()
    plt.savefig(_pic_title+'.png')
    # plt.show()
    
    
    return lo, hi

def get_average(min,max) :
    a = (min + max) / 2
    return a 

async def himpunan_fuzzy(min_usia,mid_usia,max_usia,min_berat,mid_berat,max_berat,min_keliling,mid_keliling,max_keliling,min_ukuran_batang,mid_ukuran_batang,max_ukuran_batang,min_jarak_duri,mid_jarak_duri,max_jarak_duri):
  a = None
  himpunan_fuzzy = pd.read_csv("dataset/himpunan_fuzzy.csv")
  himpunan_fuzzy.loc[0, 'Semesta Pembicaraan'] = f"[ {min_usia} , {max_usia} ]" # Semesta pembicaraan (Rendah) Usia
  himpunan_fuzzy.loc[1, 'Semesta Pembicaraan'] = f"[ {min_usia} , {max_usia} ]" # Semesta pembicaraan (Tinggi) Usia
  himpunan_fuzzy.loc[0, 'Domain'] = f"[ {min_usia} , {mid_usia + 0.5} ]" # Domain (Rendah) Usia
  himpunan_fuzzy.loc[1, 'Domain'] = f"[ {mid_usia - 0.5} , {max_usia} ]" # Domain pembicaraan (Tinggi) Usia

  # Fuzzykasi Berat
  himpunan_fuzzy.loc[2, 'Semesta Pembicaraan'] = f"[ {min_berat} , {max_berat} ]" # Semesta pembicaraan (Rendah) Berat
  himpunan_fuzzy.loc[3, 'Semesta Pembicaraan'] = f"[ {min_berat} , {max_berat} ]" # Semesta pembicaraan (Tinggi) Berat
  himpunan_fuzzy.loc[2, 'Domain'] = f"[ {min_berat} , {mid_berat + 10} ]" # Domain (Rendah) Berat
  himpunan_fuzzy.loc[3, 'Domain'] = f"[ {mid_berat - 10} , {max_berat} ]" # Domain pembicaraan (Tinggi) Berat

  # Fuzzykasi Keliling
  himpunan_fuzzy.loc[4, 'Semesta Pembicaraan'] = f"[ {min_keliling} , {max_keliling} ]" # Semesta pembicaraan (Rendah) Keliling
  himpunan_fuzzy.loc[5, 'Semesta Pembicaraan'] = f"[ {min_keliling} , {max_keliling} ]" # Semesta pembicaraan (Tinggi) Keliling
  himpunan_fuzzy.loc[4, 'Domain'] = f"[ {min_keliling} , {mid_keliling + 1} ]" # Domain (Rendah) Keliling
  himpunan_fuzzy.loc[5, 'Domain'] = f"[ {mid_keliling - 1} , {max_keliling} ]" # Domain pembicaraan (Tinggi) Keliling

  # Fuzzykasi Keliling
  himpunan_fuzzy.loc[4, 'Semesta Pembicaraan'] = f"[ {min_keliling} , {max_keliling} ]" # Semesta pembicaraan (Rendah) Keliling
  himpunan_fuzzy.loc[5, 'Semesta Pembicaraan'] = f"[ {min_keliling} , {max_keliling} ]" # Semesta pembicaraan (Tinggi) Keliling
  himpunan_fuzzy.loc[4, 'Domain'] = f"[ {min_keliling} , {mid_keliling + 1} ]" # Domain (Rendah) Keliling
  himpunan_fuzzy.loc[5, 'Domain'] = f"[ {mid_keliling - 1} , {max_keliling} ]" # Domain pembicaraan (Tinggi) Keliling

  # Fuzzykasi Ukuran Batang
  himpunan_fuzzy.loc[6, 'Semesta Pembicaraan'] = f"[ {min_ukuran_batang} , {max_ukuran_batang} ]" # Semesta pembicaraan (Rendah) Ukuran Batang
  himpunan_fuzzy.loc[7, 'Semesta Pembicaraan'] = f"[ {min_ukuran_batang} , {max_ukuran_batang} ]" # Semesta pembicaraan (Tinggi) Ukuran Batang
  himpunan_fuzzy.loc[6, 'Domain'] = f"[ {min_ukuran_batang} , {mid_ukuran_batang + 0.5} ]" # Domain (Rendah) Ukuran Batang
  himpunan_fuzzy.loc[7, 'Domain'] = f"[ {mid_ukuran_batang - 0.5} , {max_ukuran_batang} ]" # Domain pembicaraan (Tinggi) Ukuran Batang

  # Fuzzykasi Jarak Duri
  himpunan_fuzzy.loc[8, 'Semesta Pembicaraan'] = f"[ {min_jarak_duri} , {max_jarak_duri} ]" # Semesta pembicaraan (Rendah) Jarak Duri
  himpunan_fuzzy.loc[9, 'Semesta Pembicaraan'] = f"[ {min_jarak_duri} , {max_jarak_duri} ]" # Semesta pembicaraan (Tinggi) Jarak Duri
  himpunan_fuzzy.loc[8, 'Domain'] = f"[ {min_jarak_duri} , {mid_jarak_duri + 0.75} ]" # Domain (Rendah) Jarak Duri
  himpunan_fuzzy.loc[9, 'Domain'] = f"[ {mid_jarak_duri - 0.25} , {max_jarak_duri} ]" # Domain pembicaraan (Tinggi) Jarak Duri

  # Fuzzykasi Keterangan
  himpunan_fuzzy.loc[10, 'Semesta Pembicaraan'] = f"[ 0 , 1 ]" # Semesta pembicaraan (Rendah) Keterangan
  himpunan_fuzzy.loc[11, 'Semesta Pembicaraan'] = f"[ 0 , 1 ]" # Semesta pembicaraan (Tinggi) Keterangan
  himpunan_fuzzy.loc[10, 'Domain'] = f"[ 0 , 0.5 ]" # Domain (Rendah) Keterangan
  himpunan_fuzzy.loc[11, 'Domain'] = f"[ 0.5 , 1 ]" # Domain pembicaraan (Tinggi) Keterangan

  # print(himpunan_fuzzy.to_dict())
  himpunan_fuzzy.to_csv('out.csv',index=False)

  with open("out.csv", "r") as f:
          reader = csv.DictReader(f)
          a = list(reader)
  await asyncio.sleep(0.2)    
  # print(a)    
  return  a

async def fuzzy(status, usianya = None , beratnya = None , kelilingnya = None , ukuran_batangnya = None , jarak_durinya = None):
  dataset = None
  data_durian = pd.read_csv("dataset/dataset.csv")
  # await asyncio.sleep(0.5)
  with open("dataset/dataset.csv", "r") as f:
        reader =  csv.DictReader(f)
        dataset =  list(reader)
  await asyncio.sleep(0.1)

  # data usia
  data_usia = pd.DataFrame(data_durian)
  data_usia = data_usia['Usia'].tolist()
  _data_usia = data_usia
  min_usia = min(data_usia) - 1
  max_usia = max(data_usia) +1
  mid_usia =np.median(data_usia)
  await asyncio.sleep(0.1)

  # data berat
  data_berat = pd.DataFrame(data_durian)
  data_berat = data_berat['Berat'].tolist()
  _data_berat = data_berat
  min_berat = min(data_berat) - 50
  max_berat = max(data_berat) + 50
  mid_berat =np.median(data_berat)

  # data keliling
  data_keliling = pd.DataFrame(data_durian)
  data_keliling = data_keliling['Keliling'].tolist()
  _data_keliling = data_keliling
  min_keliling = min(data_keliling) - 1
  max_keliling = max(data_keliling) + 1
  # mid_keliling = get_average(min_keliling,max_keliling) #42.0
  mid_keliling =np.median(data_keliling)

  # data ukuran batang
  data_ukuran_batang = pd.DataFrame(data_durian)
  data_ukuran_batang = data_ukuran_batang['Ukuran_batang'].tolist()
  _data_ukuran_batang = data_ukuran_batang
  min_ukuran_batang = min(data_ukuran_batang) - 0.5
  max_ukuran_batang = max(data_ukuran_batang) + 0.5
  # mid_ukuran_batang =   get_average(min_ukuran_batang,max_ukuran_batang) #4.0
  mid_ukuran_batang =  np.median(data_ukuran_batang)

  # data jarak duri
  data_jarak_duri = pd.DataFrame(data_durian)
  data_jarak_duri = data_jarak_duri['Jarak_duri'].tolist()
  _data_jarak_duri = data_jarak_duri
  # print(data_jarak_duri)
  min_jarak_duri = min(data_jarak_duri) - 0.5
  max_jarak_duri = max(data_jarak_duri) + 0.5
  mid_jarak_duri =  get_average(min_jarak_duri,max_jarak_duri)#1.0

 
  var_himpunan_fuzzy = await himpunan_fuzzy(min_usia,mid_usia,max_usia,min_berat,mid_berat,max_berat,min_keliling,mid_keliling,max_keliling,min_ukuran_batang,mid_ukuran_batang,max_ukuran_batang,min_jarak_duri,mid_jarak_duri,max_jarak_duri)

  
  # fuzzy untuk field usia
  x_usia = RangeSubjektif(min_usia , max_usia , 1)
  r_usia = np.array([
      [min_usia,min_usia,mid_usia,mid_usia],
      [mid_usia,mid_usia,max_usia,max_usia]
  ])
  lo_usia , hi_usia = FuzzyShow(r_usia , x_usia, 'Umur (minggu)',"usia")


  # fuzzy untuk field berat
  x_berat = RangeSubjektif(min_berat , max_berat , 1)
  r_berat = np.array([
      [min_berat,min_berat,mid_berat,mid_berat+10],
      [mid_berat,mid_berat+10,max_berat,max_berat]
  ])
  lo_berat , hi_berat = FuzzyShow1(r_berat , x_berat, 'Berat (kg)', "berat")

  # fuzzy untuk field keliling
  x_keliling = RangeSubjektif(min_keliling , max_keliling , 1)
  r_keliling = np.array([
      [min_keliling,min_keliling,mid_keliling,mid_keliling],
      [mid_keliling,mid_keliling,max_keliling,max_keliling]
  ])
  lo_keliling , hi_keliling = FuzzyShow(r_keliling , x_keliling, 'Keliling (cm)', "keliling")

  # fuzzy untuk field ukuran batang
  x_ukuran_batang = RangeSubjektif(min_ukuran_batang , max_ukuran_batang , 1)
  r_ukuran_batang = np.array([
      [min_ukuran_batang,min_ukuran_batang,mid_ukuran_batang,mid_ukuran_batang],
      [mid_ukuran_batang,mid_ukuran_batang,max_ukuran_batang,max_ukuran_batang]
  ])
  lo_ukuran_batang , hi_ukuran_batang = FuzzyShow(r_ukuran_batang , x_ukuran_batang, 'Keliling (cm)', "ukuran_batang")

  # fuzzy untuk field jarak duri
  x_jarak_duri = RangeSubjektif(min_jarak_duri , max_jarak_duri , 1)
  r_jarak_duri = np.array([
      [min_jarak_duri,min_jarak_duri,mid_jarak_duri,mid_jarak_duri],
      [mid_jarak_duri,mid_jarak_duri,max_jarak_duri,max_jarak_duri]
  ])
  lo_jarak_duri , hi_jarak_duri = FuzzyShow(r_jarak_duri , x_jarak_duri, 'Jarak Duri (mm)', "jarak_duri")


  #  Keanggotaan untuk usia
  i = 0
  anggota_usia = []
  for usia in _data_usia:
      ini_dia =  FungsiKeanggotaan(x_usia,lo_usia,hi_usia,usia)
      
      anggota_usia.append(ini_dia)
      i = i+1
  # print(anggota_usia)

  #  Keanggotaan untuk berat
  anggota_berat = []
  for berat in _data_berat:
      ini_dia =  FungsiKeanggotaan(x_berat,lo_berat,hi_berat,berat)
      anggota_berat.append(ini_dia)

  #  Keanggotaan untuk keliling
  anggota_keliling = []
  for keliling in _data_keliling:
      ini_dia =  FungsiKeanggotaan(x_keliling,lo_keliling,hi_keliling,keliling)
      anggota_keliling.append(ini_dia)

  #  Keanggotaan untuk ukuran batang
  anggota_ukuran_batang = []
  for ukuran_batang in _data_ukuran_batang:
      ini_dia =  FungsiKeanggotaan(x_ukuran_batang,lo_ukuran_batang,hi_ukuran_batang,ukuran_batang)
      # print(ini_dia)
      anggota_ukuran_batang.append(ini_dia)

  #  Keanggotaan untuk jarak duri
  anggota_jarak_duri = []
  for jarak_duri in _data_jarak_duri:
      ini_dia =  FungsiKeanggotaan(x_jarak_duri,lo_jarak_duri,hi_jarak_duri,jarak_duri)
      anggota_jarak_duri.append(ini_dia)

  rule_base = None
  with open("dataset/rule.csv", "r") as f:
        reader = csv.DictReader(f)
        rule_base = list(reader)


  keanggotaannya = await contoh_dulu(data_durian,anggota_usia,anggota_berat,anggota_keliling,anggota_ukuran_batang,anggota_jarak_duri,i)

  # print(keanggotaannya)
  data_usia = {'min':min_usia, 'max':max_usia}
  data_berat = {'min':min_berat, 'max':max_berat}
  data_keliling = {'min':min_keliling, 'max':max_keliling}
  data_ukuran_batang = {'min':min_ukuran_batang, 'max':max_ukuran_batang}
  data_jarak_duri = {'min':min_jarak_duri, 'max':max_jarak_duri}
  detail_attribut = {'usia':data_usia, 'berat':data_berat, 'keliling':data_keliling, 'ukuran_batang':data_ukuran_batang, 'jarak_duri':data_jarak_duri}

  if(status == 'ambil_dataset'):
    context = {'detail_attribute':detail_attribut, 'rule_base':rule_base, 'keanggotaan':keanggotaannya, 'dataset' : dataset, 'himpunan_fuzzy' : var_himpunan_fuzzy}

  elif (status == 'load_fuzzy'):
    def hitungan_keterangan(usia,berat,keliling,ukuran_batang,jarak_duri):
        df = pd.read_csv("dataset/rule.csv")
        rule_length = len(df.index)
        list_rule = df
        keterangan = None   
        ket_usia = "Tinggi" if  usia[0] < usia[1] else "Rendah"
        ket_berat = "Tinggi" if berat[0] < berat[1]   else "Rendah" 
        ket_keliling = "Tinggi" if keliling[0] <= keliling[1] else "Rendah"
        ket_ukuran_batang = "Tinggi" if ukuran_batang[0] <= ukuran_batang[1] else "Rendah"
        ket_jarak_duri = "Tinggi" if jarak_duri[0] < jarak_duri[1] else "Rendah"
        for n in range(rule_length):
            if str(list_rule.at[n,'Usia']) == ket_usia and str(list_rule.at[n,'Berat']) == ket_berat and str(list_rule.at[n,'Keliling']) == ket_keliling and str(list_rule.at[n,'Ukuran Batang']) == ket_ukuran_batang and str(list_rule.at[n,'Jarak Duri']) == ket_jarak_duri:
                keterangan = str(list_rule.at[n,'Keterangan'])
                break
        return keterangan

    usia = usianya
    berat = beratnya
    keliling = kelilingnya
    ukuran_batang = ukuran_batangnya
    jarak_duri = jarak_durinya
    keanggotaan_usia = FungsiKeanggotaan(x_usia,lo_usia,hi_usia,usia)
    print(keanggotaan_usia)
    keanggotaan_berat = FungsiKeanggotaan(x_berat,lo_berat,hi_berat,berat)
    print(keanggotaan_berat)
    keanggotaan_keliling = FungsiKeanggotaan(x_keliling,lo_keliling,hi_keliling,keliling)
    print(keanggotaan_keliling)
    keanggotaan_ukuran_batang = FungsiKeanggotaan(x_ukuran_batang,lo_ukuran_batang,hi_ukuran_batang,ukuran_batang)
    print(keanggotaan_ukuran_batang)
    keanggotaan_jarak_duri =FungsiKeanggotaan(x_jarak_duri,lo_jarak_duri,hi_jarak_duri,jarak_duri)
    print(keanggotaan_jarak_duri)
    datanya = hitungan_keterangan(keanggotaan_usia,keanggotaan_berat,keanggotaan_keliling,keanggotaan_ukuran_batang,keanggotaan_jarak_duri)
    context = datanya
  






  
  # hitungan fuzzy tsukamoto berdasarkan data latih

  return context