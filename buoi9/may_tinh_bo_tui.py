import tkinter as tk
bieu_thuc = ""

def nut_bam(ky_tu):
    global bieu_thuc
    bieu_thuc = bieu_thuc + str(ky_tu)
    o_nhap.delete(0, tk.END)
    o_nhap.insert(tk.END, bieu_thuc)

def xoa_het():
    global bieu_thuc
    bieu_thuc = ""
    o_nhap.delete(0, tk.END)

def tinh_toan():
    global bieu_thuc
    try:
        # eval() tự động tính giá trị của chuỗi biểu thức số học
        ket_qua = str(eval(bieu_thuc))
        o_nhap.delete(0, tk.END)
        o_nhap.insert(tk.END, ket_qua)
        bieu_thuc = ket_qua  # Cho phép bấm tính tiếp trên kết quả vừa ra
    except ZeroDivisionError:
        o_nhap.delete(0, tk.END)
        o_nhap.insert(tk.END, "Lỗi chia 0")
        bieu_thuc = ""
    except:
        o_nhap.delete(0, tk.END)
        o_nhap.insert(tk.END, "Lỗi cú pháp")
        bieu_thuc = ""

# Khởi tạo cửa sổ chính
cua_so = tk.Tk()
cua_so.title("Máy tính bỏ túi")
cua_so.resizable(False, False)

# Ô Entry hiển thị biểu thức và kết quả
o_nhap = tk.Entry(cua_so, font=("Arial", 18), justify="right", bd=8, relief=tk.RIDGE)
o_nhap.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Danh sách các nút bấm
nut_list = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

# Tạo các nút bấm vào giao diện
for (text, hang, cot) in nut_list:
    if text == "=":
        cmd = tinh_toan
    elif text == "C":
        cmd = xoa_het
    else:
        cmd = lambda t=text: nut_bam(t)
        
    btn = tk.Button(cua_so, text=text, width=5, height=2, font=("Arial", 14), command=cmd)
    btn.grid(row=hang, column=cot, padx=4, pady=4)

# Chạy vòng lặp giao diện
cua_so.mainloop()