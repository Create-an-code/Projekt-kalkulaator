import requests
import csv
#currency_url = 'https://www.eestipank.ee/valuutakursid'
#file = 

valuutafail = 'article-report(4).csv'
valuutadict = {}
data = []
with open('article-report(4).csv') as csv:
    lines = csv.reader()
with open(valuutafail, 'r') as csv:
    for line in data[3:]:
        
        # line = line.removesuffix('\n')
        # rida = line.split(',')
        # print(rida)
        # rida = dict([rida])
        # #valuutadict.update({dict(zip(rida))})
        csv.write(line)

#euribor_url = 