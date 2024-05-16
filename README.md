# Projekt-kalkulaator
RAM0620 programmeermimise kursuse projekti hoidla

_Projekti plaan/kirjeldus_
RAHA KALKULAATOR

A. Programm võimaldab kasutajatel arvutada erinevaid rahalisi toiminguid, logida finantstehinguid ning arvutada intressi või valuutakursside muutumist.

B. Oleme ajaliselt maas ning lisame antud info 08.04. 

Programmi ehitamiseks kasutame pythonit. Kalkulaatori kasutajaliidese loomiseks kasutame Tkinteri moodulit. 

C. Erik ning Marcus - internetist info pullimine, et saada reaalajas valuutakursse ning euribori, nende andmete söödavaks tegemine pythonile

Oliver ja Patrik - Front-end dev., kalkulaatori tegemine :)

D. 05.04-23.04 - info otsimine

23.04 - vahearuande koostamise hetk - Selleks hetkeks peab olema info kursside ja muu kohta kätte saadud, saab juba tasakesi alustada programmi koodi koostamisega.

24.04-10.05 - 

10.05 peab valmis olema (tegelik tähtaeg 16.05, kui on esitlus), sest muidu laseme uuesti tähtaja mööda.


_Projekti_vahearuanne_

 24.04-  olime loonud 2 koodifaili (UI), üks intressikalkulaatori jaoks ning teine valuutakalkulaatori jaoks. Olime loonud TKinteri abil kasutajale sisestamiseks vajalikud väljad. Probleemiks võiks pidada tingimuste kirjutamist, et mis tingimused ja väljad peavad olema täidetud, et kasutajale kuvada soovitud kalkulaatori tulemid. Nimelt oli probleeme str konventeerimisel floatiks. 
 06.05 - Lõime kolmanda koodifaili (main), mis kuvab kasutajale valikuna, millist kalkulaatorit soovib kasutaja kasutada ning avab kalkulaatori akna. Siinkohal oli probleeme selles, et kuidas ühendada failid omavahel ning, et sulgeks main faili akna peale seda, kui on avanud kalkulaatori akna. Õppisime ühendama mitmeid TKinteri koodifaile ning TKinteri mooduli rakendamist üleüldiselt.
 12.05 - lõime arvutuslikud koodifailid mõlema kalkulaatori jaoks, mis tõmbab Euroopa Keskpangast iga kord värsked andmed alla. Probleemiks või raskuseks oli xml tüüpi failide töötlemine ning Euroopa Keskpanga IP aadressiga tegelemine, valuutakalkulaatoriga oli vähe lihtsam, kuna andmeid mida töödelda on valuutakalkulaatoris vähem. 

_Lõpparuanne_

A. Projekt sai edukalt kuid planeeritust 3 päeva hiljem valmis.

B. Teostatud tööd
- tegime lihtsa plaani, kuidas programm võiks välja näha plokkskeemis
- jagasime meeskonna pooleks
- kirjutasime koodi
- 

C. Panused polnud projektis võrdsed, kuid need polnud ka kodutööde tegemisel võrdsed. Ühte tegid ühed inimesed rohkem, teist teine meeskonna pool. Seega üldine panus meeskonda oli kursuse mõttes ühtlane ning keegi ära ei kadunud. 

D. Projekti tugevus on see, et info mõlema kalkulaatori jaoks on ajakohane, st et me uuendame pidevalt andmeid ning ei pea manuaalselt faile uute valuuta ning euribori väärtustega uuendama. Selle töö teeb ära Euroopa Keskpanga API, mida iga kord callime. Nõrkuseks see, et igal uuel arvutamisel teeme ECBle uue calli, igal käivitusel võiks olla logifail, mis kontrollib viimast andmete uuendust, ning kui vajadust ei ole, siis ei tee uut API calli (valuutainfo uueneb päevas korra, seega võiks teha kontrolli, kas tänased andmed on juba alla tõmmatud)

E. Väga palju arendada ei saaks, kuna selliseid programme on piisavalt. Lisaks on nad palju kiiremad jne, firmat selle pealt ehitada ei saaks.
