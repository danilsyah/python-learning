# list => [] data bisa di tambahkan dan boleh duplikat
# tuple => () data tidak bisa di ubah atau di tambahkan
# set => {} data harus unik tidak boleh ada yang sama datanya, cara pemanggilan elemen harus menggunakan loop

nama = {"Eko","Joko","Eko","Joko","Danil"}
nama.add("syah")
nama.remove("Eko")
print(nama)
for data in nama:
    print(data)