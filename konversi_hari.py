#! /usr/bin/latian/konversi_hari.py

hari = input('masukkan hari: ')
print('----------------------------------')
t = hari / 365          #t = tahun
sh = hari % 365         #sh = sebagai nilai sementara untuk menampung sisa hari dalam setahunya...
b = sh / 30             #b = bulan (contoh input=480 >> 1thn, (480 % 365)/30= 115 / 30= 3 bulan )
h = sh % 30             #h = hari (contoh input=480 >> 1thn, 3bln, (480 % 365)%30= 115 % 30= 25 hari)
print(t, 'tahun', b,'bulan', h,'hari')       #contoh input=480 >> 1thn, 3bln, 25hari..
