"""
author : nero chaniago
email : nerochaniago@student.telkomuniversity.ac.id
"""
from operator import itemgetter

list = []
hasil_hitung = []

#definisikan kapasitas
kapasitas = 16

#variabel
profit = 0
weight = 0
profit_weight = 0
min_weight = 0
profit_pi_wi = 0
max_pi_wi = 0
kapasitas_pi_wi = kapasitas
kapasitas_min_weight = kapasitas

#definisikan weight dan profit di setiap item
dataset_1 = {'weight' : 6, 'profit' : 12, 'max_pi_wi': 0}
dataset_2 = {'weight' : 5, 'profit' : 15, 'max_pi_wi': 0}
dataset_3 = {'weight' : 10, 'profit' : 50, 'max_pi_wi': 0}
dataset_4 = {'weight' : 5, 'profit' : 10, 'max_pi_wi': 0}

#masukan dict dataset ke list
list.append(dataset_1)
list.append(dataset_2)
list.append(dataset_3)
list.append(dataset_4)

#ambil dataset dengan maksimum profit
list.sort(key=itemgetter('profit'), reverse=True)

for row in list:
    profit = profit + row['profit']
    weight = weight + row['weight']
    kapasitas = kapasitas - row['weight']
    if kapasitas <= 1 or kapasitas == 0:
        break

print('total profit yang di dapat dari dataset max profit : ', str(profit))
print('total weight yang di dapat dari dataset max profit : ', str(weight))

#ambil item dengan minimum weight
list.sort(key=itemgetter('weight'),reverse=False)

for j in list:
    profit_weight = profit_weight + j['profit']
    min_weight = min_weight + j['weight']
    kapasitas_min_weight = kapasitas_min_weight - j['weight']
    if kapasitas_min_weight <= 1 or kapasitas_min_weight == 0:
        break

print('total profit yang di dapat dari dataset min weight : ', str(profit_weight))
print('total weight yang di dapat dari dataset min weight : ', str(min_weight))

#ambil item dengan maximum (Pi/Wi)
for i in list:
    nilai = i['profit'] / i['weight']
    i['max_pi_wi'] = nilai

list.sort(key=itemgetter('max_pi_wi'),reverse=True)
for n in list:
    profit_pi_wi = profit_pi_wi + n['profit']
    max_pi_wi = max_pi_wi + n['weight']
    kapasitas_pi_wi = kapasitas_pi_wi - n['weight']
    if kapasitas_pi_wi <= 1 or kapasitas_pi_wi == 0:
        break

print('total profit yang di dapat dari dataset max pi/wi : ', str(profit_pi_wi))
print('total weight yang di dapat dari dataset max pi/wi : ', str(max_pi_wi))
