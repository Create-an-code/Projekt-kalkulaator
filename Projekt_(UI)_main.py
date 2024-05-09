import tkinter
import customtkinter
import UI_valuutakalkulaator
import UI_Intressikalkulaator

#loome akna
aken = tkinter.Tk()
aken.geometry("400x300")
aken.title("Kalkulaator")

# defineerime funktsiooni, mis defineerib comboboxi vastavad valikud
def valuuta_voi_intress_valik(values):
    valuuta_voi_intress_combobox.get()
    # kui comboboxi väärtus on "Valuutakalkulaator" ehk kasutaja valis Valuutakalkulaatori, siis 
    # avame Valuutakalkulaatori TKinteri akna ning selle TKinteri akna suleme
    if valuuta_voi_intress_combobox.get() == "Valuutakalkulaator":
        aken.destroy()
        UI_valuutakalkulaator.run()
    # kui comboboxi väärtus on "Intressikalkulaator" ehk kasutaja valis Intressikalkulaatori, siis
    # avame Intressikalkulaatori TKinteri akna ning selle TKinteri akna suleme
    if valuuta_voi_intress_combobox.get() == "Intressikalkulaator":
        aken.destroy()
        UI_Intressikalkulaator.run()


#fondi valimine, valisime Helvetica fondi
font1 = customtkinter.CTkFont(family="Helvetica", size=16, weight="bold")

# Raami loomine
raam = customtkinter.CTkFrame(master=aken,
                               width=300,
                               height=200,
                               corner_radius=10)
raam.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

# Pealkirja sildi loomine
pealkiri_silt = customtkinter.CTkLabel(master=aken,
                               text="Kalkulaatori valik",
                               width=120,
                               height=25,
                               corner_radius=8,font=font1)
pealkiri_silt.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)

#Küsib kasutajalt, kas ta soovib valuutakalkulaatorit või intressikalkulaatorit
valuuta_voi_intress_combobox = customtkinter.CTkComboBox(master=raam,
                                             values=["Valuutakalkulaator", "Intressikalkulaator"], width=170,
                                             command=valuuta_voi_intress_valik)
valuuta_voi_intress_combobox.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
valuuta_voi_intress_combobox.set("")
valuuta_voi_intress_combobox_silt = customtkinter.CTkLabel(master=raam,
                                    text="Valige, millist kalkulaatorit soovite: ",
                                    width=120,
                                    height=25,
                                    corner_radius=8, font=customtkinter.CTkFont(family="Helvetica", size=14))
valuuta_voi_intress_combobox_silt.place(relx=0.5, rely=0.35, anchor=tkinter.CENTER)

aken.mainloop()