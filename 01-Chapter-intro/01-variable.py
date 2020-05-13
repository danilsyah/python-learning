# ==== belajar variable dan tipe data primitif ====

angka = 10 #int
pecahan = 3.14 #float
nama = 'danil syah' #string
logic = True #bool

print(angka, " type = ", type(angka))
print(pecahan, " type = ", type(pecahan))
print(nama, " type = ", type(nama))
print(logic, " type = ", type(logic))

# assign multiple value
a,b,c = 1,2,3
print(a,c,b)

a,b,_ = 2,1,6
print(a,_,b)

a = b = c = 1
print(a,b,c)
b = 2
print(a,b,c)