import tkinter
import customtkinter
from PIL import Image, ImageTk

# Akna loomine
aken = tkinter.Tk()
aken.geometry("600x500")
aken.title("Valuutakalkulaator")

#fondi valimine, valisime Helvetica fondi
font1 = customtkinter.CTkFont(family="Helvetica", size=16, weight="bold")

# Raami loomine
raam = customtkinter.CTkFrame(master=aken,
                               width=400,
                               height=400,
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
summa_sisend.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)
summa_silt = customtkinter.CTkLabel(master=raam,
                                    text="Sisestage summa:",
                                    width=120,
                                    height=25,
                                    corner_radius=8, font=customtkinter.CTkFont(family="Helvetica", size=14))
summa_silt.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)

#loon ka tulemuse sildi, mis siis annab kasutajale teada, et kas mõni lahter on täitmata või valesti täidetud
tulemus_silt = customtkinter.CTkLabel(master=raam,
                                    text="",
                                    width=120,
                                    height=25,
                                    corner_radius=8, font=customtkinter.CTkFont(family="Helvetica", size=14))
tulemus_silt.place(relx=0.5, rely=0.9, anchor=tkinter.CENTER)

# Valuuta kursi valiku jaoks kastikese loomine
# Valuuta kurss, mida soovitakse teisendada
valuuta_kurss1 = customtkinter.CTkLabel(master=raam,
                                    text="Kurss, mida teisendada: ",
                                    width=25,
                                    height=25,
                                    corner_radius=8, font=customtkinter.CTkFont(family="Helvetica", size=14))
valuuta_kurss1.place(relx=0.5, rely=0.35, anchor=tkinter.CENTER)
def valuuta_valik1(valuuta):
    print("Valisite valuuta kursiks:", valuuta)

valuuta_combobox1 = customtkinter.CTkComboBox(master=raam,
                                             values=["USD", "EUR", "GBP"],
                                             command=valuuta_valik1)
valuuta_combobox1.place(relx=0.5, rely=0.45, anchor=tkinter.CENTER)
valuuta_combobox1.set("")

# Valuuta kursi valiku jaoks kastikese loomine
# Valuuta kurss, milleks soovitakse teisendada ehk kurss, mida soovitakse saada
valuuta_kurss2 = customtkinter.CTkLabel(master=raam,
                                    text="Kurss, milleks teisendada: ",
                                    width=25,
                                    height=25,
                                    corner_radius=8, font=customtkinter.CTkFont(family="Helvetica", size=14))
valuuta_kurss2.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)
def valuuta_valik2(valuuta):
    print("Valisite valuuta kursiks:", valuuta)

valuuta_combobox2 = customtkinter.CTkComboBox(master=raam,
                                             values=["USD", "EUR", "GBP"],
                                             command=valuuta_valik2)
valuuta_combobox2.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)
valuuta_combobox2.set("")

#defineerin nupu väärtuse, mida ma tahan kuvada kasutajale, peale seda, kui ta on vajutanud nupule "Arvuta"
def nupu_väärtus():
    summa = summa_sisend.get()
    try:
        summa = round(float(summa,2))
    except:
#     kuna textbox on alati str type, siis proovime try exceptiga teda muuta floatiks ning 2 komakohta peale koma
#    aga proovime convertida, kui õnnestub, siis prindime kasutajale tühja teate ehk mitte midagi ja kui ei, siis
#    kirjutame kasutajale sõnumina teate, mida kasutaja peab muutma või lisama
        tulemus_silt.configure(text="Palun sisestage summa numbrites", text_color="red")
    if isinstance(summa, int):
        tulemus_silt.configure(text="", text_color="green")
    if valuuta_combobox1.get() == "" or valuuta_combobox2.get() == "":
        tulemus_silt.configure(text="Palun valige valuuta", text_color="red")
    




nupp = customtkinter.CTkButton(master=raam,
                                 width=120,
                                 height=32,
                                 border_width=0,
                                 corner_radius=8,
                                 text="Arvuta",
                                 command=nupu_väärtus)
nupp.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)

# my_image = customtkinter.CTkImage(light_image=Image.open("Valuutakalkulaatori pilt.png"),size=(30, 30))
# img_path = "Valuutakalkulaatori pilt.png"
# img_pil = Image.open(img_path)
# 
# ctk_img = customtkinter.CTkImage(img_pil, size=img_pil.size)
# photo_label = customtkinter.CTkLabel(aken, image=ctk_img)
# photo_label.pack()
# 
# #img = ImageTk.PhotoImage(ctk_img.cget('light_image'))
# img = ImageTk.PhotoImage(img_pil)
# aken.iconphoto(False, img)


aken.mainloop()
