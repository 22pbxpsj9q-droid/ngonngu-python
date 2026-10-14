#hoat dong 4
#4.1
toa_do = (3, 5)
print(toa_do, type(toa_do))

#4.2
x, y = toa_do
print("x =", x, "- y =", y)
a, b = 10, 20
a, b = b, a
print("a =", a, "- b =", b)

#4.3
c, d = 17, 5
thuong_du = divmod(c, d)
thuong, du = thuong_du
print(f"{c} chia {d} duoc thuong {thuong}, du {du}")

#hoat dong 5
import math

diem_a = (2, 3)
diem_b = (7, 8)

xa, ya = diem_a
xb, yb = diem_b

khoang_cach = math.sqrt((xb - xa) * 2 + (yb - ya) * 2)
print(f"Khoang cach giua {diem_a} va {diem_b} la: {round(khoang_cach, 2)}")

#bo sung
cac_diem = [(0, 0), (3, 4), (6, 8)]

for diem in cac_diem:
    x, y = diem
    kc = math.sqrt(x**2 + y**2)
    print(f"Khoang cach tu diem {diem} toi goc toa do (0, 0) la: {round(kc, 2)}")