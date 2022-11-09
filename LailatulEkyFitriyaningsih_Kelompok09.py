""""
TUGAS 2 ALGORITMA DAN PEMROGRAMAN (KELAS D)
LAILATUL EKY FITRIYANINGSIH
222410102019
"""


print("""   
    =====DATA RINCIAN SAPI=====
    1  Sapi Warrior = 690 hari
    2  Sapi Mage    = 420 hari
    3  Sapi Assasin = 530 hari
    4  Sapi Nolep   = 330 hari   
    """)

Sapi_Warrior = 690
Sapi_Mage    = 420
Sapi_Assasin = 530
Sapi_Nolep   = 330
jumlah_sapi = int(input("Masukkan jumlah sapi yang dimiliki : "))

waktu = 0
for kode_sapi in range (jumlah_sapi) :
    kode_sapi = int(input("Masukkan kode sapi : "))
    if kode_sapi == 1 : 
        waktu += Sapi_Warrior
    elif kode_sapi == 2 :
        waktu += Sapi_Mage
    elif kode_sapi == 3 :
        waktu += Sapi_Assasin
    elif kode_sapi == 4 :
        waktu += Sapi_Nolep
    else :
        print ("Kode sapi",kode_sapi,"tidak terdaftar")

tahun = int(waktu // 365)
bulan = int((waktu - tahun * 365) // 30)
hari = int(waktu - tahun * 365 - bulan * 30)
print("Jumlah hari yang diperlukan ialah " +str(tahun)+ " tahun, " +str(bulan)+ " bulan, dan " +str(hari)+ " hari")