import requests
import xml.etree.ElementTree as ET


def fetch_forex():
        
    sonade_list = ['Cube', '>', '<' , "'" , '=' , 'rate', 'currency', '/']
    currency_list = []
    ordered_currency = []

    url_of_xml = 'https://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml'
    xml_data = requests.get(url_of_xml)
    data = 'forex_daily.txt'
    with open(data, 'w+') as file:
        file.write(xml_data.text)
        file.close()

    with open('forex_daily.txt') as file:
        for line in file:
            if '.' in line:
                for element in sonade_list:
                    line = line.replace(element, '')
                currency_list.append(line)
    currency_list = currency_list[2:]
                                
    for el in currency_list:
        el = el.strip()
        el = el.split(' ')
        ordered_currency.append(el)
    for el in ordered_currency:
        index = ordered_currency.index(el)
        ordered_currency[index][1] = float(ordered_currency[index][1])
    ordered_currency.insert(0 , ['EUR', 1])
    return(ordered_currency)

def show_cur():
    valuuta_nimed = []
    for i in fetch_forex():
        valuuta_nimed.append(i[0])
    return(valuuta_nimed)

def def_cur(cur1, cur2):
    cur_list = show_cur()
    money_list = fetch_forex()
    name1 = cur_list.index(cur1)
    name2 = cur_list.index(cur2)
    name1 = money_list[name1][1]
    name2 = money_list[name2][1]
    return(name1, name2)

def fx_converter(sisend, cur1, cur2):
    exh_rate = (sisend/cur1)*cur2
    return(exh_rate)