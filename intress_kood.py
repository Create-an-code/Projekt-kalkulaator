import json
import requests
def euribor():
    euribor_link = 'https://data-api.ecb.europa.eu/service/data/FM/M.U2.EUR.RT.MM.EURIBOR6MD_.HSTA?lastNObservations=1&detail=dataonly&format=jsondata'
    text = requests.get(euribor_link, allow_redirects=True)
    open('6_month.json', 'wb').write(text.content)
    file = open('6_month.json')
    data = json.load(file)
    act_info = (data['dataSets'])
    act_info = (act_info[-1])
    act_info = act_info['series']
    act_info = act_info['0:0:0:0:0:0:0']
    act_info = act_info['observations']
    euribor=(next(reversed(act_info.values())))
    euribor = euribor[0]
    return euribor

def LaenuArvutus(laenusumma, intress, kuud):
    euriboor = euribor()
    print(euriboor)
    print(intress)
    intress = round((((intress + euriboor)/100)/12),5)
    print(intress)
    vastus = laenusumma * intress * (1.0 + intress)**kuud / (((1.0 + intress)**kuud) - 1.0)
    kuumakse = round(vastus,2)
    kogusumma = (round((vastus*kuud),2))
    return(kuumakse, kogusumma)