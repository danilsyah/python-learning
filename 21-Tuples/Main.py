# tuple : data tidak bisa di ubah , dihapus, ditambah dan proses pengolahan stuktur data tuple lebih cepat dari , list

# list
Ganjil = [1, 2, 3, 4, 5, 5]

# tuple
Genap = (2, 3, 4, 5, 6, 6)

print(type(Ganjil))
print(type(Genap))

# # mengganti nilai member
# Ganjil[2] = 99  # bisa
# # Genap[2] = 99  # error

# # menambahkan data
# Ganjil.append(88)
# # Genap.append(88) #error

# # menghapus data
# Ganjil.remove(99)
# # Genap.remove(2) #error

# print(dir(Ganjil))
# print(dir(Genap))

print(Genap.count(6))
print(Ganjil.count(5))
