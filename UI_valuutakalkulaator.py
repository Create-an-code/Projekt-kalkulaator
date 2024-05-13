import tkinter
import customtkinter
import kalk_kood

def run():
    
    valuuta_list = kalk_kood.show_cur()

    # Akna loomine
    valuuta_aken = tkinter.Tk()
    valuuta_aken.geometry("600x400")
    valuuta_aken.title("Valuutakalkulaator")

    #fondi valimine, valisime Helvetica fondi
    font1 = customtkinter.CTkFont(family="Helvetica", size=16, weight="bold")

    # Raami loomine
    raam = customtkinter.CTkFrame(master=valuuta_aken,
                                   width=500,
                                   height=300,
                                   corner_radius=10)
    raam.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    # Pealkirja sildi loomine valuutakalkulaatori jaoks
    pealkiri_silt = customtkinter.CTkLabel(master=valuuta_aken,
                                   text="Valuutakalkulaator",
                                   width=120,
                                   height=25,
                                   corner_radius=8,font=font1)
    pealkiri_silt.place(relx=0.5, rely=0.15, anchor=tkinter.CENTER)
    
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
    summa_silt.place(relx=0.5, rely=0.12, anchor=tkinter.CENTER)

    # Valuuta kursi valiku jaoks kastikese loomine
    # Valuuta kurss, mida soovitakse teisendada
    valuuta_kurss1 = customtkinter.CTkLabel(master=raam,
                                        text="Kurss, mida teisendada: ",
                                        width=25,
                                        height=25,
                                        corner_radius=8, font=customtkinter.CTkFont(family="Helvetica", size=14))
    valuuta_kurss1.place(relx=0.2, rely=0.3, anchor=tkinter.CENTER)
    def valuuta_valik1(valuuta):
        print("Valisite valuuta kursiks:", valuuta)

    valuuta_combobox1 = customtkinter.CTkComboBox(master=raam,
                                                 values=valuuta_list,
                                                 command=valuuta_valik1)
    valuuta_combobox1.place(relx=0.2, rely=0.38, anchor=tkinter.CENTER)
    valuuta_combobox1.set("")

    # Valuuta kursi valiku jaoks kastikese loomine
    # Valuuta kurss, milleks soovitakse teisendada ehk kurss, mida soovitakse saada
    valuuta_kurss2 = customtkinter.CTkLabel(master=raam,
                                        text="Kurss, milleks teisendada: ",
                                        width=25,
                                        height=25,
                                        corner_radius=8, font=customtkinter.CTkFont(family="Helvetica", size=14))
    valuuta_kurss2.place(relx=0.8, rely=0.3, anchor=tkinter.CENTER)
    def valuuta_valik2(valuuta):
        print("Valisite valuuta kursiks:", valuuta)

    valuuta_combobox2 = customtkinter.CTkComboBox(master=raam,
                                                 values=valuuta_list,
                                                 command=valuuta_valik2)
    valuuta_combobox2.place(relx=0.8, rely=0.38, anchor=tkinter.CENTER)
    valuuta_combobox2.set("")

    #loon ka tulemuse sildi, mis siis annab kasutajale teada, et kas mõni lahter on täitmata või valesti täidetud
    tulemus_silt = customtkinter.CTkLabel(master=raam,
                                    text="",
                                    width=120,
                                    height=25,
                                    corner_radius=8, font=customtkinter.CTkFont(family="Helvetica", size=14))
    tulemus_silt.place(relx=0.5, rely=0.65, anchor=tkinter.CENTER)

    #defineerin nupu väärtuse, mida ma tahan kuvada kasutajale, peale seda, kui ta on vajutanud nupule "Arvuta"
    def nupu_väärtus():
        summa = summa_sisend.get()
        # kuna textbox on alati str type, siis proovime try exceptiga teda muuta floatiks ning 2 komakohta peale koma
        # aga proovime convertida, kui õnnestub, siis prindime kasutajale tühja teate ehk mitte midagi ja kui ei, siis
        # kirjutame kasutajale sõnumina teate, mida kasutaja peab muutma või lisama
        
        try:
            summa = round(float(summa),2)
        except:
            tulemus_silt.configure(text="Palun sisestage summa numbrites", text_color="red")
        # tingimus1, kui summa on täisarv, siis veateadet ei kuvata
        if isinstance(summa, int):
            tulemus_silt.configure(text="", text_color="green")
        # tingimus2, kui summa on ujukomaarv, siis veateadet ei kuvata
        if isinstance(summa, float):
            tulemus_silt.configure(text="", text_color="green")
        # tinimgus3, kui kasutaja pole valinud kummagist valuuta valikust midagi, siis annab kasutajale teada, et ta peab valikud tegema
        if valuuta_combobox1.get() == "" or valuuta_combobox2.get() == "":
            tulemus_silt.configure(text="Palun valige valuuta", text_color="red")
        # tingimus4, kui summa lahtrisse on kirjutatud sõne, siis kuvame veateate
        if isinstance(summa,str):
            tulemus_silt.configure(text="Palun sisestage summa numbrites", text_color="red")
        # tingimus5, kui summa lahter on tühjaks jäetud, siis kuvame kasutajale veateate
        if summa == "":
            tulemus_silt.configure(text="Palun sisestage summa numbrites", text_color="red")

    # loome nupu, peale mida kuvatakse vajalik info, või veateated vms
    nupp = customtkinter.CTkButton(master=raam,
                                     width=120,
                                     height=32,
                                     border_width=0,
                                     corner_radius=8,
                                     text="Arvuta",
                                     command=nupu_väärtus)
    nupp.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    valuuta_aken.mainloop()

if __name__ == "__main__":
    run()