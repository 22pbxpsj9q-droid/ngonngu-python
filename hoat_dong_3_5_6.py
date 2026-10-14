print("=" * 20, "HOẠT ĐỘNG 3", "=" * 20)

ten = "Nguyen Van A"
diem_toan = 8.5
diem_van = 7.0
so_luong_mon_hoc = 2
MUC_LUONG_TOI_THIEU = 5000000

print(f"Họ tên: {ten}")
print(f"Điểm Toán: {diem_toan} | Điểm Văn: {diem_van}")
print(f"Số lượng môn học: {so_luong_mon_hoc}")
print(f"Mức lương tối thiểu: {MUC_LUONG_TOI_THIEU}\n")


print("=" * 20, "HOẠT ĐỘNG 5", "=" * 20)

a = 17
b = 5
print("--- Bài tập 5.1 ---")
print("a + b  =", a + b)
print("a - b  =", a - b)
print("a * b  =", a * b)
print("a / b  =", a / b)
print("a // b =", a // b)
print("a % b  =", a % b)
print("a * b =", a * b)

diem = 6.5
tuoi = 20
print("\n--- Bài tập 5.2 ---")
dat_loai_kha = (diem >= 6.5) and (diem < 8.0)
print("Điểm có đạt loại Khá?:", dat_loai_kha)

tuoi_chua_du_18_hoac_tren_60 = (tuoi < 18) or (tuoi > 60)
print("Tuổi < 18 hoặc > 60?:", tuoi_chua_du_18_hoac_tren_60)
print("Phủ định điều kiện tuổi (18 <= tuổi <= 60)?:", not tuoi_chua_du_18_hoac_tren_60)

print("\n--- Bài tập 5.3 ---")
x = 10
x += 5
print("x sau += 5  :", x)
x -= 3
print("x sau -= 3  :", x)
x *= 2
print("x sau *= 2  :", x)
x /= 4
print("x sau /= 4  :", x)
x //= 2
print("x sau //= 2 :", x)
x **= 3
print("x sau **= 3 :", x)

danh_sach = [1, 2, 3, "python"]
print("3 có trong danh_sach không? ('in'):", 3 in danh_sach)

list_clone = danh_sach
list_moi = [1, 2, 3, "python"]
print("list_clone is danh_sach:", list_clone is danh_sach)
print("list_moi is danh_sach  :", list_moi is danh_sach)

print("\n--- Bài tập 5.4 ---")
print("2 + 3 * 4 * 2 =", 2 + 3 * 4 * 2)
print("(2 + 3) * 4 * 2 =", (2 + 3) * 4 * 2)
print("10 > 5 and 3 < 1 or not False =", 10 > 5 and 3 < 1 or not False)
print()


print("=" * 20, "HOẠT ĐỘNG 6", "=" * 20)

bien = 10
print(bien, type(bien))

bien = "Xin chao"
print(bien, type(bien))

bien = 3.14
print(bien, type(bien))

bien = True
print(bien, type(bien))

print("\n--- Bài tập 6.2 ---")
ho_ten = "Nguyen Van A"
diem_toan = 8.0
diem_ly = 7.5
diem_hoa = 9.0

dtb = (diem_toan + diem_ly + diem_hoa) / 3

la_gioi = dtb >= 8.0
la_kha = dtb >= 6.5 and dtb < 8.0
la_trung_binh = dtb >= 5.0 and dtb < 6.5
la_yeu = dtb < 5.0

print(ho_ten, "- DTB:", round(dtb, 2))
print("Dat loai Gioi?", la_gioi)
print("Dat loai Kha?", la_kha)
print("Dat loai Trung binh?", la_trung_binh)
print("Dat loai Yeu?", la_yeu)
print("Kieu du lieu cua la_gioi:", type(la_gioi))