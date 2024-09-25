import tkinter as tk
from tkinter import messagebox

def calculate_rectangle():
    try:
        # รับค่าความยาวและความกว้างจาก input
        length = float(entry_length.get())
        width = float(entry_width.get())
        
        # คำนวณพื้นที่และเส้นรอบรูป (ผลลัพธ์เป็นจำนวนเต็ม)
        area = int(length * width)
        perimeter = int(2 * (length + width))
        
        # แสดงผลลัพธ์ใน messagebox
        result_message = f"พื้นที่: {area} ตารางเมตร\nเส้นรอบรูป: {perimeter} เมตร"
        messagebox.showinfo("ผลลัพธ์", result_message)
    except ValueError:
        messagebox.showerror("ข้อผิดพลาด", "กรุณาใส่ตัวเลขที่ถูกต้อง")

# สร้างหน้าต่างหลัก
root = tk.Tk()
root.title("คำนวณสี่เหลี่ยมผืนผ้า")

# ป้ายและช่องกรอกข้อมูลความยาว
label_length = tk.Label(root, text="ความยาว (เมตร):")
label_length.grid(row=0, column=0, padx=10, pady=10)

entry_length = tk.Entry(root)
entry_length.grid(row=0, column=1, padx=10, pady=10)

# ป้ายและช่องกรอกข้อมูลความกว้าง
label_width = tk.Label(root, text="ความกว้าง (เมตร):")
label_width.grid(row=1, column=0, padx=10, pady=10)

entry_width = tk.Entry(root)
entry_width.grid(row=1, column=1, padx=10, pady=10)

# ปุ่มคำนวณ
calculate_button = tk.Button(root, text="คำนวณ", command=calculate_rectangle)
calculate_button.grid(row=2, columnspan=2, pady=20)

# รันโปรแกรม
root.mainloop()
