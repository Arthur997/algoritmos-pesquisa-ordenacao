#metodo de pesquisa que necessita de uma lista ORDENADA
#com isso ele procura o item desejado apartir do meio da lista
#e checa se o item esta na metade inferior ou superior
#e repete o processo ate chegar no item desejado.
import math

def binary_search(list, goal):
    
    index_max=len(list)-1
    index_min=0
    
    while index_min <= index_max:
        
        index_midle = math.floor((index_max+index_min)/2)
        item = list[index_midle]
        if goal < item:
            index_max = index_midle - 1
            print("menor")
        
        elif goal > item:
            index_min = index_midle + 1
            print("maior")
        else: return index_midle
        
    
x = binary_search([0,1,2,3,4,5], 5)
print(x)

#esse processo leva O(log n) para executar, oq é bem rapido. 