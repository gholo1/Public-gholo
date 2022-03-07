money = float(input("Введите сумму:"))
per_cent = {'TKB_deposit': 5.6, 'SKB_deposit': 5.9, 'VTB_deposit': 4.28, 'SBER_deposite': 4.0}
TKB_deposit = money * per_cent['TKB_deposit']/100
SKB_deposit = money * per_cent['SKB_deposit']/100
VTB_deposit = money * per_cent['VTB_deposit']/100
SBER_deposite = money * per_cent['SBER_deposite']/100
deposite = []
deposite.append(TKB_deposit)
deposite.append(SKB_deposit)
deposite.append(VTB_deposit)
deposite.append(SBER_deposite)
print('ТКБ=',TKB_deposit,'СКБ=',SKB_deposit,'ВТБ=',VTB_deposit,'СБЕР=',SBER_deposite)
print('Максимальная сумма, которую вы можете заработать=',max(deposite))

