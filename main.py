from bs4 import BeautifulSoup
import yfinance as yf
import pandas as pd
import requests
import time
import json


def parsing(link: str):
    base = link
    html = requests.get(base).content
    soup = BeautifulSoup(html, 'lxml')
    return soup


table = {}
while True:
    try:
        for i in range(0, 251, 250):
            soup = parsing(f'https://finance.yahoo.com/screener/predefined/ms_technology?count=250&offset={i}')
            tbody = soup.find('tbody')
            symbol = tbody.find_all('a')
            name = tbody.find_all('td', class_='Va(m) Ta(start) Px(10px) Fz(s)')
            table.update({f"{symbol[j].get_text()}": name[j].get_text() for j in range(len(symbol))})
        break
    except ValueError:
        pass

print(table)

listik1 = []
n = 0
for item_symbol, item_name in table.items():
    try:
        r = requests.get(
            f"https://query1.finance.yahoo.com/v8/finance/chart/{item_symbol}?&period1=1615627623&period2=1618219623&interval=1d&includePrePost=true&events=div")
        # print(f'{item_symbol}', dict(json.loads(r.content)['chart']['result'][0]['events']['dividends']), end='\n \n')
        for i in dict(json.loads(r.content)['chart']['result'][0]['events']['dividends']).values():
            print(f'{item_symbol}', i)
            r = requests.get(f"https://query1.finance.yahoo.com/v10/finance/quoteSummary/{item_symbol}?modules=price,defaultKeyStatistics,financialData,summaryDetail")

        listik2 = [json.loads(r.content)['quoteSummary']['result'][0]['price']['marketCap']['raw'],
           json.loads(r.content)['quoteSummary']['result'][0]['defaultKeyStatistics']['forwardPE']['raw'],
           json.loads(r.content)['quoteSummary']['result'][0]['price']['marketCap']['raw'],
           json.loads(r.content)['quoteSummary']['result'][0]['defaultKeyStatistics']['enterpriseValue']['raw'],
           json.loads(r.content)['quoteSummary']['result'][0]['defaultKeyStatistics']['pegRatio']['raw'],
           json.loads(r.content)['quoteSummary']['result'][0]['defaultKeyStatistics']['priceToSalesTrailing12Months']]

        listik1.append(listik2)
        n += 1

        print(n, item_symbol,
              json.loads(r.content)['quoteSummary']['result'][0]['summaryDetail']['trailingPE']['raw'],
              json.loads(r.content)['quoteSummary']['result'][0]['price']['marketCap']['raw'],
              json.loads(r.content)['quoteSummary']['result'][0]['defaultKeyStatistics']['forwardPE']['raw'],
              json.loads(r.content)['quoteSummary']['result'][0]['price']['marketCap']['raw'],
              json.loads(r.content)['quoteSummary']['result'][0]['defaultKeyStatistics']['enterpriseValue']['raw'],
              json.loads(r.content)['quoteSummary']['result'][0]['defaultKeyStatistics']['pegRatio']['raw'],
              json.loads(r.content)['quoteSummary']['result'][0]['defaultKeyStatistics'][
                  'priceToSalesTrailing12Months']
              )
    except:
        pass

r = requests.get(f"https://query1.finance.yahoo.com/v8/finance/chart/ORCL?&period1=1615627623&period2=1618219623&interval=1d&includePrePost=true&events=div")

print(json.loads(r.content)['chart']['result'][0]['indicators']['adjclose'][0]['adjclose'], end='\n \n')

print(json.loads(r.content)['chart']['result'][0]['events']['dividends'], end='\n \n')

print(json.loads(r.content)['chart']['result'][0]['timestamp'], end='\n \n')

print(json.loads(r.content)['chart']['result'][0]['indicators']['quote'][0]['volume'], end='\n \n')

r = requests.get(f"https://query1.finance.yahoo.com/v10/finance/quoteSummary/ORCL?modules=incomeStatementHistoryQuarterly")

print(json.loads(r.content)['quoteSummary']['result'][0]['incomeStatementHistoryQuarterly']['incomeStatementHistory'][0]['totalRevenue']['raw'], end='\n \n')

print(json.loads(r.content)['quoteSummary']['result'][0]['incomeStatementHistoryQuarterly']['incomeStatementHistory'][1]['totalRevenue']['raw'], end='\n \n')

print(json.loads(r.content)['quoteSummary']['result'][0]['incomeStatementHistoryQuarterly']['incomeStatementHistory'][0]['grossProfit']['raw'], end='\n \n')

print(json.loads(r.content)['quoteSummary']['result'][0]['incomeStatementHistoryQuarterly']['incomeStatementHistory'][1]['grossProfit']['raw'], end='\n \n')

r = requests.get(f"https://query1.finance.yahoo.com/v10/finance/quoteSummary/ORCL?modules=balanceSheetHistoryQuarterly")

print(json.loads(r.content)['quoteSummary']['result'][0]['balanceSheetHistoryQuarterly']['balanceSheetStatements'][0]['longTermDebt']['raw'], end='\n \n')

print(json.loads(r.content)['quoteSummary']['result'][0]['balanceSheetHistoryQuarterly']['balanceSheetStatements'][1]['longTermDebt']['raw'], end='\n \n')

r = requests.get(f"https://query1.finance.yahoo.com/v8/finance/chart/APH?&period1=1615627623&period2=1618219623&interval=1d&includePrePost=true&events=div")

for i in dict(json.loads(r.content)['chart']['result'][0]['events']['dividends']).values():
    print(f'APH', i['amount'])
