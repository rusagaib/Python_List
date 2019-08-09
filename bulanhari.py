#! /usr/bin/latian/bulanhari.py
print("Program bulan hari")

th = int(input("Input tahun berapa sekarang :"))

print ("""
      1 = januari     7 = juli
      2 = februari    8 = agustus
      3 = maret       9 = september
      4 = april       10 = oktober
      5 = mei         11 = november
      6 = juni        12 = desember
""")
bln1 = (1,3,5,7,9,11)
bln2 = (4,6,8,10,12)
bln3 = (2)
bln = int(input("Input bulan :"))

if th % 4 == 0 :
  print (th," adalah tahun Kabisatt\n\nBulan yang anda masukkan adalah :")
  if bln in bln1:
    print ("31 hari")
  elif bln in bln2 :
    print ("30 hari")
  else: print ("29 hari")

else:
  print (th,"bukan tahun kabisat\n\nBulan yang anda masukkan adalah :",bln)
  if bln in bln1:
    print ("31 hari")
  elif bln in bln2:
    print ("30 hari")
  else:
    print ("28 hari")
print ("\n\nTerimakasihhh.....")
