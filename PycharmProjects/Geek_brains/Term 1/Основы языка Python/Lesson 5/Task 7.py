import json
f = open("file_task7.txt", 'r')
profits = 0
c = 0
spisok = []
profit_vsex = {}
av_prof = {}
spisok.append(profit_vsex)
spisok.append(av_prof)
for firm in f.read().split('\n'):
    firm_profit = 0
    firm_profit += int(firm.split()[2]) - int(firm.split()[3])
    profit_vsex[firm.split()[0]] = firm_profit
    if firm_profit >= 0:
        profits += firm_profit
        c += 1
av_prof['Average profit'] = profits / c
print(spisok)
fj = open('file_j_task7', 'w')
json.dump(spisok, fj)
