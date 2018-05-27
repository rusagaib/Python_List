#! /usr/lib/env python 3.5

data=[]

##fungsi untuk menampilkan data di dalam list
def show_data():
	if len(data) <= 0:
		print("belum ada data..")
	else:
		for indeks in range(len(data)):
			print("[%d] %s" % (indeks,data[indeks]))

##fungsi untuk menambahkan data ke dalam list
def insert_data():
	data_baru=input("Masukkan Data: ")
	data.append(data_baru)

##fungsi untuk menghapus data melalui id data terkait
def delet_data():
	show_data()
	indeks=input("Inputkan ID Data: ")
	if(indeks>len(data)):
		print("ID data terkait salah..")
	else:
		data.remove(data[indeks])

##fungsi untuk mengedit data dalam list
def edit_data():
	show_data()
	indeks=input("Inputkan ID Data: ")
	if(indeks>len(data)):
	 	print("id data Salah..")
	else:
	 	data_baru = input("Data baru: ")
		data[indeks]=data_baru   

##fungsi menampilkan menu utama..
def show_menu():
	print("""\n-------------Menu-------------\n[1] Show Data\n[2] Insert Data\n[3] Delete Data\n[4] Exit\n""")
	menu=input("Pilih Menu: ")
	print("\n")

	if(menu==1):
		show_data()
	elif(menu==2):
		insert_data()
	elif(menu==3):
		delet_data()
	elif(menu==4):
		exit()
	elif(menu==5):
		edit_data()
	else:
		print("Salah Pilih..")

##-----------[default main loop]-------------------##
if __name__ == "__main__":	

	while(True):
		show_menu()
