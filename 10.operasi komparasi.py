#operasi komparasi

#setiap hasil dari operasi komparasi adalah boolean

#>,<, >= , <= , == , != , is , is not

a = 4
b = 2
print("YANG BEKERJA PADA SYNTAX LITERAL")
#lebih besar dari >
print("====lebih besar dari >====")
hasil = a > 3
print(a,'>',3,'=',hasil)
hasil = a > 4
print(a,'>',4,'=',hasil)
hasil = a > 2
print(a,'>',2,'=',hasil)

#kurang dari <
print("====lebih besar dari >====")
hasil = a < 3
print(a,'<',3,'=',hasil)
hasil = a < 4
print(a,'<',4,'=',hasil)
hasil = a < 5
print(a,'<',5,'=',hasil)

#lebih dari sama dengan >=
print("====lebih besar sama dengan >= ====")
hasil = a >= 3
print(a,'>=',3,'=',hasil)
hasil = a >= 4
print(a,'>=',4,'=',hasil)
hasil = a >= 5
print(a,'>=',5,'=',hasil)

#kurang dari sama dengan <=
print("====kurang dari sama dengan <= ===")
hasil = a <= 3
print(a,'<=',3,'=',hasil)
hasil = a <= 4
print(a,'<=',4,'=',hasil)
hasil = a <= 5
print(a,'<=',5,'=',hasil)

#sama dengan ==
print("====sama dengan == ====")
hasil = a == 3
print(a,'==',3,'=',hasil)
hasil = a == 4
print(a,'==',4,'=',hasil)
hasil = a == 5
print(a,'==',5,'=',hasil)

#tidak sama dengan !=
print("====tidak sama dengan != ====")
hasil = a != 3
print(a,'!=',3,'=',hasil)
hasil = a != 4
print(a,'!=',4,'=',hasil)
hasil = a != 5
print(a,'!=',5,'=',hasil)

#sama dengan
print("====sama dengan == ====")
hasil = a == 3
print(a,'==',3,'=',hasil)
hasil = a == 4
print(a,'==',4,'=',hasil)
hasil = a == 5
print(a,'==',5,'=',hasil)

print("YANG BEKERJA UNTUK MEMBANDINGKAN MEMORI")
#'is' sebagai komparasi object identity
x = 5 # ini adalah assignment membuat object
y = 5
print('nilai x =',x,'id =',hex(id(x)))
print('nilai y =',y,'id =',hex(id(y)))
hasil = x is y
print('x is y =',hasil)
hasil = x is not y
print('x is not y=',hasil)
