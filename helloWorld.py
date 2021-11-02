# var= 'mundo'
# print (var)  

# pruebapares = 0
# comparison= pruebapares % 2

# while comparison == 0 and pruebapares <101:
#     print(pruebapares)
#     pruebapares += 1




# for i in range (1, 100, 2):
#     print ( i )
primenums =[]

for n in range(1,101):
    contador=0
    for i in range (1, n+1):
        if n%i ==0:
            contador = contador +1
    if contador == 2:
        primenums.append(n)
print(primenums)