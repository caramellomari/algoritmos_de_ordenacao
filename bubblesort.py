import sys,time

import csv

arquivo = open('lista.txt')
linhas = csv.reader(arquivo)

input_array = []
for linha in linhas:
    input_array.append(linha)


def bubbleSort(array):
        
	length=len(array)
	result = True
	global count
	while result:
		result = False
		i=0
		while (i < length-1):
			if (array[i] > array[i+1]):
				tempVar = array[i]
				array[i] = array[i+1]
				array[i+1] = tempVar
				result = True
				
			i=i+1
			count+=1
			print ("Sorting: " + str(array))
			
	return array
    
count = 0
time1 = time.time()
arrayResult = str(bubbleSort(input_array))
print ("")
print ("Quantidade de trocas: " + str(count))
print ("Trocas:  " + arrayResult)
print ("---")
print ("Tempo de execução: " + str(time.time()-time1) + " segundos")

