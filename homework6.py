my_dict = {'Alex': 1989, 'Stan':1997, 'Philip':1975,'Andrew':2002}
print(my_dict)
print(my_dict.get('Alex','Нет таких тут'))
print(my_dict.get('Jenny','Нет таких тут'))
my_dict.update({'James':1994, 'Michael':1991})
a=my_dict.pop('Stan')
print(a)
print(my_dict)
my_set={1,2,3,5,7,22,2,1,'Fun',True,'Ride',5,13,22,'Fun',(1,2,2.5)}
print(my_set)
my_set.add(5)
my_set.add((9,3.2,'Fat'))
my_set.discard(22)
print(my_set)