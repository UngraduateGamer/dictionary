dict={'rahul':'a programmer',
      'age':18,
      'eligible':True}
print(dict['rahul'])  # if rahul is not present . throws an error
print(dict.get('rahul')) # if rehul is not present return None

print(dict.keys()) # print keys
print(dict.values()) # print values
print(dict.items()) # print key and values
for keyss,valuess in dict.items():
    print(f"The value of the {keyss} is {valuess}")

for i in dict.keys():  
    print(dict[i])

name1=input("Enter your Name: ")
age=int(input("Enter your Age: "))
dict1={'name':name1,
       'Age':age,
       'eligible':True}

dict2={'friend1':'nikhil',
       'friend2:':'bishan'}
dict1.update(dict2)
dict1.items()

for k,v in dict1.items():
    print(f"The value of the corresponding key {k} is {v}")

d1={'name':"rahul",
    'age':18,
    'canvote':True}
d1.pop('age')   # remove age key values 
print(d1)

d1={'name':"rahul",
    'age':18,
    'canvote ':True}
d1.clear()   # remove all key values in dictionary
print(d1)

d1={'name':"rahul",
    'age':18,
    'canvote ':True}
del d1 # remove  dictionary
print(d1)

d1={'name':"rahul",
    'age':18,
    'canvote ':True}
del d1['age'] # remove age in   dictionary
print(d1)

d1={'name':"rahul",
    'age':18,
    'canvote ':True}
d1.popitem() # remove last key value pairs in dictionary
print(d1)

