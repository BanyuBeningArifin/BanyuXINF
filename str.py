# Mengupdate String

# Contoh 1
message = 'Hello'
print('Sebelum Update =', message)

message = message + ' Banyu'
print('Sesudah Update =', message)

# Contoh 2
nama = 'Bagus Mas'
print('sebelum =', nama)

nama_lengkap = nama[:5] + ' Satya ' + nama[6:]
print('sesudah =', nama_lengkap)

# Contoh 3
x = nama[6:] + " " + nama[:5]
print('kombinasi baru =', x)
