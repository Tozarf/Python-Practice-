# var= 'mundo'
# print (var)  

# pruebapares = 0
# comparison= pruebapares % 2

# while comparison == 0 and pruebapares <101:
#     print(pruebapares)
#     pruebapares += 1




# for i in range (1, 100, 2):
#     print ( i )
for num in range(1,101):
    for i in range(2,num):
        if (num%i==0):
            break
        else:
            print(num)
            break