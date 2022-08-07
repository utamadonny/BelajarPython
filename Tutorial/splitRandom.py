# from numpy import random

# tujuan_uang = 3_000_000
# print(random.uniform(200_000,300_000))
# x=random.normal(100, size=(4))

# print(x) 
# def random_num():
# 	return random.choice([100_000,125_000, 200_000, 250_000, 50_000,500_000,75_000,35_000,400_000,65_000,145_000,365_000,300_000])

# x = 0
# uang_yang_harus_ditabung = []
# for i in range(12):
# 	x += random_num()
# 	uang_yang_harus_ditabung.append(x)
# 	print(f"Uang yang ditabungkan {i+1} = {x}")
# 	if x >= tujuan_uang:
# 		break

# while x < tujuan_uang:
# 	x += random_num
# 	uang_yang_ditabung.append(random_num)
# 	print(f"Sisa uang {x}")
# 	random_num = random.choice([100_000,125_000, 200_000, 250_000, 50_000, 75_000,35_000,400_000,65_000,145_000,365_000, 300_000])
# 	if x >= tujuan_uang:
# 		print(f"Sisa uang {x}")
# 		print(f"Uang terkumpul {tujuan_uang}")
# 		print(f"Uang yang ditabung {uang_yang_ditabung}")

# while x < tujuan_uang:
# 	for i in range(12):
# 		x += random_num
# 		uang_yang_harus_ditabung.append(random_num)
# 		print(f"Sisa uang {x}")
# 		random_num()
# 		if x >= tujuan_uang:
# 			print(f"Sisa uang {x}")
# 			print(f"Uang terkumpul {tujuan_uang}")
# 			print(f"Uang yang ditabung {uang_yang_ditabung}")

import numpy as np
tujuan = 3_000_000
uang_yang_harus_ditabung = []
waktu = 52

rata_rata = tujuan/waktu
# print(f'rata rata {rata_rata}')
x= np.zeros(100)
while x.sum()<tujuan:
	x=np.random.randint(rata_rata-rata_rata/2,rata_rata+rata_rata/2,size=(waktu))
print(f'list random {x}')
print(f'rata rata {x.mean():_}')
print(f'jumlah {x.sum():_}')


