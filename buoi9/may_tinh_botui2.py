import tkinter as tk
import math

class CasioCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Casio fx-750 Simulator")
        self.root.resizable(False, False)
        self.root.configure(bg="#2d3436")

        self.bieu_thuc = ""

        # --- MÀN HÌNH HIỂN THỊ (2 DÒNG) ---
        khung_man_hinh = tk.Frame(root, bg="#dff9fb", bd=6, relief=tk.SUNKEN)
        khung_man_hinh.pack(padx=12, pady=12, fill="x")

        # Dòng 1: Biểu thức nhập vào
        self.man_hinh_bieu_thuc = tk.Label(
            khung_man_hinh, text="", font=("Consolas", 14),
            anchor="e", bg="#dff9fb", fg="#636e72"
        )
        self.man_hinh_bieu_thuc.pack(fill="x", padx=6, pady=2)

        # Dòng 2: Kết quả tính toán
        self.man_hinh_ket_qua = tk.Label(
            khung_man_hinh, text="0", font=("Consolas", 22, "bold"),
            anchor="e", bg="#dff9fb", fg="#2d3436"
        )
        self.man_hinh_ket_qua.pack(fill="x", padx=6, pady=2)

        # --- KHUNG BÀN PHÍM ---
        khung_phim = tk.Frame(root, bg="#2d3436")
        khung_phim.pack(padx=10, pady=8)

        # Bố cục nút bấm: (Ký tự hiển thị, Hàng, Cột, Màu nền)
        nut_list = [
            # Hàng phím chức năng khoa học 1
            ('sin', 0, 0, '#636e72'), ('cos', 0, 1, '#636e72'), ('tan', 0, 2, '#636e72'), ('log', 0, 3, '#636e72'), ('ln', 0, 4, '#636e72'),
            # Hàng phím chức năng khoa học 2
            ('x²', 1, 0, '#636e72'), ('xʸ', 1, 1, '#636e72'), ('√', 1, 2, '#636e72'), ('x!', 1, 3, '#636e72'), ('π', 1, 4, '#636e72'),
            # Hàng phím số & điều khiển
            ('(', 2, 0, '#636e72'), (')', 2, 1, '#636e72'), ('DEL', 2, 2, '#d63031'), ('AC', 2, 3, '#d63031'), ('e', 2, 4, '#636e72'),
            ('7', 3, 0, '#b2bec3'), ('8', 3, 1, '#b2bec3'), ('9', 3, 2, '#b2bec3'), ('/', 3, 3, '#0984e3'), ('%', 3, 4, '#0984e3'),
            ('4', 4, 0, '#b2bec3'), ('5', 4, 1, '#b2bec3'), ('6', 4, 2, '#b2bec3'), ('*', 4, 3, '#0984e3'), ('1/x', 4, 4, '#0984e3'),
            ('1', 5, 0, '#b2bec3'), ('2', 5, 1, '#b2bec3'), ('3', 5, 2, '#b2bec3'), ('-', 5, 3, '#0984e3'), ('Ans', 5, 4, '#00cec9'),
            ('0', 6, 0, '#b2bec3'), ('.', 6, 1, '#b2bec3'), ('+/-', 6, 2, '#b2bec3'), ('+', 6, 3, '#0984e3'), ('=', 6, 4, '#00b894')
        ]

        self.ans = "0"

        for (text, hang, cot, mau_nen) in nut_list:
            btn = tk.Button(
                khung_phim, text=text, width=5, height=2,
                font=("Arial", 11, "bold"), bg=mau_nen, fg="white" if mau_nen != '#b2bec3' else '#2d3436',
                relief=tk.RAISED, bd=2,
                command=lambda t=text: self.xu_ly_bam_nut(t)
            )
            btn.grid(row=hang, column=cot, padx=3, pady=3)

    def cap_nhat_man_hinh(self):
        self.man_hinh_bieu_thuc.config(text=self.bieu_thuc)

    def xu_ly_bam_nut(self, text):
        if text == "AC":
            self.bieu_thuc = ""
            self.man_hinh_ket_qua.config(text="0")
            self.cap_nhat_man_hinh()

        elif text == "DEL":
            self.bieu_thuc = self.bieu_thuc[:-1]
            self.cap_nhat_man_hinh()

        elif text == "Ans":
            self.bieu_thuc += self.ans
            self.cap_nhat_man_hinh()

        elif text == "=":
            self.tinh_ket_qua()

        elif text == "sin":
            self.bieu_thuc += "sin("
            self.cap_nhat_man_hinh()
        elif text == "cos":
            self.bieu_thuc += "cos("
            self.cap_nhat_man_hinh()
        elif text == "tan":
            self.bieu_thuc += "tan("
            self.cap_nhat_man_hinh()
        elif text == "log":
            self.bieu_thuc += "log10("
            self.cap_nhat_man_hinh()
        elif text == "ln":
            self.bieu_thuc += "log("
            self.cap_nhat_man_hinh()
        elif text == "√":
            self.bieu_thuc += "sqrt("
            self.cap_nhat_man_hinh()
        elif text == "x²":
            self.bieu_thuc += "**2"
            self.cap_nhat_man_hinh()
        elif text == "xʸ":
            self.bieu_thuc += "**"
            self.cap_nhat_man_hinh()
        elif text == "x!":
            self.bieu_thuc += "factorial("
            self.cap_nhat_man_hinh()
        elif text == "π":
            self.bieu_thuc += str(math.pi)
            self.cap_nhat_man_hinh()
        elif text == "e":
            self.bieu_thuc += str(math.e)
            self.cap_nhat_man_hinh()
        elif text == "1/x":
            self.bieu_thuc = f"1/({self.bieu_thuc})" if self.bieu_thuc else "1/"
            self.cap_nhat_man_hinh()
        elif text == "+/-":
            if self.bieu_thuc and self.bieu_thuc[0] == "-":
                self.bieu_thuc = self.bieu_thuc[1:]
            else:
                self.bieu_thuc = "-" + self.bieu_thuc
            self.cap_nhat_man_hinh()
        else:
            self.bieu_thuc += str(text)
            self.cap_nhat_man_hinh()

    def tinh_ket_qua(self):
        if not self.bieu_thuc:
            return

        # Tạo không gian tên an toàn chứa các hàm toán học
        safe_dict = {
            'sin': lambda x: math.sin(math.radians(x)),  # Mặc định góc độ (Degree) chuẩn Casio
            'cos': lambda x: math.cos(math.radians(x)),
            'tan': lambda x: math.tan(math.radians(x)),
            'sqrt': math.sqrt,
            'log': math.log,        # ln (log tự nhiên)
            'log10': math.log10,    # log cơ số 10
            'factorial': lambda x: math.factorial(int(x)),
            'pi': math.pi,
            'e': math.e
        }

        try:
            # Tính toán biểu thức
            ket_qua = eval(self.bieu_thuc, {"__builtins__": None}, safe_dict)
            
            # Làm tròn số thập phân để tránh lỗi hiển thị dấu phẩy động
            if isinstance(ket_qua, float):
                ket_qua = round(ket_qua, 10)
                if ket_qua.is_integer():
                    ket_qua = int(ket_qua)

            self.ans = str(ket_qua)
            self.man_hinh_ket_qua.config(text=str(ket_qua))
        except ZeroDivisionError:
            self.man_hinh_ket_qua.config(text="Math ERROR (Chia 0)")
        except ValueError:
            self.man_hinh_ket_qua.config(text="Math ERROR")
        except SyntaxError:
            self.man_hinh_ket_qua.config(text="Syntax ERROR")
        except Exception:
            self.man_hinh_ket_qua.config(text="ERROR")


if __name__ == "__main__":
    root = tk.Tk()
    app = CasioCalculator(root)
    root.mainloop()