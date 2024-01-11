my_dict = {'key1':'value1','key2':'value2'} # dictionary
print(my_dict)
print(my_dict['key1']) # value1

prices_lookup = {'apple':2.99,'oranges':1.99,'milk':5.80} # dictionary
print(prices_lookup['apple']) # 2.99

d = {'k1':123,'k2':[0,1,2],'k3':{'insideKey':100}} # dictionary
print(d['k2']) # [0,1,2]
print(d['k3']['insideKey']) # 100
print (d['k2'][2]) # 2

d = {'key1':['a','b','c']} # dictionary
print(d)
my_list = d['key1'] # list
letter = my_list[2] # c
print(letter) # c
print(letter.upper()) # C
print(d['key1'][2].upper()) # C

d = {'k1':100,'k2':200} # dictionary
print(d)
d['k3'] = 300 # dictionary
print(d) # {'k1': 100, 'k2': 200, 'k3': 300}
d['k1'] = 'NEW VALUE' # dictionary
print(d) # {'k1': 'NEW VALUE', 'k2': 200, 'k3': 300}
print(d.keys()) # dict_keys(['k1', 'k2', 'k3'])
print(d.values()) # dict_values(['NEW VALUE', 200, 300])
print(d.items()) # dict_items([('k1', 'NEW VALUE'), ('k2', 200), ('k3', 300)])
