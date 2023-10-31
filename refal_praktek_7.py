#Nama: Refal isya' rasya pratama
#No.absen: 23
#Kelas : XI-TKJ 1




# Input informasi pembaruan perangkat lunak
pembaruan_perlukan_restart = input("Apakah pembaruan perangkat lunak memerlukan restart? (ya/tidak): ")

# Memeriksa apakah sistem perlu di-restart
if pembaruan_perlukan_restart.lower() == "ya":
    print("Sistem perlu di-restart.")
else:
    print("Sistem tidak perlu di-restart.")