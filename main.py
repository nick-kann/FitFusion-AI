import customtkinter as ctk
from pushup import start as wk

ctk.set_appearance_mode("dark")

root = ctk.CTk()
root.geometry("500x300")

def test():
    print("meow")


frame = ctk.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = ctk.CTkLabel(master=frame, text="meowmewom")
label.pack(pady=12, padx=10)

butt = ctk.CTkButton(master=frame, command=wk, text="click me for love")
butt.pack(pady=22, padx=10)

root.mainloop()
