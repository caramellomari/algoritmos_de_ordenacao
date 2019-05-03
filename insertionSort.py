import sys,time

import csv

arquivo = open('lista.txt')
linhas = csv.reader(arquivo)

input_array = []
for linha in linhas:
    input_array.append(linha)

def insertionSort(array):
    global count
    length=len(array)
    for index in range(1,len(array)):
        currentvalue = array[index]
        position = index

        while (position>0 and array[position-1]>currentvalue):
            array[position]=array[position-1]
            position = position-1

            
		
       
        array[position]=currentvalue

array = input_array
insertionSort(array)
time1 = time.time()
print(array)
print ("Tempo de execução: " + str(time.time()-time1) + " segundos")
