furniture = ['table', 'chair', 'rack', 'shelf']
print(furniture[0:4])

#//Using for loops with Lists//
furniture = ['table', 'chair', 'rack', 'shelf']
for item in furniture:
    print(item)


#//Getting the index in a loop with enumerate()//
furniture = ['table', 'chair', 'rack', 'shelf']
for index, item in enumerate(furniture):
       print(f'index: {index} - item: {item}')


#// Loop in Multiple Lists with zip()//

furniture = ['table', 'chair', 'rack', 'shelf']
price = [100, 50, 80, 40]
for item, amount in zip(furniture, price):
    print(f'The {item} costs ${amount}')

# /special/
if 'rack' in furniture:
    print("true")

if 'bed' not in furniture:
    print("not found")