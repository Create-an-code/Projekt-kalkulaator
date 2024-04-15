import tkinter
import customtkinter

# Akna loomine
aken = tkinter.Tk()
aken.geometry("400x240")
aken.title("Valuutakalkulaator")

#fondi valimine, valisime Helvetica fondi
font1 = customtkinter.CTkFont(family="Helvetica", size=16, weight="bold")

# Raami loomine
raam = customtkinter.CTkFrame(master=aken,
                               width=200,
                               height=200,
                               corner_radius=10)
raam.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

# Pealkirja sildi loomine valuutakalkulaatori jaoks
pealkiri_silt = customtkinter.CTkLabel(master=aken,
                               text="Valuutakalkulaator",
                               width=120,
                               height=25,
                               corner_radius=8,font=font1)
pealkiri_silt.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)

# Summa sisestamiseks tekstikasti loomine
# Summa, mida soovitakse teisendada
summa_sisend = customtkinter.CTkEntry(master=raam,
                                      width=120,
                                      height=25,
                                      corner_radius=10)
summa_sisend.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)
summa_silt = customtkinter.CTkLabel(master=raam,
                                    text="Sisestage summa:",
                                    width=120,
                                    height=25,
                                    corner_radius=8, font=customtkinter.CTkFont(family="Helvetica", size=14))
summa_silt.place(relx=0.5, rely=0.15, anchor=tkinter.CENTER)

# Valuuta kursi valiku jaoks kastikese loomine
# Valuuta kurss, mida soovitakse teisendada
valuuta_kurss1 = customtkinter.CTkLabel(master=raam,
                                    text="Kurss, mida soovite teisendada: ",
                                    width=25,
                                    height=25,
                                    corner_radius=8, font=customtkinter.CTkFont(family="Helvetica", size=14))
valuuta_kurss1.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
def valuuta_valik(valuuta):
    print("Valisite valuuta kursiks:", valuuta)

valuuta_combobox = customtkinter.CTkComboBox(master=raam,
                                             values=["USD", "EUR", "GBP"],
                                             command=valuuta_valik)
valuuta_combobox.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)
valuuta_combobox.set("USD")

aken.mainloop()