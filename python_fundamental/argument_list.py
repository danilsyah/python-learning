def jumlahkan(*list_angka):
    total = 0
    for angka in list_angka:
        total = total + angka
    print(f"Total {list_angka} = {total}")
    return (list_angka, total)

total = jumlahkan(10,10)
print(total)