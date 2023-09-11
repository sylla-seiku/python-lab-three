# Learning Nested Loops
for x in range(4):
    print(x)

for x in range(4):   #outer loop
    for y in range(3):  #inner loop
        print(f'({x}, {y})')

#practice writting the letter "F" and "L" using nested loops
numbers = [5, 2, 5, 2, 2]
for x_count in numbers:
    print('x' * x_count)


numbers = [2, 2, 2, 2, 5]
for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'x'

    print(output)





'''
# Learning For Loops
for item in ['Seiku', 'Beyage', 'Ebrahim']: # "[]" this right here defines a list.
    print(item)

for item in [1, 2, 3, 4,]:
    print(item)

for item in range(5, 10, 2): #range creats an object we can irrerate over. the first num is count 2nd num it ends 3rd num is the steps
    print(item)



for item in 'Python':
    print(item)

#practice
prices = [10, 20, 30]

total = 0
for price in prices:
    total += price
print(f"Total: {total}")
'''



'''
#learning While Loops
i = 1
while i <= 5:
    print('*' * i)
    i += 1
print("Done")
'''