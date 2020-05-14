# List
int_list = [1, 2, 3]
string_list = ['danil', 'syah']
empty_list = []
mixed_list = [1, 'abc', True, 2.34, None]
nested_list = [['a','b','c'], [1, 2, 3]]
print(int_list)
print(string_list)
print(empty_list)
print(mixed_list)
print(nested_list)

names = ['Danil','Khalinda','Fika','Haykal']
print(names[2])
print(names[1])
print(names[-1])
print(names[-3])
print(names)
names[0] = 'rizal'
print(names)

names.append("icih") # menambahkan data ke list ke akhir list
print(names)

names.insert(2, "udin") #menambahkan data ke list seusai index yang di inginkan
print(names)

names.remove("udin") # menghapus data list sesuai dengan object yang di input
print(names)
print("fika berada pada index ke ", names.index("Fika")) # get index dalam list sesuai object yang di input

# menghitung jumlah item yang sama dalam list
a = [1, 1, 1, 1, 3, 4, 2]
print(a)
print("jumlah 1 dalam list : ", a.count(1))
print(a[::-1]) #menampilkan list dari kanan

# menghapus data pada index trakhir dan mengembalikan index yang terhapus 
print(names)
print(names.pop())
print(names)

for name in names:
    print(name)

