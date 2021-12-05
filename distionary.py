# I am going to create a python dictionary

car1 = {        
    #property:value
    "brand":'TATA',
    'model':'nexon',
    'myear':'2020',
    'brand':'maruty'
}
#  does not allow dublicate python dictionary 
print(car1)
#dictname['propertyname']
print("I have a "+car1['brand'] +" "+ car1['model'] +" " + 'car.')

print(f"I have a {car1['brand']} nexon car2")

friends = {
    "name":"ritik",
    "surname":"patidar",
    "contect":"9074171872",
}

print(friends)
#now i want to change the surname 
friends['surname'] = "bheelavat"
print(friends)
# now i going to create a new property

# dictnme['newpropertyname'] = 'value'
friends['address'] = 'jeeran'

print(friends)
#now i going to remove a property contect
del friends['contect']
print(friends)
#access the property name
print("my friend name is "+ friends.get('name'))