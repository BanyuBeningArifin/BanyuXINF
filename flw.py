a = int(input("Nilai a: "))
b = int(input("Nilai b: "))
op = input("Masukkan operator (+, -, *, /): ")

if op == '+':
    hasil = a + b
elif op == '-':
    hasil = a - b
elif op == '*':
    hasil = a * b
elif op == '/':
    if b != 0:
        hasil = a / b
    else:
        hasil = "Tidak bisa dibagi"
else:
    hasil = "Operator tidak dikenali"
    
print("Hasil =", int(hasil))
