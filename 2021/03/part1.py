from sys import stdin

ones_zeros_count = [
    {
        'ones': 0,
        'zeros': 0
    },{
        'ones': 0,
        'zeros': 0
    },{
        'ones': 0,
        'zeros': 0
    },{
        'ones': 0,
        'zeros': 0
    },{
        'ones': 0,
        'zeros': 0
    },{
        'ones': 0,
        'zeros': 0
    },{
        'ones': 0,
        'zeros': 0
    },{
        'ones': 0,
        'zeros': 0
    },{
        'ones': 0,
        'zeros': 0
    },{
        'ones': 0,
        'zeros': 0
    },{
        'ones': 0,
        'zeros': 0
    },{
        'ones': 0,
        'zeros': 0
    },
]

for line in stdin:
    for i in range(0, len(line.rstrip())):
        if line[i] == '1':
            ones_zeros_count[i]['ones'] += 1
        else:
            ones_zeros_count[i]['zeros'] += 1

gamma_rate = ''
epsilon_rate = ''
for count in ones_zeros_count:
    if count['ones'] > count['zeros']:
        gamma_rate += '1'
        epsilon_rate += '0'
    else:
        gamma_rate += '0'
        epsilon_rate += '1'

gamma_rate = int(gamma_rate, 2)
epsilon_rate = int(epsilon_rate, 2)

print(gamma_rate * epsilon_rate)
