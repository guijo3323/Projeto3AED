import time 
from criaConjuntos import cria_conjuntos
from fazGraficos import fazGraficos
import random

# https://www.geeksforgeeks.org/quick-sort-algorithm/


def partition(arr, low, high):
    meio= (low+high)//2
    # Choose the pivot
    pivot = arr[high]
    escolher = [(arr[low],low), (arr[meio],meio), (arr[high],high)]
    escolher.sort()
    pivot,indice_pivot=escolher[1]
    swap(arr, indice_pivot, high)
    # Index of smaller element and indicates 
    # the right position of pivot found so far
    i = low - 1
    
    # Traverse arr[low..high] and move all smaller
    # elements to the left side. Elements from low to 
    # i are smaller after every iteration
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            swap(arr, i, j)
    
    # Move pivot after smaller elements and
    # return its position
    swap(arr, i + 1, high)
    return i + 1

# Swap function
def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

# The QuickSort function implementation
def quickSort(arr, low, high):
    if low < high:
        
        # pi is the partition return index of pivot
        pi = partition(arr, low, high)
        
        # Recursion calls for smaller elements
        # and greater or equals elements
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)




def main():
    tamanhos=[200000,400000,600000,800000,1000000]
    tempos_a=[]
    tempos_b=[]
    tempos_c=[]

    for j in tamanhos:
        print('Tamanho do array:' ,j)
        for i in range(3):
            start = time.time()
            arr = cria_conjuntos(j, i+1)
            quickSort(arr,0,len(arr)-1)
            tempo =time.time() - start
            print('Conjunto ',i+1,': ', tempo*1000, 'ms')
            if i==0:
                tempos_a.append(tempo)
            elif i==1:
                tempos_b.append(tempo)
            else:
                tempos_c.append(tempo)

    tempos=[tempos_a,tempos_b,tempos_c]
    
    fazGraficos(tamanhos,tempos,'Quick Sort')


if __name__ == "__main__":
    main()