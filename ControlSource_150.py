nilai = int(input("masukkan nilai: "))

if nilai >= 90:
    print ("exellent")
elif nilai >= 80:
    print("very good")
elif nilai >= 70:
    print("good")        
elif nilai >= 60:
    print("avrage") 
else:
    print(" so poor")


##2
num1 = int(input("Masukkan angka pertama: "))
num2 = int(input("Masukkan angka kedua: "))
num3 = int(input("Masukkan angka ketiga: "))

#  percabangan untuk menentukan angka terbesar
if num1 >= num2 and num1 >= num3:
    terbesar = num1
elif num2 >= num1 and num2 >= num3:
    terbesar = num2
else:
    terbesar = num3
print(f"Angka terbesar di antara {num1}, {num2}, dan {num3} adalah: {terbesar}")

###3
n = int(input("Masukkan nilai n untuk Fibonacci: "))
a, b = 0, 1

print("Deret Fibonacci:")
while a <= n:
    print(a, end=" ")
    a, b = b, a + b
print()

##4
n = int(input("Masukkan nilai n untuk angka ganjil: "))

print("Angka ganjil:")
for i in range(1, n + 1, 2):
    print(i, end=" ")
print()