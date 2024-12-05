    #Program Manajemen Kontak

def melihat_kontak():
    # Melihat semua kontak
    if kontak:  # untuk memberitahu user bahwa kontak masih kosong, jika ada sisnya akan membentuk True tapi jika tidak ada nilainya akan menjadi False
        for a, b in enumerate(kontak, start=1):
            # variabel a di gunakan untuk menjadi angka urutannya
            # variabel b untuk memanggil key dari dictionary
            print(f"{a}. {b['Nama']} ({b['No.HP']} {b['Email']})")
    else:
        print("Kontak masih kosong!")
        return 1

def menambah_kontak():
    # Menambahakan kontak baru
    nama = input("Masukan Nama : ")
    nohp = input("Masukan kontak : ")
    email = input("masukan email : ")
    # karena menggunakan konsep dictionary jadi dibuat bentuk dictionary
    # mendiskripsikan variabel baru dengan variabel lama (Key di dictory yg di buat diatas) agar dapat di ubah
    kontak_baru = {'Nama': nama, 'No.HP': nohp, 'Email': email}
    # karna menambah list jadi menggunakan append
    kontak.append(kontak_baru)
    print("Kontak baru berhasil di tambahkan")


def menghapus_kontak():
    # Menghapus Kontak
    # Melihat semua kontak

    if melihat_kontak() == 1:
        return

    # membuat inputan angka untuk menghapus daftar nomor
    # dan menginput angka harus menggunakan tipe data int atau float
    # Layernya tidak di bawah for atau if
    i_hapus = int(input("Masukan nomor yang akan di hapus : "))
    # del di gunakan untuk menghapus variabel, objek maupun di dalam list
    # kenapa (-1) karna datanya di mulai atau di start dari 1
    del kontak[i_hapus - 1]
    print("Kontak Berhasil Di Hapus")



# Program pilihan 1
# menggunakan dictionarry
kontak1 = {'Nama' : 'Andi', 'No.HP' : '08426127190', 'Email' : 'Andry@gmail.com'}
kontak2 = {'Nama' : 'Bayu', 'No.HP' : '08426127188', 'Email' : 'Lukman@gmail.com'}
# bentuk list
kontak = [kontak1,kontak2]



while True:
    print("\n Menu Kontak")
    print("1. Melihat Semua Kontak")
    print("2. Menambahkan kontak baru")
    print("3. Menghapus Kontak")
    print("4. Keluar dari Kontak")

    pilihan = input("Masukan pilihan menu kontak (1,2,3 atau 4): ")

    if pilihan == '1':
        melihat_kontak()


    elif pilihan == '2':
        menambah_kontak()


    elif pilihan == '3':
        menghapus_kontak()


    elif pilihan == '4':
        # Keluar dari kontak
        break
    else:
        print("Anda memasukkan pilihan yang salah!")
