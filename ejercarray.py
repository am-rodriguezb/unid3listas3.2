import numpy as np 
#forma 1 lista
lista=[1,2,3,4]
arr = np.array(lista)
#print(arr)
# forma 2 directa
arr2=np.array([5,6,7,8])
#print(arr2)

#funciones con arreglos
#arreglo=np.array([5,6,7,8,9,10,11,12])

# print(arreglo.ndim) dimension
# print(len(arreglo)) el tamaño de la arreglo
# print(arreglo[4:7]) pociciciones exactas
# print(arreglo[0:7:2]) de pocicion / hasta la pocicion / en paso de 
# print(arreglo[::3]) se salta 
c=[i for i in range(0,100)]
print(c[1::2]) #numeros impares
print(c[2::2]) #numero pares
