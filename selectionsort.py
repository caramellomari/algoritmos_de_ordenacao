import random
import sys,time
import csv

arquivo = open('lista.txt')

linhas = csv.reader(arquivo)

input_array = []
for linha in linhas:
    input_array.append(linha)
    

def fill_array(array, num):
    for i in range(num):
        array.append(random.randint(1, num))

def selectionSort(array):
    
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if j >= len(array):
                break

            if array[i] > array[j]:
                temp = array[i]
                array[i] = array[j]
                array[j] = temp
       

def print_array(array):
    for i in range(len(array)):
        print(array[i], end=" ")
        if i != 0 and i % 10 == 0:
            print('')

def run():
    array = []
    num = int(input("Digite um número: "))

    fill_array(array, num)
    selectionSort(array)
    print_array(array)

if __name__ == '__main__':
    run()

time1 = time.time()
print ("")
print ("Tempo de execução: " + str(time.time()-time1) + " segundos")
