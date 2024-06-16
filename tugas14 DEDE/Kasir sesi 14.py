print("DEDE MAULANA")
print("20230040012")
print("Sesi 14 Dasar Pemograman")

barang = input("masukan nama barang :")
harga = int(input("masukan harga :"))
jumlah_barang = int(input("masukan jumlah barang :"))

text = f'''=== Nota Pembelian ===
barang : {barang}
harga : {harga}
jumlah_barang : {jumlah_barang}
total : {harga * jumlah_barang}
'''
file = open('nota.txt', 'a')
file.write(text)
file.close
