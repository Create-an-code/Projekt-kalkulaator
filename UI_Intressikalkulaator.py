import tkinter
import customtkinter

def run():
    
    # Akna loomine
    intress_aken = tkinter.Tk()
    intress_aken.geometry("500x500")
    intress_aken.title("Intressikalkulaator")

    #fondi valimine, valisime Helvetica fondi
    font1 = customtkinter.CTkFont(family="Helvetica", size=16, weight="bold")

    # Raami loomine
    raam = customtkinter.CTkFrame(master=intress_aken,
                                   width=400,
                                   height=400,
                                   corner_radius=10)
    raam.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    # Pealkirja sildi loomine intressikalkulaatori jaoks
    pealkiri_silt = customtkinter.CTkLabel(master=intress_aken,
                                   text="Intressikalkulaator",
                                   width=120,
                                   height=25,
                                   corner_radius=8,font=font1)
    pealkiri_silt.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)
    
    # Summa tekstiväli kasutajale
    # Summa silt tekstiväljale
    # Summa, mida kasutaja soovib laenuna võtta
    summa_sisend = customtkinter.CTkEntry(master=raam,
                                          width=120,
                                          height=25,
                                          corner_radius=10)
    summa_sisend.place(relx=0.5, rely=0.17, anchor=tkinter.CENTER)
    summa_silt = customtkinter.CTkLabel(master=raam,
                                        text="Sisestage summa, palju soovite laenu võtta:",
                                        width=120,
                                        height=25,
                                        corner_radius=8, font=customtkinter.CTkFont(family="Helvetica", size=14))
    summa_silt.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)

    # Kuude arvu tekstiväli
    # Kasutaja sisestab, mitmeks kuuks soovib laenu võtta
    kuu_sisend = customtkinter.CTkEntry(master=raam,
                                          width=120,
                                          height=25,
                                          corner_radius=10)
    kuu_sisend.place(relx=0.5, rely=0.35, anchor=tkinter.CENTER)
    kuu_silt = customtkinter.CTkLabel(master=raam,
                                        text="Mitmeks kuuks soovite laenu võtta: ",
                                        width=120,
                                        height=25,
                                        corner_radius=8, font=customtkinter.CTkFont(family="Helvetica", size=14))
    kuu_silt.place(relx=0.5, rely=0.27, anchor=tkinter.CENTER)

    # Euribori sildi loomine, mille väärtus kuvatakse kasutajale
    Euribor_silt = customtkinter.CTkLabel(master=raam,
                                        text="Euribor: {vaartus}",
                                        width=25,
                                        height=25,
                                        corner_radius=8, font=customtkinter.CTkFont(family="Helvetica", size=14))
    Euribor_silt.place(relx=0.5, rely=0.75, anchor=tkinter.CENTER)

    # Küsime kasutajalt intressimäära, mis tohib olla ujukomaarv, kuid peale koma mitte rohkem kui 2 kohta
    # Intressimäära silt, mis kuvatakse kasutajale ning näitamaks, kui suur on intressimäär
    intress_sisend = customtkinter.CTkEntry(master=raam,
                                          width=120,
                                          height=25,
                                          corner_radius=10)
    intress_sisend.place(relx=0.5, rely=0.53, anchor=tkinter.CENTER)
    intress_silt = customtkinter.CTkLabel(master=raam,
                                        text="Palun sisestage intressimäär: ",
                                        width=120,
                                        height=25,
                                        corner_radius=8, font=customtkinter.CTkFont(family="Helvetica", size=14))
    intress_silt.place(relx=0.5, rely=0.45, anchor=tkinter.CENTER)

    #loon ka tulemuse sildi, mis siis annab kasutajale teada, et kas mõni lahter on täitmata või valesti täidetud
    tulemus_silt = customtkinter.CTkLabel(master=raam,
                                    text="",
                                    width=120,
                                    height=25,
                                    corner_radius=8, font=customtkinter.CTkFont(family="Helvetica", size=14))
    tulemus_silt.place(relx=0.5, rely=0.85, anchor=tkinter.CENTER)

    
    #defineerin nupu väärtuse, mida ma tahan kuvada kasutajale, peale seda, kui ta on vajutanud nupule "Arvuta"
    def nupu_väärtus():
        kuu = kuu_sisend.get()
        summa = summa_sisend.get()
        intressimaar = intress_sisend.get()
        # kuna textbox on alati str type, siis proovime try exceptiga summa lahtrit muuta floatiks ning 2 komakohta peale koma
        # aga proovime convertida, kui õnnestub, siis prindime kasutajale tühja teate ehk mitte midagi ja kui ei, siis
        # kirjutame kasutajale sõnumina teate, mida kasutaja peab muutma või lisama
        try:
            summa = round(float(summa),2)
        except:
            tulemus_silt.configure(text="Palun sisestage summa numbrites", text_color = "red")
        # try exceptiga vaatan, et kui kasutaja sisestab komaga arvu, siis kuvab kasutajale veateate
        # Kasutaja peab kuude arvuks sisestama ainult täisarvud
        try:
            kuu = int(kuu)
        except:
            tulemus_silt.configure(text="Palun sisestage kuude arv täisarvudes", text_color = "red")
        # kuna textbox on alati str type, siis proovime try exceptiga intressimäära lahtrit muuta floatiks ning 2 komakohta peale koma
        # aga proovime convertida, kui õnnestub, siis prindime kasutajale tühja teate ehk mitte midagi ja kui ei, siis
        # kirjutame kasutajale sõnumina teate, mida kasutaja peab muutma või lisama
        try:
            intressimaar = int(float(intressimaar))
        except:
            tulemus_silt.configure(text="Palun sisestage intressimäär numbrites", text_color = "red")
        # tingimus1, kui summa on täisarv, siis veateadet ei kuvata
        if isinstance(summa, int):
            tulemus_silt.configure(text="", text_color = "green")
        # tingimus2, kui summa on ujukomaarv, siis veateadet ei kuvata
        if isinstance(summa, float):
            tulemus_silt.configure(text="", text_color = "green")
        # tingimus3, kui kuude arv on täisarv, siis veateadet ei kuvata
        if isinstance(kuu, int):
            tulemus_silt.configure(text="", text_color = "green")
        # tingimus4, kui summa lahter on tühjaks jäetud, siis kuvatakse veateade
        if summa == "":
            tulemus_silt.configure(text="Palun sisestage summa numbrites", text_color = "red")
        # tingimus5, kui kuude lahter on tühjaks jäetud, siis kuvatakse veateade
        if kuu == "":
            tulemus_silt.configure(text="Palun sisestage kuude arv täisarvudes", text_color = "red")
        # tingimus6, kui summa lahtris on sõne ehk string, siis kuvame veateate
        if isinstance(summa,str):
            tulemus_silt.configure(text="Palun sisestage summa numbrites", text_color = "red")
        # tingimus7, kui kuude lahtris on sõne ehk string, siis kuvame veateate
        if isinstance(kuu, str):
            tulemus_silt.configure(text="Palun sisestage kuude arv täisarvudes", text_color = "red")
        # tingimus8, kui kasutaja sisestatud intressimäär on täisarv, siis veateadet ei kuva
        if isinstance(intressimaar,int):
            tulemus_silt.configure(text="", text_color = "green")
        # tingimus9, kui kasutaja sisestatud intressimäär on float ehk ujukomaarv, siis veateadet ei kuvata
        if isinstance(intressimaar,float):
            tulemus_silt.configure(text="", text_color = "green")
        # tingimus10, kui kasutaja sisestaud intressimäär on sõne ehk string, siis kuvame kasutajale veateate
        if isinstance(intressimaar,str):
            tulemus_silt.configure(text="Palun sisestage intressimäär numbrites", text_color = "red")
        # tingimus11, kui intressimäära lahter jäetakse tühjaks, siis kuvatakse kasutajale veateade
        if intressimaar == "":
            tulemus_silt.configure(text="Palun sisestage intressimäär numbrites", text_color = "red")

    # loome nupu, peale mida kuvatakse vajalik info, või veateated vms
    nupp = customtkinter.CTkButton(master=raam,
                                     width=120,
                                     height=32,
                                     border_width=0,
                                     corner_radius=8,
                                     text="Arvuta",
                                     command=nupu_väärtus)
    nupp.place(relx=0.5, rely=0.65, anchor=tkinter.CENTER)

    intress_aken.mainloop()

if __name__ == "__main__":
    run()