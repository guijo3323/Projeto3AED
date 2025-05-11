import time
from criaConjuntos import cria_conjuntos
from fazGraficos import fazGraficos

# https://www.geeksforgeeks.org/heap-sort/

# # Python program for implementation of heap Sort

# To heapify a subtree rooted with node i
# which is an index in arr[].
def heapify(arr, n, i):
    
     # Initialize largest as root
    largest = i 
    
    #  left index = 2*i + 1
    l = 2 * i + 1 
    
    # right index = 2*i + 2
    r = 2 * i + 2  

    # If left child is larger than root
    if l < n and arr[l] > arr[largest]:
        largest = l

    # If right child is larger than largest so far
    if r < n and arr[r] > arr[largest]:
        largest = r

    # If largest is not root
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap

        # Recursively heapify the affected sub-tree
        heapify(arr, n, largest)

# Main function to do heap sort
def heapSort(arr):
    
    n = len(arr) 

    # Build heap (rearrange array)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # One by one extract an element from heap
    for i in range(n - 1, 0, -1):
      
        # Move root to end
        arr[0], arr[i] = arr[i], arr[0] 

        # Call max heapify on the reduced heap
        heapify(arr, i, 0)



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
            heapSort(arr)
            tempo =time.time() - start
            print('Conjunto ',i+1,': ', tempo*1000, 'ms')
            if i==0:
                tempos_a.append(tempo)
            elif i==1:
                tempos_b.append(tempo)
            else:
                tempos_c.append(tempo)

    tempos=[tempos_a,tempos_b,tempos_c]
    
    fazGraficos(tamanhos,tempos,'Heap Sort')



if __name__ == "__main__":
    main()