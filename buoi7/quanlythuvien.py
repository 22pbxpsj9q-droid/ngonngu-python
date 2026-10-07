danh_sach_sach = []
lich_su_muon_tra = []

def hien_thi_danh_sach_sach():
    if len(danh_sach_sach) == 0:
        print("-> Danh sach sach hien dang trong.")
        return
    print("\n" + "=" * 65)
    print(f"{'Ma sach':<10}{'Ten sach':<20}{'The loai':<15}{'Gia/ngay':<10}{'Trang thai':<12}{'Nguoi muon':<15}")
    print("-" * 65)
    for sach in danh_sach_sach:
        print(f"{sach['ma_sach']:<10}{sach['ten_sach']:<20}{sach['the_loai']:<15}{sach['gia_thue']:>8,} "
              f"{sach['trang_thai']:<12}{sach['nguoi_muon']:<15}")
    print("=" * 65)

def tim_sach_theo_ma(ma_sach):
    for sach in danh_sach_sach:
        if sach["ma_sach"] == ma_sach:
            return sach
    return None

def xem_sach_co_san():
    sach_co_san = [sach for sach in danh_sach_sach if sach["trang_thai"] == "Co san"]
    if len(sach_co_san) == 0:
        print("-> Hien khong co cuon sach nao co san.")
        return
    print("\nCAC SACH DANG CO SAN:")
    for sach in sach_co_san:
        print(f"  {sach['ma_sach']} - {sach['ten_sach']} ({sach['the_loai']}) - {sach['gia_thue']:,} VND/ngay")

def them_sach(ma_sach, ten_sach, the_loai, gia_thue):
    if tim_sach_theo_ma(ma_sach) is not None:
        print(f"-> Ma sach {ma_sach} da ton tai, khong the them.")
        return
    danh_sach_sach.append({
        "ma_sach": ma_sach,
        "ten_sach": ten_sach,
        "the_loai": the_loai,
        "gia_thue": gia_thue,
        "trang_thai": "Co san",
        "nguoi_muon": ""
    })
    print(f"-> Da them sach '{ten_sach}' ({ma_sach}) thanh cong.")

def muon_sach(ma_sach, ten_nguoi_muon):
    sach = tim_sach_theo_ma(ma_sach)
    if sach is None:
        print(f"-> Khong tim thay sach co ma {ma_sach}.")
        return
    if sach["trang_thai"] == "Dang muon":
        print(f"-> Sach {ma_sach} da duoc muon boi nguoi khac.")
        return
    sach["trang_thai"] = "Dang muon"
    sach["nguoi_muon"] = ten_nguoi_muon
    print(f"-> Cho doc gia {ten_nguoi_muon} muon sach {ma_sach} thanh cong.")

def tra_sach(ma_sach, so_ngay):
    sach = tim_sach_theo_ma(ma_sach)
    if sach is None:
        print(f"-> Khong tim thay sach co ma {ma_sach}.")
        return
    if sach["trang_thai"] == "Co san":
        print(f"-> Sach {ma_sach} dang co san tai thu vien, khong can tra.")
        return
    thanh_tien = sach["gia_thue"] * so_ngay
    lich_su_muon_tra.append({
        "ma_sach": ma_sach,
        "ten_sach": sach["ten_sach"],
        "nguoi_muon": sach["nguoi_muon"],
        "so_ngay": so_ngay,
        "thanh_tien": thanh_tien
    })
    print(f"-> Doc gia {sach['nguoi_muon']} tra sach '{sach['ten_sach']}' sau {so_ngay} ngay.")
    print(f"-> Tong tien phi thue sach: {thanh_tien:,} VND")
    sach["trang_thai"] = "Co san"
    sach["nguoi_muon"] = ""

def thong_ke_doanh_thu():
    if len(lich_su_muon_tra) == 0:
        print("-> Chua co giao dich tra sach nao.")
        return
    tong_tien = 0
    print("\nLICH SU GIAO DICH MUON / TRA SACH:")
    for gd in lich_su_muon_tra:
        print(f"  {gd['ma_sach']} - {gd['ten_sach']} | Doc gia: {gd['nguoi_muon']} - {gd['so_ngay']} ngay - {gd['thanh_tien']:,} VND")
        tong_tien += gd["thanh_tien"]
    print(f"\n>>> TONG DOANH THU THU VIEN: {tong_tien:,} VND")

def nhap_so_nguyen(loi_nhac):
    while True:
        try:
            return int(input(loi_nhac))
        except ValueError:
            print("-> Du lieu khong hop le, vui long nhap lai mot so nguyen.")

def hien_thi_menu():
    print("\n===== HE THONG QUAN LY THU VIEN SACH =====")
    print("1. Hien thi danh sach tat ca sach")
    print("2. Xem cac sach dang co san")
    print("3. Them sach moi")
    print("4. Muon sach")
    print("5. Tra sach / Thanh toan phi")
    print("6. Thong ke doanh thu cho muon")
    print("0. Thoat chuong trinh")

def chay_chuong_trinh():
    while True:
        hien_thi_menu()
        lua_chon = input("Nhap lua chon cua ban: ").strip()
        if lua_chon == "1":
            hien_thi_danh_sach_sach()
        elif lua_chon == "2":
            xem_sach_co_san()
        elif lua_chon == "3":
            ma_sach = input("Nhap ma sach moi: ").strip().upper()
            ten_sach = input("Nhap ten sach: ").strip().title()
            the_loai = input("Nhap the loai sach: ").strip().title()
            gia_thue = nhap_so_nguyen("Nhap gia thue/ngay: ")
            them_sach(ma_sach, ten_sach, the_loai, gia_thue)
        elif lua_chon == "4":
            ma_sach = input("Nhap ma sach can muon: ").strip().upper()
            ten_nguoi_muon = input("Nhap ten nguoi muon: ").strip().title()
            muon_sach(ma_sach, ten_nguoi_muon)
        elif lua_chon == "5":
            ma_sach = input("Nhap ma sach can tra: ").strip().upper()
            so_ngay = nhap_so_nguyen("Nhap so ngay da muon: ")
            tra_sach(ma_sach, so_ngay)
        elif lua_chon == "6":
            thong_ke_doanh_thu()
        elif lua_chon == "0":
            print("Cam on ban da su dung chuong trinh. Tam biet!")
            break
        else:
            print("-> Lua chon khong hop le, vui long chon lai.")

if __name__ == "__main__":
    chay_chuong_trinh()