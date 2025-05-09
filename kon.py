# Rating film

rating = float(input("Masukkan rating film (0.0 - 10.0): "))

if rating >= 8.5:
    print("Film ini luar biasa! Wajib ditonton.")
elif rating >= 7.0:
    print("Film ini bagus dan layak ditonton.")
elif rating >= 5.0:
    print("Film ini cukup menghibur, tapi tidak terlalu istimewa.")
else:
    print("Film ini kurang memuaskan, cari yang lain saja.")

ulasan = input("Tulis ulasan singkat Anda tentang film ini: ")
print("Terima kasih atas ulasan Anda!")
