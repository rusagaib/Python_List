# inisialiasai
Nm_penyetor=[]

# fungsi print array Nm_penyetor
def zakatfitah(inpNama):
    count=0
    jumTot=len(inpNama)
    print("Data penyetor ", jumTot)
    for i in inpNama:
        print("Data ke - ", count+1, " : ",i)
        count+=1

def inputin(jum):
    for x in range(jum):
        inputan = input("Masukan nama penyetor: ")
        Nm_penyetor.append(inputan)

#main
print("-main-")
jum_input = int(input("Masukkan jumlah penyetor : "))
inputin(jum_input)
print("-end_of_main-")

#after main/main tambahan proses ,
#biasanya digunakan sebagai tambahan proses saat kita pakai class atau di web-apps flask dsb
if __name__ == "__main__":
    print("--tambahan-process--")
    print(Nm_penyetor) #<-pindah baris ke-22 atau dicopas biar terlihat bedanya..
    zakatfitah(Nm_penyetor) #<- atau yang ini..
