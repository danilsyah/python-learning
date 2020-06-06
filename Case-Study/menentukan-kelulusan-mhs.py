
mahasiswa = []
jumlahMhs = int(input('Input Jumlah Mhs : '))

for j in range(0, jumlahMhs):
    print(" data ke- ", j)
    nama = input("masukan nama :")
    nik = input("masukan nik ")
    mahasiswa.append([nama, nik])

print(mahasiswa)

for i in mahasiswa:
    print(i)


# mhs = [
#     [
#         'danil',
#         3216607,
#         'danilsyah@gmail.com'
#     ],
#     [
#         'haykal',
#         3216608,
#         'haykal@gmail.com'
#     ]
# ]

# print(mhs)
