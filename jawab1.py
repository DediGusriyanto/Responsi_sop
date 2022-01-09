print("-"*25)
print("Dedi Gusriyanto")
print("5200411059")
print("-"*25)

print("=========RESPONSI SOP_V==========")

kapasitas = int(input("kapasitas total ram: "))
total = int(input("total kapasitas: "))
operasi = int(input("kapasitas ram yang digunakan oleh sistem operasi: "))
program1 = int(input("kapasitas ram yang digunakan oleh program 1: "))
program2 = int(input("kapasitas ram yang digunakan oleh program 2: "))

hitung2 = total-kapasitas
hitung = operasi + program1 + program2
hitung1 = kapasitas - hitung
hitung3 = kapasitas/total
hitung4 = kapasitas - hitung2

print("========HASIL==========")
print("total ram: " , kapasitas)
print("total petabit: " , total)
print("kapasitas per petabit: " , hitung2)

print("-"*20)
print("total ram yang terpakai: " , hitung)
print("total ram yang tidak terpakai: " , hitung1)

print("-"*20)
print("jumlah blok yang bernilai 1:", hitung3)
print("jumlah blok yang bernilai 0:", hitung4)