value1 = 123405 #результат = 120
value2 = 999 #результат = 729
value3 = 1000 #результат = 1
value4 = 1111 #результат = 1
z = 1

for i in str(value1):
    if i == '0':
        continue
    else:
        z = z * int(i)
    
print(z)