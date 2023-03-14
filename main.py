import tkinter as tk

class Calculator:

    def __init__(self, master):
        self.master = master
        master.title("PyCalculator")

        #Text Header
        self.label = tk.Label(master, text="Harap Masukkan 2 Angka dan Pilihlah Operasi.")

        self.label.grid(row=0, column=0, columnspan=4)

        #Input Pertama
        self.input1 = tk.Entry(master)
        self.input1.grid(row=1, column=0, columnspan=2)

        #Input Kedua
        self.input2 = tk.Entry(master)
        self.input2.grid(row=1, column=2, columnspan=2)

        #Tombol Tambah
        self.tambah = tk.Button(master, text="+", command=self.tambah)
        self.tambah.grid(row=2, column=0)

        #Tombol Kurangi
        self.kurangi = tk.Button(master, text="-", command=self.kurangi)
        self.kurangi.grid(row=2, column=1)

        #Tombol Kali
        self.kali = tk.Button(master, text="*", command=self.kali)
        self.kali.grid(row=2, column=2)

        #Tombol Bagi
        self.bagi = tk.Button(master, text="/", command=self.bagi)
        self.bagi.grid(row=2, column=3)

        #Output hasil
        self.label_hasil = tk.Label(master, text="")
        self.label_hasil.grid(row=3, column=0, columnspan=4)

    def tambah(self):

        no1 = int(self.input1.get())
        no2 = int(self.input2.get())

        hasil = no1 + no2

        self.label_hasil.configure(text = hasil )

    def kurangi(self):

        no1 = int(self.input1.get())
        no2 = int(self.input2.get())

        hasil = no1 - no2
        self.label_hasil.configure(text = hasil)

    def kali(self):

        no1 = int(self.input1.get())
        no2 = int(self.input2.get())

        hasil = no1 * no2
        self.label_hasil.configure(text = hasil)

    def bagi(self):

        num1 = int(self.input1.get())
        num2 = int(self.input2.get())

        hasil = num1 / num2
        self.label_hasil.configure(text = hasil)

root = tk.Tk()
my_calculator = Calculator(root)
root.mainloop()
