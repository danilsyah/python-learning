banyak = int(input("Berapa banyak data : "))
nama = []
umur = []
i = 0
while i < banyak:
    print(f"data ke {i}")
    input_nama = input("nama : ")
    input_umur = input("umur : ")
    nama.append(input_nama)
    umur.append(input_umur)
    i += 1

for i in range(0, len(nama)):
    data_nama = nama[i]
    data_umur = umur[i]
    print(f"{data_nama} berumur {data_umur}")