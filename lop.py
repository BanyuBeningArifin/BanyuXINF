# While Loop
print("=== WHILE LOOP ===")
angka = int(input("Masukkan perulangan (while): "))
i = 1
while i <= angka:
    print("Perulangan ke-", i)
    i += 1

# For Loop
print("\n=== FOR LOOP ===")
batas = int(input("Masukkan Juara (for): "))
for i in range(1, batas + 1):
    print("Juara ke-", i)

# Nested loop
print("\n=== NESTED LOOP ===")
baris = int(input("Masukkan jumlah baris: "))
kolom = int(input("Masukkan jumlah kolom: "))
for i in range(baris):
    for j in range(kolom):
        print(f"({i},{j})", end=" ")
    print()  