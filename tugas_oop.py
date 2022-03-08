from abc import abstractmethod, ABC

class Mahasiswa:
    '''Dasar kelas untuk semua karyawan'''
    jumlah_mhs = 0

    def __init__(self, namanya, mhs):
        self.namanya = namanya
        self.mhs = mhs
        Mahasiswa.jumlah_mhs += 1

    def jumlah(self):
        print("")
        print("Jumlah Mahasiswa :",Mahasiswa.jumlah_mhs)
    
    def profil(self):
        print("Nama Mahasiswa :",self.namanya)
        print("Universitas",self.mhs)
        print("")
       

 # Membuat objek pertama dari kelas Karyawan
mahasiswa1 = Mahasiswa("Ilyas Dinar Lokajaya","Yarsi")
# Membuat objek kedua dari kelas Karyawan
mahasiswa2 = Mahasiswa("Shakila Ratu Pratiwi","Indonesia")
    
#Function
def rank(jam):
        if (jam>=12) : # angka 12 menunjukkan pukul 12 Malam
            print("ga lah males udah malem!")
        else:
            print("Push rank kuy!")

    
def perkalian():
    a = 7 
    c = a * 3
    return c

def perpangkatan():
    x = 5
    x **= 3
    return x
                                                           # SENIN 7 MARET 2022
                                                           # SESI PAGI