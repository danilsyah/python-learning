def penjumlahan(nilai_a = 0, nilai_b = 0):
    jumlah = nilai_a + nilai_b
    print(f"{nilai_a} + {nilai_b} = {jumlah} ")

def say_hello(first_name = "danil", last_name ="syah"):
    print(f"hello {first_name} - {last_name}")

penjumlahan(2,1)
first_name = input("masukan nama depan = ")
last_name = input("masukan nama belakang = ")
say_hello(first_name, last_name)
say_hello(last_name=last_name)
say_hello(last_name = "dafiansyah", first_name="haykal")