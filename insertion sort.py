import time 
from criaConjuntos import cria_conjuntos
from fazGraficos import fazGraficos

# https://www.geeksforgeeks.org/insertion-sort-algorithm/

# Python program for implementation of Insertion Sort

# Function to sort array using insertion sort
def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def main():
    tamanhos=[20000,40000,60000,80000,100000]
    tempos_a=[]
    tempos_b=[]
    tempos_c=[]
    tempos_d=[]
    
    for j in tamanhos:
        print('Tamanho do array:' ,j)
        for i in range(3):
            start = time.time()
            arr = cria_conjuntos(j, i+1)
            insertionSort(arr)
            tempo =time.time() - start
            print('Conjunto ',i+1,': ', tempo*1000, 'ms')
            if i==0:
                tempos_a.append(tempo)
            elif i==1:
                tempos_b.append(tempo)
            else:
                tempos_c.append(tempo)

    tempos=[tempos_a,tempos_b,tempos_c,tempos_d]
    
    fazGraficos(tamanhos,tempos,'Insertion Sort')



if __name__ == "__main__":
    main()
