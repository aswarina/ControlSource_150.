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